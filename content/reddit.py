import praw
import os
import random
from contextlib import closing

def main():
  #Create reddit instance
  reddit = praw.Reddit(
  client_id=os.environ["REDDIT_CLIENT_ID"], 
  client_secret=os.environ["REDDIT_CLIENT_SECRET"], 
  user_agent=os.environ["REDDIT_USER_AGENT"],)

  #Get a list of subreddit and choose a random subreddit
  subs = read_subreddit_file("./reddit/subreddit.txt")
  sub_name = subs[random.randint(0,len(subs)-1)]

  #Get top posts
  top_posts = reddit.subreddit(sub_name).top(limit=1000,time_filter="month")

  print("Searching for post in r/" + sub_name + "...")
  #Search for SFW post with content <1 words which hasn't been generated before
  for post in top_posts:
    if (len(post.selftext.split()) <= 1 and post.over_18  == False and not(search_string_in_file("./reddit/blacklist_links.txt",post.permalink))):
      print("Found post: " + post.title)
      add_string_to_file("./reddit/blacklist_links.txt",post.permalink)

      content = post.title + "\n"

      length = len(post.selftext.split())

      comments = post.comments

      #Keeps adding comments as 
      for comment in comments:
        if not isinstance(comment, praw.models.MoreComments):
          if (length <= 130):
            if (len(comment.body.split()) <= 35 and comment.body != "[deleted]" and comment.body != "[removed]"):
              length += len(comment.body.split())
              if(length <= 130):
                content += "\n\n" + comment.body
                
      return content

#Function to add a string to a file
def add_string_to_file(filename, content):
    with closing(open(filename, 'a')) as file:
        file.write(content)
        file.write('\n')

#Function to search for a string in a file - returns true if found
def search_string_in_file(filename, search_string):
    with closing(open(filename, 'r')) as file:
        for line in file:
            if search_string in line:
                return True
    return False

#Converts lines in a file to an array
def read_subreddit_file(filename):
    with open(filename, 'r') as file:
        # Read the lines of the file and store them in an array
        subs = file.readlines()

    # Remove the trailing newline character from each line
    subs = [line.rstrip('\n') for line in subs]

    return subs 


if __name__ == '__main__':
    # Call the main function
    main()