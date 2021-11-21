#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/11/02 22:12
# @Author     :mik1th0n
# @File       :OSMS_SASH_UpdateDownload.py


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
	****                      运维安全管理系统堡垒机系列(OSMS/SAS-H)                        ****
	****                                                                                 ****
	*****************************************************************************************
	'''

	# 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包V5.6R10F04”
	url = 'https://update.nsfocus.com/update/listSashDetail/v/V5.6R10F04'
	file_path = './UpdateThePackage/运维安全管理系统堡垒机系列(OSMS_SASH)/运维安全管理系统（堡垒机）系列(OSMS_SASH)/引擎升级包V5.6R10F04/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包V5.6R10F04”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包V5.6R10F03”
	url = 'https://update.nsfocus.com/update/listSashDetail/v/V5.6R10F03'
	file_path = './UpdateThePackage/运维安全管理系统堡垒机系列(OSMS_SASH)/运维安全管理系统（堡垒机）系列(OSMS_SASH)/引擎升级包V5.6R10F03/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包V5.6R10F03”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包V5.6R10F02”
	url = 'https://update.nsfocus.com/update/listSashDetail/v/V5.6R10F02'
	file_path = './UpdateThePackage/运维安全管理系统堡垒机系列(OSMS_SASH)/运维安全管理系统（堡垒机）系列(OSMS_SASH)/引擎升级包V5.6R10F02/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包V5.6R10F02”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包V5.6R10F01”
	url = 'https://update.nsfocus.com/update/listSashDetail/v/V5.6R10F01'
	file_path = './UpdateThePackage/运维安全管理系统堡垒机系列(OSMS_SASH)/运维安全管理系统（堡垒机）系列(OSMS_SASH)/引擎升级包V5.6R10F01/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包V5.6R10F01”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包 5.6.10”
	url = 'https://update.nsfocus.com/update/listSashDetail/v/engine5.6.10'
	file_path = './UpdateThePackage/运维安全管理系统堡垒机系列(OSMS_SASH)/运维安全管理系统（堡垒机）系列(OSMS_SASH)/引擎升级包 5.6.10/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->运维安全管理系统（堡垒机）系列(OSMS_SASH)->引擎升级包 5.6.10”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                              信息技术应用创新-堡垒机                              ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->信息技术应用创新-堡垒机->兆芯系列(X86_64-ZX)->引擎升级包V5.6R10F01”
	url = 'https://update.nsfocus.com/update/listSashDetail/v/V5.6R10F01.x86_64-zx'
	file_path = './UpdateThePackage/运维安全管理系统堡垒机系列(OSMS_SASH)/信息技术应用创新-堡垒机/兆芯系列(X86_64-ZX)/引擎升级包V5.6R10F01/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->信息技术应用创新-堡垒机->兆芯系列(X86_64-ZX)->引擎升级包V5.6R10F01”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->信息技术应用创新-堡垒机->飞腾系列(ARM64-FT)->引擎升级包V5.6R10F01”
	url = 'https://update.nsfocus.com/update/listSashDetail/v/V5.6R10F01.arm64-ft'
	file_path = './UpdateThePackage/运维安全管理系统堡垒机系列(OSMS_SASH)/信息技术应用创新-堡垒机/飞腾系列(ARM64-FT)/引擎升级包V5.6R10F01/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“运维安全管理系统堡垒机系列(OSMS_SASH)->信息技术应用创新-堡垒机->飞腾系列(ARM64-FT)->引擎升级包V5.6R10F01”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 OSMS/SAS-H 升级包的更新  *********************************\n')

#Update()