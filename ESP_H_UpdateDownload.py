#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/31 03:14
# @Author     :mik1th0n
# @File       :ESP-H_UpdateDownload.py


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
	****                             绿盟安全管理平台(ESP-H)                              ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“绿盟安全管理平台(ESP-H)->系统升级包->V3.0R00F06”
	url = 'http://update.nsfocus.com/update/listesphDetail/v/V3.0F06'
	file_path = './UpdateThePackage/绿盟安全管理平台(ESP-H)/系统升级包/V3.0R00F06/'
	path_features = r'<a href="(.*)" \r\n >NE'
	filename_features = r'>NE(.*)</a>'
	filename_features_n = 'NE'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟安全管理平台(ESP-H)->系统升级包->V3.0R00F06”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟安全管理平台(ESP-H)->系统升级包->V3.0R00F07”
	url = 'http://update.nsfocus.com/update/listesphDetail/v/V3.0F07'
	file_path = './UpdateThePackage/绿盟安全管理平台(ESP-H)/系统升级包/V3.0R00F07/'
	path_features = r'<a href="(.*)" \r\n >NE'
	filename_features = r'>NE(.*)</a>'
	filename_features_n = 'NE'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟安全管理平台(ESP-H)->系统升级包->V3.0R00F07”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟安全管理平台(ESP-H)->系统升级包->V3.0R01”
	url = 'http://update.nsfocus.com/update/listesphDetail/v/V3.0R01'
	file_path = './UpdateThePackage/绿盟安全管理平台(ESP-H)/系统升级包/V3.0R01/'
	path_features = r'<a href="(.*)" \r\n >es'
	filename_features = r'>es(.*)</a>'
	filename_features_n = 'es'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟安全管理平台(ESP-H)->系统升级包->V3.0R01”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟安全管理平台(ESP-H)->ESP-H 规则升级包->V3.0R00F06”
	url = 'http://update.nsfocus.com/update/listesphDetail/v/RULEV3.0R00F06'
	file_path = './UpdateThePackage/绿盟安全管理平台(ESP-H)/ESP-H 规则升级包/V3.0R00F06/'
	path_features = r'<a href="(.*)" \r\n >ES'
	filename_features = r'>ES(.*)</a>'
	filename_features_n = 'ES'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟安全管理平台(ESP-H)->ESP-H 规则升级包->V3.0R00F06”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟安全管理平台(ESP-H)->ESP-H 规则升级包->V3.0R00F07”
	url = 'http://update.nsfocus.com/update/listesphDetail/v/RULEV3.0R00F07'
	file_path = './UpdateThePackage/绿盟安全管理平台(ESP-H)/ESP-H 规则升级包/V3.0R00F07/'
	path_features = r'<a href="(.*)" \r\n >ES'
	filename_features = r'>ES(.*)</a>'
	filename_features_n = 'ES'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟安全管理平台(ESP-H)->ESP-H 规则升级包->V3.0R00F07”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟安全管理平台(ESP-H)->ESP-H 规则升级包->V3.0R01->解析规则包”
	url = 'http://update.nsfocus.com/update/listesphDetail/v/V3.0R01PR'
	file_path = './UpdateThePackage/绿盟安全管理平台(ESP-H)/ESP-H 规则升级包/V3.0R01/解析规则包/'
	path_features = r'<a href="(.*)" \r\n >par'
	filename_features = r'>par(.*)</a>'
	filename_features_n = 'par'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟安全管理平台(ESP-H)->ESP-H 规则升级包->V3.0R01->解析规则包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟安全管理平台(ESP-H)->ESP-H 规则升级包->V3.0R01->攻击识别规则包”
	url = 'http://update.nsfocus.com/update/listesphDetail/v/V3.0R01F00NG'
	file_path = './UpdateThePackage/绿盟安全管理平台(ESP-H)/ESP-H 规则升级包/V3.0R01/攻击识别规则包/'
	path_features = r'<a href="(.*)" \r\n >par'
	filename_features = r'>par(.*)</a>'
	filename_features_n = 'par'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟安全管理平台(ESP-H)->ESP-H 规则升级包->V3.0R01->攻击识别规则包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟安全管理平台(ESP-H)->漏洞库升级包”
	url = 'http://update.nsfocus.com/update/listesphDetail/v/V3.0R01F00NG'
	file_path = './UpdateThePackage/绿盟安全管理平台(ESP-H)/漏洞库升级包/'
	path_features = r'<a href="(.*)" \r\n >iso'
	filename_features = r'>iso(.*)</a>'
	filename_features_n = 'iso'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟安全管理平台(ESP-H)->漏洞库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 ESP-H 升级包的更新  *********************************\n')

#Update()