#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/31 02:55
# @Author     :mik1th0n
# @File       :CSSP_UpdateDownload.py


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
	****                     绿盟网络空间安全仿真平台-竞技靶场(CSSP-C)                      ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“绿盟网络空间安全仿真平台(CSSP)->绿盟网络空间安全仿真平台-竞技靶场(CSSP-C)->V5.0R00F00”
	url = 'http://update.nsfocus.com/update/cssptdetail/v/V5.0R00F00'
	file_path = './UpdateThePackage/绿盟网络空间安全仿真平台(CSSP)/绿盟网络空间安全仿真平台-竞技靶场(CSSP-C)/V5.0R00F00/'
	path_features = r'<a href="(.*)" \r\n >CSS'
	filename_features = r'>CSS(.*)</a>'
	filename_features_n = 'CSS'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟网络空间安全仿真平台(CSSP)->绿盟网络空间安全仿真平台-竞技靶场(CSSP-C)->V5.0R00F00”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟网络空间安全仿真平台(CSSP)->绿盟网络空间安全仿真平台-竞技靶场(CSSP-C)->中台升级包”
	url = 'http://update.nsfocus.com/update/csspdetail/v/core'
	file_path = './UpdateThePackage/绿盟网络空间安全仿真平台(CSSP)/绿盟网络空间安全仿真平台-竞技靶场(CSSP-C)/中台升级包/'
	path_features = r'<a href="(.*)" \r\n >CSS'
	filename_features = r'>CSS(.*)</a>'
	filename_features_n = 'CSS'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟网络空间安全仿真平台(CSSP)->绿盟网络空间安全仿真平台-竞技靶场(CSSP-C)->中台升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                     绿盟网络空间安全仿真平台-实训靶场(CSSP-T)                      ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“绿盟网络空间安全仿真平台(CSSP)->绿盟网络空间安全仿真平台-实训靶场(CSSP-T)->V5.0R00F00”
	url = 'http://update.nsfocus.com/update/cssptdetail/v/V5.0R00F00'
	file_path = './UpdateThePackage/绿盟网络空间安全仿真平台(CSSP)/绿盟网络空间安全仿真平台-实训靶场(CSSP-T)/V5.0R00F00/'
	path_features = r'<a href="(.*)" \r\n >CSS'
	filename_features = r'>CSS(.*)</a>'
	filename_features_n = 'CSS'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟网络空间安全仿真平台(CSSP)->绿盟网络空间安全仿真平台-实训靶场(CSSP-T)->V5.0R00F00”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟网络空间安全仿真平台(CSSP)->绿盟网络空间安全仿真平台-实训靶场(CSSP-T)->中台升级包”
	url = 'http://update.nsfocus.com/update/csspdetail/v/core'
	file_path = './UpdateThePackage/绿盟网络空间安全仿真平台(CSSP)/绿盟网络空间安全仿真平台-实训靶场(CSSP-T)/中台升级包/'
	path_features = r'<a href="(.*)" \r\n >CSS'
	filename_features = r'>CSS(.*)</a>'
	filename_features_n = 'CSS'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟网络空间安全仿真平台(CSSP)->绿盟网络空间安全仿真平台-实训靶场(CSSP-T)->中台升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 CSSP-C/CSSP-T 升级包的更新  *********************************\n')

Update()