#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/11/02 22:55
# @Author     :mik1th0n
# @File       :NF_UpdateDownload.py


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
	****                                 下一代防火墙(NF)                                 ****
	****                                                                                 ****
	*****************************************************************************************
	'''

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->引擎升级包->引擎升级包 6.0.3”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/nf6.0.3'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/引擎升级包/引擎升级包 6.0.3/'
	path_features = r'<a href="(.*)" \r\n >up'
	filename_features = r'>up(.*)</a>'
	filename_features_n = 'up'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->引擎升级包->引擎升级包 6.0.3”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->引擎升级包->引擎升级包 6.0.2”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/nf6.0.2'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/引擎升级包/引擎升级包 6.0.2/'
	path_features = r'<a href="(.*)" \r\n >up'
	filename_features = r'>up(.*)</a>'
	filename_features_n = 'up'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->引擎升级包->引擎升级包 6.0.2”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->引擎升级包->引擎升级包（虚拟化版）6.0.1”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/vNF6.0.1'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/引擎升级包/引擎升级包（虚拟化版）6.0.1/'
	path_features = r'<a href="(.*)" \r\n >up'
	filename_features = r'>up(.*)</a>'
	filename_features_n = 'up'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->引擎升级包->引擎升级包（虚拟化版）6.0.1”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->规则库升级包->规则升级包 6.0.1_6.0.3”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/rule6.0.1'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/规则库升级包/规则升级包 6.0.1_6.0.3/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->规则库升级包->规则升级包 6.0.1_6.0.3”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->规则库升级包->规则升级包 6.0.2”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/rule6.0.2'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/规则库升级包/规则升级包 6.0.2/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->规则库升级包->规则升级包 6.0.2”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->病毒特征库升级包->病毒特征库升级包 6.0.0”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/av6.0.0'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/病毒特征库升级包/病毒特征库升级包 6.0.0/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->病毒特征库升级包->病毒特征库升级包 6.0.0”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->病毒特征库升级包->病毒特征库升级包 6.0.1”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/av6.0.1'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/病毒特征库升级包/病毒特征库升级包 6.0.1/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->病毒特征库升级包->病毒特征库升级包 6.0.1”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->应用规则库升级包”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/apprule6.0.0'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/应用规则库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->应用规则库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->URL分类库升级包”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/urllib6.0.0'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/URL分类库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'>eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->URL分类库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->恶意站点库升级包”
	url = 'https://update.nsfocus.com/update/listNewNfDetail/v/webmalware5.6.7'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/恶意站点库升级包/'
	path_features = r'<a href="(.*)" \r\n >web'
	filename_features = r'>web(.*)</a>'
	filename_features_n = 'web'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->恶意站点库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->NF其他升级包->NF特殊升级包”
	url = 'https://update.nsfocus.com/update/listNewNfSpecialDetail/v/special'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/NF其他升级包/NF特殊升级包/'
	path_features = r'<a href="(.*)" \r\n >up'
	filename_features = r'>up(.*)</a>'
	filename_features_n = 'up'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->NF其他升级包->NF特殊升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->NF其他升级包->NF接口升级包”
	url = 'https://update.nsfocus.com/update/listNewNfInterfaceDetail/v/interface'
	file_path = './UpdateThePackage/下一代防火墙系统(NF)/下一代防火墙(NF)/NF其他升级包/NF接口升级包/'
	path_features = r'<a href="(.*)" \r\n >NPAI'
	filename_features = r'>NPAI(.*)</a>'
	filename_features_n = 'NPAI'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“下一代防火墙系统(NF)->下一代防火墙(NF)->NF其他升级包->NF接口升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)



	print('\n*********************************  祝贺你完成 NF 升级包的更新  *********************************\n')

Update()