#coding: utf-8

import requests
import time
import os 

def save_video(addr):
    error_time = 0
    while True:
        try:  
            save_video_core(addr)
            break
        except Exception as e:
            error_time += 1
            if error_time > 3:
                break
            print ('!!!failed :'+str(e), 'retry', error_time)


def save_video_core(addr):
    split_path = addr.split('/')
    filename = split_path.pop()
    directory = os.environ['directory']
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        return
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    print(filename,'start',now)
    headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   }    
    response = requests.get(addr,headers=headers)
    data = response.content
    
    # sentence = " osascript -e 'display notification \"lol\" with title \"Completed\"' "
    # os.system(sentence)
    f= open(file_path,'wb')
    f.write(data)
    f.close()
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    print(filename, 'saved', now, 'size: ', round(os.path.getsize(file_path)/1024/1024,2), 'M')
    


