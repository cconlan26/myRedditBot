import praw
import pdb
import re
import os
import httplib2

header = '**Recipe found using the mentioned ingredients:**\n'
footer = '\n*---This recipe was found from https://developer.edamam.com/edamam-recipe-api | Bot created by u/cconlan26 | [Source code](https://github.com/cconlan26/recipeBot)*'

def reply():

    # Authenticating
    reddit = praw.Reddit('bot1')

    # subreddit that the bot is monitering
    subreddit = reddit.subreddit("pythonforengineers")


    # if apiKeys text file doesn't exist
    if not os.path.isfile("apiKeys.txt"):
        app_id = ""
        application_key = ""
    else:
        with open("apiKeys.txt") as f:
            keys = f.read()
            keys = keys.split("\n")
            app_id = keys[0]
            application_key = keys[1]


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
                ingredientsList = ', '.join(ingredients) + "\n"

                # Now we need to use the edamam api to find recipes
                resp, content = httplib2.Http().request("https://api.edamam.com/search?q=" + ingredientsList + "&app_id=${" + app_id + "&app_key=${" + application_key + "}")

                if (resp)

                # Replying to comment
                comment.reply(header + ingredientsList + footer)

                # Adding the comment id to the list
                commentIdHistory.append(comment.id)

    with open("commentIdHistory.txt", "w") as f:
        for post_id in commentIdHistory:
            f.write(post_id + "\n")
