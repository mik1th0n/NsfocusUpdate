#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/30 22:30
# @Author     :mik1th0n
# @File       :UpdateGeneralDownload.py

import requests
import re
import os
import time
import _thread

def down_thread_file(url_file,headers,file_path,filename_features_n,file_name,j):
	r = requests.get(url_file,headers=headers,stream=True)
	f = open(file_path + filename_features_n + str(file_name[j]),"wb")
	for chunk in r.iter_content(chunk_size=512):
	    if chunk:
	        f.write(chunk)	
	f.close()	


def down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n):
	r = requests.get(url=url,headers=headers)

	# print(r.text)

	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 获取系统/引擎升级包路径信息如下')
	uri_name = re.findall(path_features,r.text)
	print(uri_name)
	# for i in uri_name:
	# 	print(str(i)+ '\n')

	file_name = re.findall(filename_features,r.text)

	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 获取系统/引擎升级包名称信息如下')
	print(file_name)
	# for i in file_name:
	# 	print(str(i)+ '\n')
	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 获取系统/引擎升级包名称信息完成')

	url_file = 'null'
	j=0
	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 开始下载系统/引擎升级包')
	for i in uri_name:
		url_file = 'http://update.nsfocus.com' + str(i)
		if(0 == os.path.isfile(file_path + filename_features_n + str(file_name[j]))):
			print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载系统/引擎升级包：' + filename_features_n + str(file_name[j]))
			print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载系统/引擎升级包URL：' + url_file)
			# r = requests.get(url_file,headers=headers,stream=True)
			# f = open(file_path + filename_features_n + str(file_name[j]),"wb")
			# for chunk in r.iter_content(chunk_size=512):
			#     if chunk:
			#         f.write(chunk)	
			# f.close()	
			down_thread_file(url_file,headers,file_path,filename_features_n,file_name,j)
			# try:
			#    _thread.start_new_thread(down_thread_file(url_file,headers,file_path,filename_features_n,file_name,j), ("Thread-1", 50, ) )
			# except:
			#    print ("Error: 无法启动线程")
		j = j+1
		if(j == 150):
			print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 已下载150个升级包')
			break
	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 系统/引擎升级包下载完成')




def down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n):
	r = requests.get(url=url,headers=headers)

	# print(r.text)

	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 获取规则升级包路径信息如下')
	uri_name = re.findall(path_features,r.text)

	try:
		print(uri_name[0])
	except IndexError:
		print('当前页面无升级包')
		pass

	# for i in uri_name:
	# 	print(str(i)+ '\n')

	file_name = re.findall(filename_features,r.text)

	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 获取规则升级包名称信息如下')
	
	try:
		print(file_name[0])
	except IndexError:
		print('当前页面无升级包')
		pass
	
	# for i in file_name:
	# 	print(str(i)+ '\n')
	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 获取规则升级包名称信息完成')

	url_file = 'null'
	j=0

	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 当前目录下规则升级包')
	cur_file_name = str(os.listdir(file_path))[2:-2]

	try:
		print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 当前目录下规则升级包：' + cur_file_name)
		print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 站点最新规则升级包：' + str(filename_features_n + str(file_name[j])))
	except IndexError:
		print('当前页面无升级包')
		pass

	try:
		url_file = 'http://update.nsfocus.com' + str(uri_name[j])
	except IndexError:
		print('当前页面无升级包')
		pass
	if(len(file_name) != 0):
		if(cur_file_name != str(filename_features_n + str(file_name[j]))):

			try:
				print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 删除目录下的规则包')
				for x in os.listdir(file_path):
					os.remove(os.path.join(file_path, x))
			except OSError:
				pass

			print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载最新规则升级包：' + filename_features_n + str(file_name[j]))
			print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载规则升级包URL：' + url_file)
			# r = requests.get(url_file,headers=headers,stream=True)
			# f = open(file_path + filename_features_n + str(file_name[j]),"wb")
			# for chunk in r.iter_content(chunk_size=512):
			#     if chunk:
			#         f.write(chunk)	
			# f.close()		
			down_thread_file(url_file,headers,file_path,filename_features_n,file_name,j)
			# try:
			#    _thread.start_new_thread(down_thread_file(url_file,headers,file_path,filename_features_n,file_name,j), ("Thread-1", 10, ) )
			# except:
			#    print ("Error: 无法启动线程")

	print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 规则升级包下载完成')

