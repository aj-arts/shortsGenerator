# **Shorts Generator**

This tool will automatically generate short form content in the form of text-based stories spoken over stimulating background videos.

https://github.com/aj-arts/shortsGenerator/assets/19521833/2c63d41a-96c5-4408-ae4f-09630034793f

## Installation Instructions

```
git clone https://github.com/aj-arts/shortsGenerator.git
```
```
cd shortsGenerator
```
### Create a virtual environment
```
python3 -m venv venv
```
### Activate venv and install dependencies
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

### **IMPORTANT** 
### To use captions on videos with MoviePy, you **MUST** download a program called ImageMagick

You can find the download links for Linux, Mac, and Windows [here](https://www.imagemagick.org/script/download.php)

---

### In order for the generator to scrape Reddit stories or use ChatGPT you **MUST** create a .env file with
```
OPENAI_API_KEY = "[your openAI api key]"
REDDIT_CLIENT_ID = "[your reddit client_ID]"
REDDIT_CLIENT_SECRET = "[your reddit client_secret]"
REDDIT_USER_AGENT = "[your reddit user_age]"
```
*Without this you cannot access the Reddit or OpenAI API!*

---

## Usage


To use the tool run the command

```
python generator.py
```


### **BE SPECIFIC WHEN PROMPTED FOR VIDEO BACKGROUND**

For example:

    subway surfer background gameplay for tiktok

OR

    short nature background video relaxing

## **WHEN USING CHATGPT**
### With your prompt to chatGPT make sure to include a word limit, it may also help to be specific. We recommend not to go over 750 words. Using over 500 will most likely require you to increase the number of tokens in the generate_req() function on line 28 in generator.py.

See the [README](content/README.md) in content for more information.

**Examples**
```
generate a random AITA reddit story with a word limit of 150
```
```
generate an AskReddit thread with responses no longer than 200 words
```
```
generate a cute story about someone getting into a car crash and falling in love that is under 300 words
```

---
## Additional Notes

You may come across an error such as 

```
Unexpected renderer encountered.
Renderer name: dict_keys(['reelShelfRenderer'])
Search term: tetris
Please open an issue at https://github.com/pytube/pytube/issues and provide this log output.
```

This is an issue with pytube and hopefully will be resolved soon. It does not impact the performance or outcome of the video, but if you wish to mute the issue temporarily navigate to 
```
venv/lib/python3.X/site-packages/pytube/contrib/search.py
```
and after line 150 add

```python
if 'reelShelfRenderer' in video_details:
    continue
            
if 'showingResultsForRenderer' in video_details:
    continue
```
We use a graveyard in order to prevent reuse of Reddit posts and YouTube videos. See the [content README](content/README.md) and [video README](video/README.md) for more information.

---

## Future improvements

- [ ] Work towards integration with uploading to multiple media platforms - Youtube, Tiktok, Instagram
- [ ] Provide more customizability for video options
- [ ] Improve TTS engine to be more realistic

---

## Written by:
Sarvesh Thiruppathi - text scraping

Ajinkya Gokule - video processing and captioning

David Gesl - text to speech

Colin Pannikkat - video scraping, documentation

---
Copyright (c) 2023 Colin Pannikkat, Ajinkya Gokule, Sarvesh Thiruppathi, David Gesl
