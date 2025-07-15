import praw
import json
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def fetch_user_data(username):
    user = reddit.redditor(username)
    posts, comments = [], []

    for submission in user.submissions.new(limit=100):
        posts.append({
            "title": submission.title,
            "body": submission.selftext,
            "subreddit": str(submission.subreddit),
            "url": submission.url
        })

    for comment in user.comments.new(limit=100):
        comments.append({
            "body": comment.body,
            "subreddit": str(comment.subreddit),
            "link": f"https://reddit.com{comment.permalink}"
        })

    return {
        "username": username,
        "posts": posts,
        "comments": comments
    }

def save_user_data(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
