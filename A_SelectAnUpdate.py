#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/31 03:29
# @Author     :mik1th0n
# @File       :1.SelectAnUpdate.py

import sys
import time
import UpdateGeneralDownload
import ESPC_L_UpdateDownload
import ISOP_UpdateDownload
import CSSP_UpdateDownload
import ESP_H_UpdateDownload
import IDS_IPS_UpdateDownload
import RSAS_UpdateDownload

def SelectProduct(Select):
	if Select == '0':
		ESPC_L_UpdateDownload.Update()
		ISOP_UpdateDownload.Update()
		CSSP_UpdateDownload.Update()
		ESP_H_UpdateDownload.Update()
		IDS_IPS_UpdateDownload.Update()
		RSAS_UpdateDownload.Update()
		print('\n**************************************************************************************************')
		print('***                                                                                            ***')
		print('***                                  祝贺你完成所有升级包的更新                                ***')
		print('***                                                                                            ***')
		print('**************************************************************************************************\n')
	elif Select == '1':
		ESPC_L_UpdateDownload.Update()
	elif Select == '2':
		ISOP_UpdateDownload.Update()


def main():
	
	SProduct = '9999'

	print('\n  *********************************')
	print('  **  时间：' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+ '  **')
	print('  **  作者：mik1th0n             **')
	print('  **-----------------------------**')
	print('  **       0 ：所有产品          **')
	print('  **       1 ：ESPC-L            **')
	print('  **       2 ：ISOP              **')
	print('  *********************************\n')

	SelectTheProduct = input("请输入数字，下载对应产品升级包（默认值：0）:")

	if(len(SelectTheProduct) == 0):
		SProduct = '0'
	elif((SelectTheProduct == '0') | (SelectTheProduct == '1') | (SelectTheProduct == '2') ):
		SProduct = SelectTheProduct
	else:
		print('\n\n\n\n请输入图中对应数字进行选择！！！')
		main()

	SelectProduct(SProduct)


if __name__ == "__main__":
    main()
