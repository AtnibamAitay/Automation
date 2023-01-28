import json
import math
import requests

def batch_download_bilibili_favorites(mid: int):
    # TODO:将要被扫描下载下来的收藏夹，与指定目录下的所有视频相对比，若已存在，则跳过，不写入run.bat中
    # TODO:一个视频可能有多个分P，比如：https://api.bilibili.com/x/v3/fav/resource/list?media_id=2046075929&pn=1&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp
    # TODO:有15个分批，所以"page": 15,所以需要做个判断，包括分P中的视频也需要统计和下载下来

    # 使用mid参数访问bilibili API获取用户所有收藏夹信息
    url = f'https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid={mid}&jsonp=jsonp'
    res = requests.get(url)
    favorites = json.loads(res.text)
    total_media_count = 0
    video_page_sum = 0     # 一个视频可能存在多个分P，这个数据是包括分P在内的收藏夹总视频数
    flag = 1
    # 不下载的收藏夹
    skip_folders = []
    # 不下载的BV号夹
    skip_videos = ["BV1Dk4y1q781", "BV1Ts411X7PT", "BV1XY411J7aG", "BV1iV411z7Nj", "BV1Z4411C7jG", "BV1Eb4y1R7zd", "BV1Hx411S7zm"]
    # 遍历所有收藏夹，统计视频总数
    for item in favorites["data"]["list"]:
        total_media_count += item["media_count"]

    print("收藏夹中的视频总数为（包括已失效的视频）:", total_media_count)

    # 创建run.bat文件并写入默认内容
    with open('run.bat', 'w', encoding='utf-8') as f:
        f.write('@echo off\npip3 list | find "you-get"\nif errorlevel 1 (\necho you-get you-get not found, installing...\npip3 install you-get\n) else (\necho you-get already installed.\n)\n')

    # 遍历所有收藏夹
    for item in favorites['data']['list']:
        title = item['title']
        if title in skip_folders:
            print(f'收藏夹 "{item["title"]}" 在“不下载”列表中，已跳过。')
            continue
        # if flag != 1:
        #     print(f'收藏夹 "{item["title"]}" 共有 {video_pages} 个视频（这里统计的包括分P）')
        video_pages = 0
        media_count = item['media_count']
        k = math.ceil(media_count / 20)
        favorites_id = item['id']
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
                video_page = videos_item['page']
                if video_title == "已失效视频":
                    continue
                elif video_bvid in skip_videos:
                    print(f'          视频 "{video_bvid}" 在“不下载”列表中，已跳过。')
                    continue
                video_pages += videos_item['page']
                video_page_sum += videos_item['page']
                print(f'          {video_title} -> {video_bvid} -> {video_page}')
                with open('run.bat', 'a', encoding='utf-8') as f:
                    # 使用you-get下载视频
                    if video_page == 1:
                        f.write(f'you-get https://www.bilibili.com/video/{video_bvid}\n')
                    else:
                        f.write(f'mkdir {video_bvid}\n')
                        f.write(f'cd {video_bvid}\n')
                        # 如果一个视频中有多个分P，则全部下载下来
                        # for p in range(1, video_page+1):
                        #     f.write(f'you-get https://www.bilibili.com/video/{video_bvid}/?p={p}\n')
                        f.write(f'you-get --playlist https://www.bilibili.com/video/{video_bvid}\n')
                        f.write(f'cd..\n')
        print(f'收藏夹 "{item["title"]}" 共有 {video_pages} 个视频（这里统计的包括分P）')

    print("收藏夹中的视频总数为（包括已失效的视频和所有分P）:", video_page_sum)

batch_download_bilibili_favorites(B站用户ID)