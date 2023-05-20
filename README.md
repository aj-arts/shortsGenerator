# **Shorts Generator**

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

## Usage

You may come across an error such as 

```
Unexpected renderer encountered.
Renderer name: dict_keys(['reelShelfRenderer'])
Search term: ur mom
Please open an issue at https://github.com/pytube/pytube/issues and provide this log output.
```

This is an issue with pytube and hopefully will be resolved soon. If you wish to mute the issue temporarily go into your python packages and navigate to 
'pytube/contrib/search.py' and add after line 150

```
if 'reelShelfRenderer' in video_details:
    continue
            
if 'showingResultsForRenderer' in video_details:
    continue
```

To use the tool run the command

```
python UR_MOM.py
```

<br>

**BE SPECIFIC WHEN PROMPTED FOR VIDEO BACKGROUND**

For example:

    subway surfer background gameplay for tiktok

OR

    short nature background video relaxing

## Future improvements

* Work towards integration with multiple media platforms
* Provide more customizability

---

### Written by:
Sarvesh Thiruppathi - text scraping

Ajinkya Gokule - video processing and text

David Gesl - text to speech

Colin Pannikkat - video scraping

