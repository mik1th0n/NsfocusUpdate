#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# @Time       :2021/11/02 01:52
# @Author     :mik1th0n
# @File       :2.AutomaticUpdateAll.py

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


def main():
	
	print('\n**************************************************************************************************')
	print('***                                                                                            ***')
	print('***                                    开始自动更新所有的升级包                                  ***')
	print('***                                                                                            ***')
	print('**************************************************************************************************')
	
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

if __name__ == "__main__":
    main()
