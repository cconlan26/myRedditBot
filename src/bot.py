import praw
import pdb
import re
import os
import json
import requests

header = '**Recipe found using the mentioned ingredients: '
footer = '\n*---This recipe search was powered by https://developer.edamam.com/edamam-recipe-api | Bot created by u/cconlan26 | [Source code](https://github.com/cconlan26/recipeBot)*'

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


    #TODO: DELETE
    r = requests.get("https://api.edamam.com/search?q=chicken&app_id=" + app_id + "&app_key=" + application_key)
    content = r.json()



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

            # TODO: better regex
            # Using regex to check if the body contains the phrase with a list of following ingredients
            if re.match("Find me a recipe with [a-zA-Z]+\s*(,\s*[a-zA-Z]+\s*)*", comment.body):

                # Need to tokenize the ingredients
                ingredients = comment.body.split("Find me a recipe with ")[1]
                ingredients = ingredients.split("\s*,\s*")

                # Converting the ingredients list into a readable format
                ingredientsList = ','.join(ingredients)

                # Now we need to use the edamam api to find recipes
                r = requests.get("https://api.edamam.com/search?q=" + ingredientsList + "&app_id=" + app_id + "&app_key=" + application_key)
                content = r.json()

                # If a result using the listed ingredients found
                if content["count"] > 0:
                    print("results found!")
                    hits = content["hits"]
                    # Getting the first result
                    firstRecipe = hits[0]["recipe"]
                    print(firstRecipe)
                    label = firstRecipe['label']
                    url = firstRecipe["url"]
                    body = "\n The recipe we have found is " + label + "."
                    body += "\n Link to recipe: " + url + "\n"
                    # Replying to comment
                    comment.reply(header + ingredientsList + "**\n" + body + footer)
                    # Adding the comment id to the list
                    commentIdHistory.append(comment.id)

    with open("commentIdHistory.txt", "w") as f:
        for post_id in commentIdHistory:
            f.write(post_id + "\n")
