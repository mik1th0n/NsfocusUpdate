#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/31 02:47
# @Author     :mik1th0n
# @File       :ISOP_UpdateDownload.py


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
	****                            绿盟智能安全运营平台(ISOP)                             ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“绿盟智能安全运营平台(ISOP)->ISOP V3.0R01 规则包->解析规则包”
	url = 'http://update.nsfocus.com/update/listisopdetail/v/V3.0R01PR'
	file_path = './UpdateThePackage/绿盟智能安全运营平台(ISOP)/ISOP V3.0R01 规则包/解析规则包/'
	path_features = r'<a href="(.*)" \r\n >par'
	filename_features = r'>par(.*)</a>'
	filename_features_n = 'par'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟智能安全运营平台(ISOP)->ISOP V3.0R01 规则包->解析规则包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“绿盟智能安全运营平台(ISOP)->ISOP V3.0R01 规则包->攻击识别规则包”
	url = 'http://update.nsfocus.com/update/listisopdetail/v/V3.0R01F00NG'
	file_path = './UpdateThePackage/绿盟智能安全运营平台(ISOP)/ISOP V3.0R01 规则包/攻击识别规则包/'
	path_features = r'<a href="(.*)" \r\n >att'
	filename_features = r'>att(.*)</a>'
	filename_features_n = 'att'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟智能安全运营平台(ISOP)->ISOP V3.0R01 规则包->攻击识别规则包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)



	# 下载“绿盟智能安全运营平台(ISOP)->ISOP V3.0R01 规则包->行为分析规则包”
	url = 'http://update.nsfocus.com/update/listisopdetail/v/V3.0R01F00UEBA'
	file_path = './UpdateThePackage/绿盟智能安全运营平台(ISOP)/ISOP V3.0R01 规则包/行为分析规则包/'
	path_features = r'<a href="(.*)" \r\n >uba'
	filename_features = r'>uba(.*)</a>'
	filename_features_n = 'uba'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟智能安全运营平台(ISOP)->ISOP V3.0R01 规则包->行为分析规则包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)



	# 下载“绿盟智能安全运营平台(ISOP)->ISOP V3.0R01F00 漏洞库”
	url = 'http://update.nsfocus.com/update/listisopdetail/v/V3.0R01F00LEAK'
	file_path = './UpdateThePackage/绿盟智能安全运营平台(ISOP)/ISOP V3.0R01F00 漏洞库/'
	path_features = r'<a href="(.*)" \r\n >iso'
	filename_features = r'>iso(.*)</a>'
	filename_features_n = 'iso'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“绿盟智能安全运营平台(ISOP)->ISOP V3.0R01F00 漏洞库”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)



	print('\n*********************************  祝贺你完成 ISOP 升级包的更新  *********************************\n')

#Update()