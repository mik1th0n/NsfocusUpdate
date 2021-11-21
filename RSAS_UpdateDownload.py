#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/31 01:30
# @Author     :mik1th0n
# @File       :RSAS_UpdateDownload.py


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
	****                           远程安全评估系统(RSAS) 5.0                             ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 5.0”
	url = 'http://update.nsfocus.com/update/listAurora/v/5'
	file_path = './UpdateThePackage/远程安全评估系统(RSAS)/远程安全评估系统(RSAS) 5.0/'
	path_features = r'<a href="(.*)" \r\n >aur'
	filename_features = r'aur(.*)</a>'
	filename_features_n = 'aur'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 5.0”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)



	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                           远程安全评估系统(RSAS) 6.0                             ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0->RSAS V6.0系统升级包”
	url = 'http://update.nsfocus.com/update/listRsasDetail/v/rsassys'
	file_path = './UpdateThePackage/远程安全评估系统(RSAS)/远程安全评估系统(RSAS) 6.0/RSAS V6.0系统升级包/'
	path_features = r'<a href="(.*)" \r\n >rsas-'
	filename_features = r'rsas-(.*)</a>'
	filename_features_n = 'rsas-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0->RSAS V6.0系统升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0->RSAS V6.0系统插件升级包”
	url = 'http://update.nsfocus.com/update/listRsasDetail/v/vulsys'
	file_path = './UpdateThePackage/远程安全评估系统(RSAS)/远程安全评估系统(RSAS) 6.0/RSAS V6.0系统插件升级包/'
	path_features = r'<a href="(.*)" \r\n >rsas-'
	filename_features = r'rsas-(.*)</a>'
	filename_features_n = 'rsas-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0->RSAS V6.0系统插件升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0->RSAS V6.0 Web插件升级包”
	url = 'http://update.nsfocus.com/update/listRsasDetail/v/vulweb'
	file_path = './UpdateThePackage/远程安全评估系统(RSAS)/远程安全评估系统(RSAS) 6.0/RSAS V6.0 Web插件升级包/'
	path_features = r'<a href="(.*)" \r\n >rsas-'
	filename_features = r'rsas-(.*)</a>'
	filename_features_n = 'rsas-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0->RSAS V6.0 Web插件升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                       远程安全评估系统(RSAS) 6.0 飞腾系列                         ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0 飞腾系列->RSAS V6.0系统升级包(HFA HFB)”
	url = 'http://update.nsfocus.com/update/listRsasDetail/v/rsassys-arm64'
	file_path = './UpdateThePackage/远程安全评估系统(RSAS)/远程安全评估系统(RSAS) 6.0 飞腾系列/RSAS V6.0系统升级包(HFA HFB)/'
	path_features = r'<a href="(.*)" \r\n >rsas-'
	filename_features = r'rsas-(.*)</a>'
	filename_features_n = 'rsas-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0 飞腾系列->RSAS V6.0系统升级包(HFA HFB)”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0 飞腾系列->RSAS V6.0系统升级包(HFC)”
	url = 'http://update.nsfocus.com/update/listRsasDetail/v/rsassys-arm64-4c8c'
	file_path = './UpdateThePackage/远程安全评估系统(RSAS)/远程安全评估系统(RSAS) 6.0 飞腾系列/RSAS V6.0系统升级包(HFC)/'
	path_features = r'<a href="(.*)" \r\n >rsas-'
	filename_features = r'rsas-(.*)</a>'
	filename_features_n = 'rsas-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0 飞腾系列->RSAS V6.0系统升级包(HFC)”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0 飞腾系列->RSAS V6.0系统插件升级包”
	url = 'http://update.nsfocus.com/update/listRsasDetail/v/vulsys-arm64'
	file_path = './UpdateThePackage/远程安全评估系统(RSAS)/远程安全评估系统(RSAS) 6.0 飞腾系列/RSAS V6.0系统插件升级包/'
	path_features = r'<a href="(.*)" \r\n >rsas-'
	filename_features = r'rsas-(.*)</a>'
	filename_features_n = 'rsas-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0 飞腾系列->RSAS V6.0系统插件升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0 飞腾系列->RSAS V6.0 WEB插件升级包”
	url = 'http://update.nsfocus.com/update/listRsasDetail/v/vulweb-arm64'
	file_path = './UpdateThePackage/远程安全评估系统(RSAS)/远程安全评估系统(RSAS) 6.0 飞腾系列/RSAS V6.0 WEB插件升级包/'
	path_features = r'<a href="(.*)" \r\n >rsas-'
	filename_features = r'rsas-(.*)</a>'
	filename_features_n = 'rsas-'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“远程安全评估系统(RSAS)->远程安全评估系统(RSAS) 6.0 飞腾系列->RSAS V6.0 WEB插件升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 RSAS 升级包的更新  *********************************\n')

#Update()