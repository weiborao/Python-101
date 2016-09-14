# 将目录中MP4文件从youtube下载后带的文件名后缀修改一下

import os

for filename in os.listdir('.'):
    if filename.endswith('mp4'):
        os.rename(filename, filename[:-16] + filename[-4:])
    break
