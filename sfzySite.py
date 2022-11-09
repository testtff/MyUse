import datetime
from pytz import timezone
import requests
import re
from google_drive_downloader import GoogleDriveDownloader as gdd

headers = {
    'referer': 'https://www.sfzy888.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.93 Safari/537.36 '

}

def get_new_article(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    urls = re.findall(r"<a class='read-more anchor-hover' href='(.*)'>Read More<\/a>", response.text)
    print(urls)
    return urls


def get_gdid(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    print("shh--->0")
    ids = re.findall(r'<a href="https://drive.google.com/(.*)" target="_blank">', resp.text)
    print(ids)
    node_url = ids[0].split('=')[2].split('"')[0]
    print(node_url)
    return node_url


if __name__ == '__main__':
    # https://www.sfzy888.com/search/label/免费节点
    url = 'https://www.sfzy888.com/search/label/%E5%85%8D%E8%B4%B9%E8%8A%82%E7%82%B9'
    urls = get_new_article(url)
    ids = get_gdid(urls[0])
    if ids:
        gdd.download_file_from_google_drive(file_id=ids,
                                            dest_path='./WebSite/{}.yaml'.format(datetime.datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')),
                                            showsize=True, overwrite=True)

        gdd.download_file_from_google_drive(file_id=ids,dest_path='./newYaml/newestWB.yaml',showsize=True, overwrite=True)
        print("网站爬取成功")
        # requests.get('https://api.day.app/3TKmw24emfnWtLN6xyDaW9/网站爬取成功{}'.format(
        #     datetime.datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')))
    else:
        print("网站爬取失败")
        # requests.get('https://api.day.app/3TKmw24emfnWtLN6xyDaW9/网站爬取失败'.format(
        #     datetime.datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')))
