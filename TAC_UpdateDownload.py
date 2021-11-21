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
	****                         威胁分析系统在线检测系列(TAC-D)                           ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V1.0.0->引擎升级包 1.0.0”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/engine1.0.0'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V1.0.0/引擎升级包 1.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V1.0.0->引擎升级包 1.0.0”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V1.0.0->病毒库升级包 6.0.0”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/av6.0.0'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V1.0.0/病毒库升级包 6.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V1.0.0->病毒库升级包 6.0.0”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.0->引擎升级包 2.0.0”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/v2.0.0'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V2.0.0/引擎升级包 2.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.0->引擎升级包 2.0.0”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.0>病毒库升级包 6.0.0”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/av6.0.0'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V2.0.0/病毒库升级包 6.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.0->病毒库升级包 6.0.0”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.1->引擎升级包 2.0.1”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/v2.0.1'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V2.0.1/引擎升级包 2.0.1/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.1->引擎升级包 2.0.1”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.1->病毒库升级包 7.0.0”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/av7.0.0'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V2.0.1/病毒库升级包 7.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.1->病毒库升级包 7.0.0”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.2->引擎升级包 2.0.2”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/v2.0.2'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V2.0.2/引擎升级包 2.0.2/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.2->引擎升级包 2.0.2”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.2->病毒库升级包 7.0.0”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/av7.0.0'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V2.0.2/病毒库升级包 7.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.2->病毒库升级包 7.0.0”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.2->规则升级包 2.0.2”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/ruleV2.0.2'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V2.0.2/规则升级包 2.0.2/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.2->规则升级包 2.0.2”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.2->DGA规则升级包 2.0.2”
	url = 'https://update.nsfocus.com/update/listTacDetail/v/dga_rule_v2.0.2'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统在线检测系列(TAC-D)/V2.0.2/DGA规则升级包 2.0.2/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统在线检测系列(TAC-D)->V2.0.2->DGA规则升级包 2.0.2”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)




	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                         威胁分析系统邮件防护系列(TAC-E)                           ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->引擎升级包 2.0.2”
	url = 'https://update.nsfocus.com/update/listTacEDetail/v/v2.0.2'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统邮件防护系列(TAC-E)/V2.0.2/引擎升级包 2.0.2/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->引擎升级包 2.0.2”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->病毒库升级包 7.0.0”
	url = 'https://update.nsfocus.com/update/listTacEDetail/v/av7.0.0'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统邮件防护系列(TAC-E)/V2.0.2/病毒库升级包 7.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->病毒库升级包 7.0.0”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->规则升级包 2.0.2”
	url = 'https://update.nsfocus.com/update/listTacEDetail/v/ruleV2.0.2'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统邮件防护系列(TAC-E)/V2.0.2/规则升级包 2.0.2/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->规则升级包 2.0.2”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->情报升级包 2.0.0”
	url = 'https://update.nsfocus.com/update/listTacEDetail/v/ntiV2.0.0'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统邮件防护系列(TAC-E)/V2.0.2/情报升级包 2.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->DGA规则升级包 2.0.2”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->DGA规则升级包 2.0.2”
	url = 'https://update.nsfocus.com/update/listTacEDetail/v/dga_rule_v2.0.2'
	file_path = './UpdateThePackage/威胁分析中心(TAC)/威胁分析系统邮件防护系列(TAC-E)/V2.0.2/DGA规则升级包 2.0.2/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“威胁分析中心(TAC)->威胁分析系统邮件防护系列(TAC-E)->V2.0.2->DGA规则升级包 2.0.2”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	print('\n*********************************  祝贺你完成 TAC 升级包的更新  *********************************\n')

Update()