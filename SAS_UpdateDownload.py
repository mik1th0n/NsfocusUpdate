#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/31 02:38
# @Author     :mik1th0n
# @File       :ESP_UpdateDownload.py


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
	****                                安全审计系统(SAS)                                 ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“安全审计系统(SAS)->安全审计系统(SAS)->引擎升级包 5.6.10”
	url = 'https://update.nsfocus.com/update/listSasDetail/v/engine5.6.10'
	file_path = './UpdateThePackage/安全审计系统(SAS)/安全审计系统(SAS)/引擎升级包 5.6.10/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“全审计系统(SAS)->安全审计系统(SAS)->引擎升级包 5.6.10”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->安全审计系统(SAS)->引擎升级包 5.6.8”
	url = 'https://update.nsfocus.com/update/listSasDetail/v/engine5.6.8'
	file_path = './UpdateThePackage/安全审计系统(SAS)/安全审计系统(SAS)/引擎升级包 5.6.8/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“全审计系统(SAS)->安全审计系统(SAS)->引擎升级包 5.6.8”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->安全审计系统(SAS)->引擎升级包 5.6.7”
	url = 'https://update.nsfocus.com/update/listSasDetail/v/engine5.6.7'
	file_path = './UpdateThePackage/安全审计系统(SAS)/安全审计系统(SAS)/引擎升级包 5.6.7/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->安全审计系统(SAS)->引擎升级包 5.6.7”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“安全审计系统(SAS)->安全审计系统(SAS)->应用规则升级包 6.0.0”
	url = 'https://update.nsfocus.com/update/listSasDetail/v/apprule6.0.0'
	file_path = './UpdateThePackage/安全审计系统(SAS)/安全审计系统(SAS)/应用规则升级包 6.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->安全审计系统(SAS)->应用规则升级包 6.0.0”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->安全审计系统(SAS)->应用规则升级包 5.6.7”
	url = 'https://update.nsfocus.com/update/listSasDetail/v/engine5.6.7'
	file_path = './UpdateThePackage/安全审计系统(SAS)/安全审计系统(SAS)/应用规则升级包 5.6.7/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->安全审计系统(SAS)->应用规则升级包 5.6.7”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->安全审计系统(SAS)->Url分类库升级包 5.6.7”
	url = 'https://update.nsfocus.com/update/listUrllibDetail/v/5.6.6/m/4'
	file_path = './UpdateThePackage/安全审计系统(SAS)/安全审计系统(SAS)/Url分类库升级包 5.6.7/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->安全审计系统(SAS)->Url分类库升级包 5.6.7”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->安全审计系统(SAS)->Url分类库升级包 5.6.8-5.6.10”
	url = 'https://update.nsfocus.com/update/listUrllibDetail/v/5.6/m/4'
	file_path = './UpdateThePackage/安全审计系统(SAS)/安全审计系统(SAS)/Url分类库升级包 5.6.8-5.6.10/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->安全审计系统(SAS)->Url分类库升级包 5.6.8-5.6.10”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->安全审计系统(SAS)->恶意站点库升级包5.6.7-5.6.10”
	url = 'https://update.nsfocus.com/update/listWebmalwareDetail/v/5.6.8/m/2'
	file_path = './UpdateThePackage/安全审计系统(SAS)/安全审计系统(SAS)/恶意站点库升级包5.6.7-5.6.10/'
	path_features = r'<a href="(.*)" \r\n >web'
	filename_features = r'>web(.*)</a>'
	filename_features_n = 'web'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->安全审计系统(SAS)->恶意站点库升级包5.6.7-5.6.10”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)



	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                      [信息技术应用创新系列]安全审计系统(SAS)                       ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“安全审计系统(SAS)->[信息技术应用创新系列]安全审计系统(SAS)->兆芯系列（x86_64-zx）5.6.10->引擎升级包”
	url = 'https://update.nsfocus.com/update/listSasDetail/v/x86_64-zx'
	file_path = './UpdateThePackage/安全审计系统(SAS)/[信息技术应用创新系列]安全审计系统(SAS)/兆芯系列（x86_64-zx）5.6.10/引擎升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->[信息技术应用创新系列]安全审计系统(SAS)->兆芯系列（x86_64-zx）5.6.10->引擎升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->[信息技术应用创新系列]安全审计系统(SAS)->兆芯系列（x86_64-zx）5.6.10->URL分类库升级包”
	url = 'https://update.nsfocus.com/update/listUrllibDetail/v/5.6/m/4'
	file_path = './UpdateThePackage/安全审计系统(SAS)/[信息技术应用创新系列]安全审计系统(SAS)/兆芯系列（x86_64-zx）5.6.10/URL分类库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->[信息技术应用创新系列]安全审计系统(SAS)->兆芯系列（x86_64-zx）5.6.10->URL分类库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->[信息技术应用创新系列]安全审计系统(SAS)->兆芯系列（x86_64-zx）5.6.10->恶意站点升级包”
	url = 'https://update.nsfocus.com/update/listWebmalwareDetail/v/5.6.8/m/4'
	file_path = './UpdateThePackage/安全审计系统(SAS)/[信息技术应用创新系列]安全审计系统(SAS)/兆芯系列（x86_64-zx）5.6.10/恶意站点升级包/'
	path_features = r'<a href="(.*)" \r\n >web'
	filename_features = r'>web(.*)</a>'
	filename_features_n = 'web'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->[信息技术应用创新系列]安全审计系统(SAS)->兆芯系列（x86_64-zx）5.6.10->恶意站点升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“安全审计系统(SAS)->[信息技术应用创新系列]安全审计系统(SAS)->兆芯系列（x86_64-zx）5.6.10->应用规则升级包”
	url = 'https://update.nsfocus.com/update/listSasDetail/v/apprule6.0.0'
	file_path = './UpdateThePackage/安全审计系统(SAS)/[信息技术应用创新系列]安全审计系统(SAS)/兆芯系列（x86_64-zx）5.6.10/应用规则升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“安全审计系统(SAS)->[信息技术应用创新系列]安全审计系统(SAS)->兆芯系列（x86_64-zx）5.6.10->应用规则升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 SAS 升级包的更新  *********************************\n')

Update()