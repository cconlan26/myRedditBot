import praw
import pdb
import re
import os


def reply():

    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit("pythonforengineers")

    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))

    for submission in subreddit.hot(limit=5):
        if submission.id not in posts_replied_to:
            if re.search("testing bot replying", submission.title, re.IGNORECASE):
                submission.reply("replying to this")
                print("Bot replying to: " + submission.title)
                posts_replied_to.append(submission.id)

        with open("posts_replied_to.txt", "w") as f:
            for post_id in posts_replied_to:
                f.write(post_id + "\n")
