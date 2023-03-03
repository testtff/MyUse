import datetime
#from pytz import timezone
import requests
from google_drive_downloader import GoogleDriveDownloader as gdd
from lxml import etree
import os
import time

headers = {
    'referer': 'https://nodefree.org/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'

}

def get_new_urls(url):
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    urls = html.xpath('//h2[@class = "item-title"]/a/@href')
    #print("new_urls is : "+urls[0])
    return urls[0]

def get_ggid(url):
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    latest_nodeUrl = html.xpath('//div[@class = "entry-content"]//div[@class = "section"]/p[2]/text()')
    return latest_nodeUrl[0]

def downLoadNode(url):
    print(url)
    f = requests.get(url)
    with open("./newYaml/nodefree.yaml", "wb") as code:
        code.write(f.content)

if __name__ == '__main__':
    if (os.path.isfile("./newYaml/nodefree.yaml")):
        print("nodefree.yaml exist,remove it begin")
        os.remove("./newYaml/nodefree.yaml")
        time.sleep(5)
        print("nodefree.yaml exist,remove it end")
    url = "https://nodefree.org/f/freenode"
    node_Urls = get_new_urls(url)
    latest_nodeUrl = get_ggid(node_Urls)
    downLoadNode(latest_nodeUrl)
    #if googleDrive_ids:
    #  gdd.download_file_from_google_drive(file_id=googleDrive_ids,
    #                             dest_path='./newYaml/nodefree.yaml',showsize=True, overwrite=True)
    #else:
    #  print("YouTube节点爬取失败")
