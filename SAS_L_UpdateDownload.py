#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/11/02 21:53
# @Author     :mik1th0n
# @File       :SAS_L_UpdateDownload.py


import requests
import re
import time
import UpdateGeneralDownload

headers = {
		'Host':'update.nsfocus.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding':'gzip, deflate',
		'Connection':'close',
		'Cookie':'PHPSESSID=rkucspnln3hasov01kelth75u2',
		'Upgrade-Insecure-Requests': '1',
}


def Update():
	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                           安全审计系统-日志审计(SAS-L)                           ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“安全审计系统-日志审计(SAS-L)->5.6.1”
	url = 'https://update.nsfocus.com/update/listSasLDetail/v/v5update'
	file_path = './UpdateThePackage/安全审计系统-日志审计(SAS-L)/5.6.1/'
	path_features = r'<a href="(.*)" \r\n >SAS'
	filename_features = r'>SAS(.*)</a>'
	filename_features_n = 'SAS'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统-日志审计(SAS-L)->5.6.1”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 SAS-L 升级包的更新  *********************************\n')

Update()