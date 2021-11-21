#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/11/02 21:59
# @Author     :mik1th0n
# @File       :WAF_UpdateDownload


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
	****                               WEB应用防护系统(WAF)                               ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“WEB应用防护系统(WAF)->WAF V6.0.7->WAF V6.0.7 系统升级包”
	url = 'https://update.nsfocus.com/update/listWafV67Detail/v/sys6070'
	file_path = './UpdateThePackage/WEB应用防护系统(WAF)/WAF V6.0.7/WAF V6.0.7 系统升级包/'
	path_features = r'<a href="(.*)" \r\n >waf'
	filename_features = r'>waf(.*)</a>'
	filename_features_n = 'waf'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“WEB应用防护系统(WAF)->WAF V6.0.7->WAF V6.0.7 系统升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“WEB应用防护系统(WAF)->WAF V6.0.7->WAF V6.0.7 规则升级包”
	url = 'https://update.nsfocus.com/update/listWafV67Detail/v/rule6070'
	file_path = './UpdateThePackage/WEB应用防护系统(WAF)/WAF V6.0.7/WAF V6.0.7 规则升级包/'
	path_features = r'<a href="(.*)" \r\n >up'
	filename_features = r'>up(.*)</a>'
	filename_features_n = 'up'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“WEB应用防护系统(WAF)->WAF V6.0.7->WAF V6.0.7 规则升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“WEB应用防护系统(WAF)->WAF V6.0.6->WAF V6.0.6 引擎升级包”
	url = 'https://update.nsfocus.com/update/listWafV66Detail/v/engine6.0.6'
	file_path = './UpdateThePackage/WEB应用防护系统(WAF)/WAF V6.0.6/WAF V6.0.6 引擎升级包/'
	path_features = r'<a href="(.*)" \r\n >waf'
	filename_features = r'>waf(.*)</a>'
	filename_features_n = 'waf'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“WEB应用防护系统(WAF)->WAF V6.0.6->WAF V6.0.6 规则升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“WEB应用防护系统(WAF)->WAF V6.0.6->WAF V6.0.6 规则升级包”
	url = 'https://update.nsfocus.com/update/listWafV66Detail/v/rule6.0.6'
	file_path = './UpdateThePackage/WEB应用防护系统(WAF)/WAF V6.0.6/WAF V6.0.6 规则升级包/'
	path_features = r'<a href="(.*)" \r\n >up'
	filename_features = r'>up(.*)</a>'
	filename_features_n = 'up'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“WEB应用防护系统(WAF)->WAF V6.0.6->WAF V6.0.6 规则升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)

	# 下载“WEB应用防护系统(WAF)->WAF规则包”
	url = 'https://update.nsfocus.com/update/listWafSpecialDetail/v/all'
	file_path = './UpdateThePackage/WEB应用防护系统(WAF)/WAF规则包/'
	path_features = r'<a href="(.*)" \r\n >up'
	filename_features = r'>up(.*)</a>'
	filename_features_n = 'up'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“WEB应用防护系统(WAF)->WAF规则包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 WAF 升级包的更新  *********************************\n')

Update()