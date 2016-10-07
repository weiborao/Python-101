# -*- coding: utf-8 -*-
# 下载的文件文件名经常是"%9C%9F%EF%BC%89"
# 下面的代码将文件名进行转码恢复

import urllib.request

url = input("Please paste the URL,or just type 'Quit':")
while url != "Quit":
    decoded_url = urllib.request.url2pathname(url)
    print("The decoded URL is : %s" % decoded_url)
    url = input("Please paste the URL,or just type 'Quit':")
