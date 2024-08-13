import asyncio

import requests
from pprint import pprint


async def instagram_requester(https_url: str):
    url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/get-info-rapidapi"

    querystring = {"url": f"{https_url}"}

    headers = {
        "x-rapidapi-key": "b7b963b1c6mshdf4b4e9eb8bce98p1d260bjsnd1174d8514f7",
        "x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    medias = response.json().get('medias')
    photo_urls: list[str] = []
    video_urls: list[str] = []
    if medias:
        for media in medias:
            if media.get('type') == 'image':
                photo_urls.append(media.get('download_url'))
            else:
                video_urls.append(media.get('download_url'))
    else:
        if response.json().get('type') == 'image':
            photo_urls.append(response.json().get('download_url'))
        else:
            video_urls.append(response.json().get('download_url'))
    return photo_urls, video_urls, response.json().get('caption')


async def tiktok_requester(https_url: str):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/index"

    querystring = {"url": https_url}

    headers = {
        "x-rapidapi-key": "b7b963b1c6mshdf4b4e9eb8bce98p1d260bjsnd1174d8514f7",
        "x-rapidapi-host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data.get('video')[0], data.get('music')[0], data.get('description')[0]


def youtube_requester(https_url: str):
    url = "https://fb-video-reels.p.rapidapi.com/smvd/get/all"

    querystring = {"url": "https://youtu.be/JsC5XWMEkII?feature=shared"}

    headers = {
        "x-rapidapi-key": "b7b963b1c6mshdf4b4e9eb8bce98p1d260bjsnd1174d8514f7",
        "x-rapidapi-host": "fb-video-reels.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    pprint(response.json())

