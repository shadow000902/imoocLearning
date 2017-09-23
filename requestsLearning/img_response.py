# -*- coding: utf-8 -*-

import requests

def download_image():
	# 下载图片，文件
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
	url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1505504352622&di=afec52ad1c83e0c1204c1a0157fc346b&imgtype=0&src=http%3A%2F%2Ff.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F472309f79052982247b0f3b8ddca7bcb0b46d4ce.jpg"
	response = requests.get(url, headers=headers, stream=True)
	with open('demo.jpg', 'wb') as fd:
		for chunk in response.iter_content(128):
			fd.write(chunk)

def download_image_improves():
	# 下载图片
	url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1505504352622&di=afec52ad1c83e0c1204c1a0157fc346b&imgtype=0&src=http%3A%2F%2Ff.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F472309f79052982247b0f3b8ddca7bcb0b46d4ce.jpg"
	response = requests.get(url, stream=True)
	from contextlib import closing
	with closing(requests.get(url, stream=True)) as response:
		with open('demo.jpg', 'wb') as fd:
			# 每128写入一次
			for chunk in response.iter_content(128):
				fd.write(chunk)

download_image_improves()
