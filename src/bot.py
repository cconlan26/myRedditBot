import praw
import pdb
import re
import os


def reply():

    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit("pythonforengineers")

    if not os.path.isfile("postIdHistory.txt"):
        postIdHistory = []
    else:
        with open("postIdHistory.txt") as f:
            postIdHistory = f.read()
            postIdHistory = postIdHistory.split("\n")
            postIdHistory = list(filter(None, postIdHistory))

    for submission in subreddit.hot(limit=5):
        if submission.id not in posts_replied_to:
            if re.search("testing bot replying", submission.title, re.IGNORECASE):
                submission.reply("replying to this")
                print("Bot replying to: " + submission.title)
                postIdHistory.append(submission.id)

        with open("postIdHistory.txt", "w") as f:
            for post_id in postIdHistory:
                f.write(post_id + "\n")
