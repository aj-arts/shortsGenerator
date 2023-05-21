# **Shorts Generator**

This tool will automatically generate short form content in the form of text-based stories spoken over stimulating background videos.

[Example](https://www.tiktok.com/@reddit.said/video/7235313598632054062)

## Installation Instructions

```
git clone https://github.com/aj-arts/shortsGenerator.git
```
```
cd shortsGenerator
```
```
pip install -r requirements.txt
```

### To use captions on videos with MoviePy, you **must** download a program called ImageMagick

You can find the download links for Linux, Mac, and Windows [here](https://www.imagemagick.org/script/download.php)

---

## Usage


To use the tool run the command

```
python generator.py
```


**BE SPECIFIC WHEN PROMPTED FOR VIDEO BACKGROUND**

For example:

    subway surfer background gameplay for tiktok

OR

    short nature background video relaxing

---

You may come across an error such as 

```
Unexpected renderer encountered.
Renderer name: dict_keys(['reelShelfRenderer'])
Search term: tetris
Please open an issue at https://github.com/pytube/pytube/issues and provide this log output.
```

This is an issue with pytube and hopefully will be resolved soon. If you wish to mute the issue temporarily go into your python packages and navigate to 
'pytube/contrib/search.py' and after line 150 add

```
if 'reelShelfRenderer' in video_details:
    continue
            
if 'showingResultsForRenderer' in video_details:
    continue
```

---

## Future improvements

- [ ] Prevent words from Reddit stories from splitting in captions - better text timing
- [ ] Work towards integration with multiple media platforms
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
