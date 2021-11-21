#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/10/31 03:29
# @Author     :mik1th0n
# @File       :1.SelectAnUpdate.py

import sys
import time
import UpdateGeneralDownload

import CSSP_UpdateDownload
import DMS_UpdateDownload
import ESPC_L_UpdateDownload
import ESP_H_UpdateDownload
import ESP_UpdateDownload
import IDR_UpdateDownload
import IDS_IPS_UpdateDownload
import ISOP_UpdateDownload
import NCSS_I_UpdateDownload
import NF_UpdateDownload
import OSMS_SASH_UpdateDownload
import RSAS_UpdateDownload
import SAS_L_UpdateDownload
import SAS_UpdateDownload
import TAC_UpdateDownload
import WAF_UpdateDownload
import BVS_UpdateDownload
import TVM_UpdateDownload
import WSM_UpdateDownload
import WVSS_UpdateDownload

def SelectProduct(Select):
	if Select == '0':
		CSSP_UpdateDownload.Update()
		DMS_UpdateDownload.Update()
		ESPC_L_UpdateDownload.Update()
		ESP_H_UpdateDownload.Update()
		ESP_UpdateDownload.Update()
		IDR_UpdateDownload.Update()
		IDS_IPS_UpdateDownload.Update()
		ISOP_UpdateDownload.Update()
		NCSS_I_UpdateDownload.Update()
		NF_UpdateDownload.Update()
		OSMS_SASH_UpdateDownload.Update()
		RSAS_UpdateDownload.Update()
		SAS_L_UpdateDownload.Update()
		SAS_UpdateDownload.Update()
		TAC_UpdateDownload.Update()
		WAF_UpdateDownload.Update()
		BVS_UpdateDownload.Update()
		TVM_UpdateDownload.Update()
		WSM_UpdateDownload.Update()
		WVSS_UpdateDownload.Update()

		print('\n**************************************************************************************************')
		print('***                                                                                            ***')
		print('***                                  祝贺你完成所有升级包的更新                                ***')
		print('***                                                                                            ***')
		print('**************************************************************************************************\n')

	elif Select == '1':
		CSSP_UpdateDownload.Update()
	elif Select == '2':	
		DMS_UpdateDownload.Update()
	elif Select == '3':
		ESPC_L_UpdateDownload.Update()
	elif Select == '4':
		ESP_H_UpdateDownload.Update()
	elif Select == '5':
		ESP_UpdateDownload.Update()
	elif Select == '6':
		IDR_UpdateDownload.Update()
	elif Select == '7':
		IDS_IPS_UpdateDownload.Update()
	elif Select == '8':
		ISOP_UpdateDownload.Update()
	elif Select == '9':
		NCSS_I_UpdateDownload.Update()
	elif Select == '10':
		NF_UpdateDownload.Update()
	elif Select == '11':
		OSMS_SASH_UpdateDownload.Update()
	elif Select == '12':
		RSAS_UpdateDownload.Update()
	elif Select == '13':
		SAS_L_UpdateDownload.Update()
	elif Select == '14':
		SAS_UpdateDownload.Update()
	elif Select == '15':
		TAC_UpdateDownload.Update()
	elif Select == '16':
		WAF_UpdateDownload.Update()
	elif Select == '17':
		BVS_UpdateDownload.Update()
	elif Select == '18':
		TVM_UpdateDownload.Update()		
	elif Select == '19':
		WSM_UpdateDownload.Update()
	elif Select == '20':
		WVSS_UpdateDownload.Update()

def main():
	
	SProduct = '9999'

	print('\n  *********************************')
	print('  **                             **')
	print('  **  时间：' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+ '  **')
	print('  **                             **')
	print('  **  作者：mik1th0n             **')
	print('  **                             **')
	print('  **-----------------------------**')
	print('  **        0 ：所有产品         **')
	print('  **        1 ：CSSP             **')
	print('  **        2 ：DMS              **')
	print('  **        3 ：ESPC-L           **')
	print('  **        4 ：ESP-H            **')
	print('  **        5 ：ESP              **')
	print('  **        6 ：IDR              **')
	print('  **        7 ：IDS/IPS          **')
	print('  **        8 ：ISOP             **')
	print('  **        9 ：NCSS-I           **')
	print('  **       10 ：NF               **')
	print('  **       11 ：OSMS/SAS-H       **')
	print('  **       12 ：RSAS             **')
	print('  **       13 ：SAS-L            **')
	print('  **       14 ：SAS              **')
	print('  **       15 ：TAC              **')
	print('  **       16 ：WAF              **')
	print('  **       17 ：BVS              **')
	print('  **       18 ：TVM              **')
	print('  **       19 ：WSM              **')
	print('  **       20 ：WVSS             **')
	print('  *********************************\n')

	SelectTheProduct = input("请输入数字，下载对应产品升级包（默认值：0）:")

	if(len(SelectTheProduct) == 0):
		SProduct = '0'
	elif((SelectTheProduct == '0') 
		| (SelectTheProduct == '1') 
		| (SelectTheProduct == '2') 
		| (SelectTheProduct == '3') 
		| (SelectTheProduct == '4') 
		| (SelectTheProduct == '5') 
		| (SelectTheProduct == '6') 
		| (SelectTheProduct == '7') 
		| (SelectTheProduct == '8') 
		| (SelectTheProduct == '9') 
		| (SelectTheProduct == '10') 
		| (SelectTheProduct == '11') 
		| (SelectTheProduct == '12') 
		| (SelectTheProduct == '13') 
		| (SelectTheProduct == '14') 
		| (SelectTheProduct == '15') 
		| (SelectTheProduct == '16') 
		| (SelectTheProduct == '17') 
		| (SelectTheProduct == '18') 
		| (SelectTheProduct == '19') 
		| (SelectTheProduct == '20') 
		):
		SProduct = SelectTheProduct
	else:
		print('\n\n\n\n请输入图中对应数字进行选择！！！')
		main()

	SelectProduct(SProduct)


if __name__ == "__main__":
    main()
