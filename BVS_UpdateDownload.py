#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/11/15 12:06
# @Author     :mik1th0n
# @File       :BVS_UpdateDownload.py


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
	****                              安全配置核查系统(BVS)                               ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)6.0->BVS V6.0系统升级包”
	url = 'https://update.nsfocus.com/update/listBvsV6/v/bvssys'
	file_path = './UpdateThePackage/安全配置核查系统(BVS)/安全配置核查系统(BVS)6.0/BVS V6.0系统升级包/'
	path_features = r'<a href="(.*)" \r\n >bvs-'
	filename_features = r'bvs-(.*)</a>'
	filename_features_n = 'bvs-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)6.0->BVS V6.0系统升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)6.0->BVS V6.0合集升级包”
	url = 'https://update.nsfocus.com/update/listBvsV6/v/bvsfull'
	file_path = './UpdateThePackage/安全配置核查系统(BVS)/安全配置核查系统(BVS)6.0/BVS V6.0合集升级包/'
	path_features = r'<a href="(.*)" \r\n >bvs-'
	filename_features = r'bvs-(.*)</a>'
	filename_features_n = 'bvs-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)6.0->BVS V6.0合集升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)6.0->BVS 特殊升级包”
	url = 'https://update.nsfocus.com/update/listBvsV6/v/6.0'
	file_path = './UpdateThePackage/安全配置核查系统(BVS)/安全配置核查系统(BVS)6.0/BVS 特殊升级包/'
	path_features = r'<a href="(.*)" \r\n >bvs-'
	filename_features = r'bvs-(.*)</a>'
	filename_features_n = 'bvs-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)6.0->BVS 特殊升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)
	
	# 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)6.0->BVS V6.0配置核查模板包”
	url = 'https://update.nsfocus.com/update/listTvmDetail/v/vulnerability'
	file_path = './UpdateThePackage/安全配置核查系统(BVS)/安全配置核查系统(BVS)6.0/BVS V6.0配置核查模板包/'
	path_features = r'<a href="(.*)" \r\n >bvs-'
	filename_features = r'bvs-(.*)</a>'
	filename_features_n = 'bvs-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)6.0->BVS V6.0配置核查模板包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)5.0”
	url = 'https://update.nsfocus.com/update/listBvs/v/5'
	file_path = './UpdateThePackage/安全配置核查系统(BVS)/安全配置核查系统(BVS)5.0/'
	path_features = r'<a href="(.*)" \r\n >bvs-'
	filename_features = r'bvs-(.*)</a>'
	filename_features_n = 'bvs-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全配置核查系统(BVS)->安全配置核查系统(BVS)5.0”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

#Update()