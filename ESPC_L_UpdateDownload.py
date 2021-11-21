#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/31 02:30
# @Author     :mik1th0n
# @File       :ESPC-L_UpdateDownload.py


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
	****                          绿盟授权管理系统(ESPC-L) V7.0                           ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“绿盟授权管理系统(ESPC-L) V7.0”
	url = 'http://update.nsfocus.com/update/listEspcLDetail/v/V7.0R00F00'
	file_path = './UpdateThePackage/绿盟授权管理系统(ESPC-L) V7.0/'
	path_features = r'<a href="(.*)" \r\n >ES'
	filename_features = r'>ES(.*)</a>'
	filename_features_n = 'ES'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟授权管理系统(ESPC-L) V7.0”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 ESPC-L 升级包的更新  *********************************\n')

Update()