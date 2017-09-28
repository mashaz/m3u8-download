#coding: utf-8

# python3

import re
import requests
import os
import sys
import threadpool
from lxml import etree
from download_video import save_video

M3U8_XPATH = '//video/source/@src'


def m3u8_to_list():
    with open(M3U8_NAME) as f:
        lines = f.readlines()
    urls = [url.strip() for url in lines if url.startswith('http')]
    download_v(urls)

def download_m3u8(url):
    headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' } 
    proxies = {
            'http': 'socks5://127.0.0.1:1080',
            'https': 'socks5://127.0.0.1:1080'
            }   
    response = requests.get(url,headers=headers,proxies=proxies)
    f= open(url.split('=')[-1]+'.m3u8','w')
    f.write(response.content.decode())
    f.close()

def download_v(urls):
    os.environ['directory'] = M3U8_NAME.rstrip('m3u8')+'mp4'
    directory = os.environ['directory']
    if not os.path.isdir(directory):
        os.mkdir(directory)
    pool = threadpool.ThreadPool(4)
    t_requests = threadpool.makeRequests(save_video, urls)
    [pool.putRequest(req) for req in t_requests]
    pool.wait()
    os.system('rm {}'.format(M3U8_NAME))
    

    # os.system('cd {};ls | grep ts >> file.txt'.format(directory))
    # with open(os.path.join(directory, 'file.txt')) as f:
    #     files = f.readlines()
    # for fname in files:
    #     fname = fname.strip()
    #     fname_new = fname.split('-')[1]+'.ts'
    #     os.system('mv {} {}'.format(directory+'/'+fname, directory+'/'+fname_new))
        

    # os.system('cd {};'.format(directory))
    # ffmpeg = 'i=0;for filename in `ls`;do;let i=i+1;done;echo $i;for n in {1..$i};do;echo "file seg-$n-v1-a1.ts" >> file.txt;done;ffmpeg -f concat -i file.txt -c copy output.mp4;rm file.txt;rm *.ts;
    # os.system('cd {};ls;{}'.format(directory, ffmpeg))
    
    # for url in urls:
    #     save_video(url)


if __name__ == '__main__':

    url = sys.argv[1]
    #goto(url)
    download_m3u8(url)
    os.system('ls | grep m3u8 > name.txt')
    with open('name.txt') as f:
        M3U8_NAME = f.read().strip()
    m3u8_to_list()
        
    sentence = " osascript -e 'display notification \"lol\" with title \"Completed\"' "
    os.system(sentence)




    