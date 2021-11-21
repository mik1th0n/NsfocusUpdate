#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/11/15 12:18
# @Author     :mik1th0n
# @File       :WSM_UpdateDownload.py


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
	****                              网站安全监测系统(WSM)                               ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“网站安全监测系统(WSM)->系统升级包 V5”
	url = 'https://update.nsfocus.com/update/listWsmsDetail/v/5/t/sys'
	file_path = './UpdateThePackage/网站安全监测系统(WSM)/系统升级包 V5/'
	path_features = r'<a href="(.*)" \r\n >wsms-'
	filename_features = r'wsms-(.*)</a>'
	filename_features_n = 'wsms-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网站安全监测系统(WSM)->系统升级包 V5”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“网站安全监测系统(WSM)->插件升级包 V5”
	url = 'https://update.nsfocus.com/update/listWsmsDetail/v/5/t/plg'
	file_path = './UpdateThePackage/网站安全监测系统(WSM)/插件升级包 V5/'
	path_features = r'<a href="(.*)" \r\n >wsms-'
	filename_features = r'wsms-(.*)</a>'
	filename_features_n = 'wsms-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网站安全监测系统(WSM)->插件升级包 V5”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“网站安全监测系统(WSM)->系统升级包 V6”
	url = 'https://update.nsfocus.com/update/listWsmsDetail/v/6/t/sys'
	file_path = './UpdateThePackage/网站安全监测系统(WSM)/系统升级包 V6/'
	path_features = r'<a href="(.*)" \r\n >wsms-'
	filename_features = r'wsms-(.*)</a>'
	filename_features_n = 'wsms-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网站安全监测系统(WSM)->系统升级包 V6”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“网站安全监测系统(WSM)->插件升级包 V6”
	url = 'https://update.nsfocus.com/update/listWsmsDetail/v/6/t/plg'
	file_path = './UpdateThePackage/网站安全监测系统(WSM)/插件升级包 V6/'
	path_features = r'<a href="(.*)" \r\n >wsms-'
	filename_features = r'wsms-(.*)</a>'
	filename_features_n = 'wsms-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网站安全监测系统(WSM)->插件升级包 V6”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

#Update()