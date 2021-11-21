#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/30 22:30
# @Author     :mik1th0n
# @File       :IDS_IPS_UpdateDownload.py


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
	****                             网络入侵检测系统 5.6.11                              ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->引擎升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/engine5.6.11'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.11/引擎升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->引擎升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->系统规则升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/rule5.6.11'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.11/系统规则升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->系统规则升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->URL分类库升级包”
	url = 'http://update.nsfocus.com/update/listUrllibDetail/v/newurllib/m/1'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.11/URL分类库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->URL分类库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->流式病毒特征库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/av5.6.11'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.11/流式病毒特征库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->流式病毒特征库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->启发式病毒库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/av7.0.0'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.11/启发式病毒库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.11->启发式病毒库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                             网络入侵检测系统 5.6.10                              ****
	****                                                                                 ****
	*****************************************************************************************
	'''

	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.10->引擎升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/engine5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.10/引擎升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.10->引擎升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.10->系统规则库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/rule5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.10/系统规则库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.10->系统规则库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.10->URL分类库升级包”
	url = 'http://update.nsfocus.com/update/listUrllibDetail/v/newurllib/m/1'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.10/URL分类库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.10->URL分类库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.10->病毒特征库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/av5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.10/病毒特征库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.10->病毒特征库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                             网络入侵检测系统 5.6.9                               ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.9->引擎升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/engine5.6.9'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.9/引擎升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.9->引擎升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.9->系统规则库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/rule5.6.9'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.9/系统规则库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.9->系统规则库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.9->URL分类库升级包”
	url = 'http://update.nsfocus.com/update/listUrllibDetail/v/newurllib/m/1'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.9/URL分类库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.9->URL分类库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.9->病毒特征库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/av5.6.9'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 5.6.9/病毒特征库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 5.6.9->病毒特征库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                        网络入侵检测系统 兆芯 ZX 5.6.10                           ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 兆芯 ZX 5.6.10->引擎升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/ZX-engine5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 兆芯 ZX 5.6.10/引擎升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 兆芯 ZX 5.6.10->引擎升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 兆芯 ZX 5.6.10->规则升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/rule5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 兆芯 ZX 5.6.10/规则升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 兆芯 ZX 5.6.10->规则升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 兆芯 ZX 5.6.10->流式病毒库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/av5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 兆芯 ZX 5.6.10/流式病毒库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 兆芯 ZX 5.6.10->流式病毒库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                        网络入侵检测系统 飞腾 FT 5.6.10                           ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10->引擎升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/ZX-engine5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 飞腾 FT 5.6.10/引擎升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10->引擎升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10->规则升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/rule5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 飞腾 FT 5.6.10/规则升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10->规则升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10->流式病毒库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/av5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 飞腾 FT 5.6.10/流式病毒库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10>流式病毒库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10->启发式病毒库升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/FT-av5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 飞腾 FT 5.6.10/启发式病毒库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10>启发式病毒库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10->URL分类升级包”
	url = 'http://update.nsfocus.com/update/listNewidsDetail/v/FT-url5.6.10'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 飞腾 FT 5.6.10/URL分类升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 飞腾 FT 5.6.10>URL分类升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	'''  
	*****************************************************************************************
	****                                                                                 ****
	****                         网络入侵检测系统 申威 SW 5.6.8                            ****
	****                                                                                 ****
	*****************************************************************************************
	'''
	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 申威 SW 5.6.8->国产化网络入侵检测系统5.6.8->引擎升级包”
	url = 'http://update.nsfocus.com/update/idsSwIndexDetail/v/engine5.6.8'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 申威 SW 5.6.8/国产化网络入侵检测系统5.6.8/引擎升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 申威 SW 5.6.8->国产化网络入侵检测系统5.6.8->引擎升级包”')
	UpdateGeneralDownload.down_sys_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 申威 SW 5.6.8->国产化网络入侵检测系统5.6.8->规则升级包”
	url = 'http://update.nsfocus.com/update/idsSwIndexDetail/v/rule5.6.8'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 申威 SW 5.6.8/国产化网络入侵检测系统5.6.8/规则升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 申威 SW 5.6.8->国产化网络入侵检测系统5.6.8->规则升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 申威 SW 5.6.8->国产化网络入侵检测系统5.6.8->病毒特征库升级包”
	url = 'http://update.nsfocus.com/update/idsSwIndexDetail/v/av5.6.8'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 申威 SW 5.6.8/国产化网络入侵检测系统5.6.8/病毒特征库升级包/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 申威 SW 5.6.8->国产化网络入侵检测系统5.6.8->病毒特征库升级包”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	# 下载“网络入侵检测系统(IDS)->网络入侵检测系统 申威 SW 5.6.8->国产化网络入侵检测系统5.6.8->Url分类库升级包 5.6”
	url = 'http://update.nsfocus.com/update/listUrllibDetail/v/5.6/m/1'
	file_path = './UpdateThePackage/网络入侵检测系统(IDS)/网络入侵检测系统 申威 SW 5.6.8/国产化网络入侵检测系统5.6.8/Url分类库升级包 5.6/'
	path_features = r'<a href="(.*)" \r\n >eoi'
	filename_features = r'eoi(.*)</a>'
	filename_features_n = 'eoi'
	print('\r\n' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '： 下载“网络入侵检测系统(IDS)->网络入侵检测系统 申威 SW 5.6.8->国产化网络入侵检测系统5.6.8->Url分类库升级包 5.6”')
	UpdateGeneralDownload.down_rule_file(url,headers,path_features,filename_features,file_path,filename_features_n)


	print('\n*********************************  祝贺你完成 IDS/IPS 升级包的更新  *********************************\n')

#Update()