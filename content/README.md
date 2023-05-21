# Content Scraping

## **Reddit**
We used Praw and the Reddit API in order to scrap subreddits for the text stories.

### blacklist_links.txt
Similar to the video scraper, we use a blacklist to ensure that no Reddit story is used twice. If you wish to reuse reddit stories, comment out line 27 in reddit.py.

### subreddit.txt
You can include any subreddit in this txt file and one will be randomly chosen to scrape content from. Be wary though, our current code doesn't handle other subreddits well due to the length restrictions we are placing on the posts.

## **ChatGPT**
We used the OpenAI API in order to prompt ChatGPT with the users prompt. 

Currently, we provide 500 tokens to chatGPT, which means it can use up to 500 tokens to produce the content. 

One token generally corresponds to ~4 characters of text for common English text. This translates to roughly ¾ of a word (so 100 tokens ~= 75 words). 
