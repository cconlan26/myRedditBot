import praw
import pdb
import re
import os

header = '**Recipe found using the mentioned ingredients:**\n'
footer = '\n*---This recipe was found from API_LINK | Bot created by u/cconlan26 | [Source code](https://github.com/cconlan26/recipeBot)*'


def reply():

    # Authenticating
    reddit = praw.Reddit('bot1')

    # subreddit that the bot is monitering
    subreddit = reddit.subreddit("pythonforengineers")

    # If text file doesn't exist
    if not os.path.isfile("commentIdHistory.txt"):
        commentIdHistory = []
    else:
        with open("commentIdHistory.txt") as f:
            commentIdHistory = f.read()
            commentIdHistory = commentIdHistory.split("\n")
            commentIdHistory = list(filter(None, commentIdHistory))

    # For every 250 comments in the subreddit
    for comment in subreddit.comments(limit = 250):

        if comment.id not in commentIdHistory:
            # Using regex to check if the body contains the phrase with a list of following ingredients
            if re.match("Find me a recipe with [a-zA-Z]+\s*(,\s*[a-zA-Z]+\s*)*", comment.body):

                # Need to tokenize the ingredients
                ingredients = comment.body.split("Find me a recipe with ")[1]
                ingredients = ingredients.split("\s*,\s*")

                # Converting the ingredients list into a readable format
                body = ', '.join(ingredients) + "\n"

                # Now we need to use the spoonacular api to find recipes
                #TODO: use api to get body


                # Replying to comment
                comment.reply(header + body + footer)

                # Adding the comment id to the list
                commentIdHistory.append(comment.id)

    with open("commentIdHistory.txt", "w") as f:
        for post_id in commentIdHistory:
            f.write(post_id + "\n")
