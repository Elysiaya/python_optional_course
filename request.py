import requests
from lxml import etree
import re
import json
import os

bv = 'BV1m54y1b72h'
url = 'https://www.bilibili.com/video/' + bv
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 "
                  "Safari/537.36 Edg/89.0.774.76",
    "referer": "https://manga.bilibili.com/"
}


def download(url, path):
    r = requests.get(url, headers=headers)
    with open(path, 'wb') as f:
        f.write(r.content)
    return path


def video_add_mp3(video_path, audio_path):
    """
     视频添加音频
    :param video_path: 传入视频文件的路径
    :param audio_path: 传入音频文件的路径
    :return:
    """
    outfile_name = video_path.split('.')[0] + '.mp4'
    path = 'ffmpeg.exe' + ' -i ' + '\"' + video_path + '\"' + ' -i ' + '\"' + audio_path + '\"' + ' -codec copy ' + '\"' + outfile_name + '\"'
    os.system(path)
    if os.path.exists(outfile_name):
        os.remove(video_path)
        os.remove(audio_path)
        print('下载完成')
    else:
        print('视频合成失败')


if __name__ == '__main__':
    r = requests.get(url=url, headers=headers)

    html = etree.HTML(r.text)

    r = html.xpath('/html/head/script[5]/text()')[0]

    re_pattern = re.compile('{.+}')
    r_json = re.findall(pattern=re_pattern, string=r)[0]

    j = json.loads(r_json)

    data = j["data"]

    quality = data['quality']
    format = data['format']
    timelength = data['timelength']
    accept_format = data['accept_format']
    accept_description = data['accept_description']
    accept_quality = data['accept_quality']

    video = data['dash']['video'][0]['baseUrl']
    audio = data['dash']['audio'][0]['baseUrl']
    p1 = download(video, bv + '_video.m4s')
    p2 = download(audio, bv + '_audio.m4s')
    video_add_mp3(p1, p2)
