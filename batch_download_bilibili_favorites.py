import json
import math
import requests

def batch_download_bilibili_favorites(mid: int):
    # TODO:将要被扫描下载下来的收藏夹，与指定目录下的所有视频相对比，若已存在，则跳过，不写入run.bat中


    # 使用mid参数访问bilibili API获取用户所有收藏夹信息
    url = f'https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid={mid}&jsonp=jsonp'
    res = requests.get(url)
    favorites = json.loads(res.text)
    total_media_count = 0
    flag = 1
    # 遍历所有收藏夹，统计视频总数
    for item in favorites["data"]["list"]:
        total_media_count += item["media_count"]

    print("收藏夹中的视频总数为（包括已失效的视频）:", total_media_count)

    # 创建run.bat文件并写入默认内容
    with open('run.bat', 'w', encoding='utf-8') as f:
        f.write('@echo off\npip3 list | find "you-get"\nif errorlevel 1 (\necho you-get you-get not found, installing...\npip3 install you-get\n) else (\necho you-get already installed.\n)\n')

    # 遍历所有收藏夹
    for item in favorites['data']['list']:
        media_count = item['media_count']
        k = math.ceil(media_count / 20)
        favorites_id = item['id']
        title = item['title']
        print(f'收藏夹 "{item["title"]}" 共有 {media_count} 个视频')
        with open('run.bat', 'a', encoding='utf-8') as f:
            # 若flag不为1，说明不是第一次循环，则需要先返回上一层文件夹
            if flag != 1:
                f.write(f'cd..\n')
            # 创建新文件夹
            f.write(f'mkdir {title}\n')
            f.write(f'cd {title}\n')
            flag = flag + 1
        # 遍历当前收藏夹中的所有视频
        for i in range(1, k + 1):
            # 获取当前收藏夹第i页的视频列表
            favorites_videos_url = f'https://api.bilibili.com/x/v3/fav/resource/list?media_id={favorites_id}&pn={i}&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp'
            res = requests.get(favorites_videos_url)
            videos_list = json.loads(res.text)
            # 遍历当前页的所有视频
            for videos_item in videos_list['data']['medias']:
                # 获取视频的标题和bvid
                video_title = videos_item['title']
                video_bvid = videos_item['bvid']
                print(f'          {video_title} -> {video_bvid}')
                with open('run.bat', 'a', encoding='utf-8') as f:
                    # 使用you-get下载视频
                    f.write(f'you-get https://www.bilibili.com/video/{video_bvid}\n')

batch_download_bilibili_favorites(b站的用户ID)