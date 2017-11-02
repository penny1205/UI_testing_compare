#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
import os.path


class WayBillTempImport(object):
    '''
    批量导入运单
   /api/tms/tmpWayBill/importExcel
    '''
    __slots__ = ('__wayBillTempImportApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTempImportApiUrl = 'https://{0}:{1}{2}/api/tms/tmpWayBill/importExcel'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_temp_import(self, file=''):
         '''批量导入运单'''
         try:
             file_name = os.path.basename(file)
             file_type = os.path.splitext(file)[1]
             if file_type == '.xls':
                 file_content_type ='application/vnd.ms-excel'
             elif file_type == '.xlsx':
                 file_content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
             else:
                 file_content_type = ''

             files ={
                 'file': (file_name, open(file, 'rb'), file_content_type, {'Expires': '0'}),
                 'partnerNo': (None, str('ShiDeTang'))
             }
             response = HttpClient().post_multipart(self.__wayBillTempImportApiUrl,files,self.__head_dict)
             return response
         except Exception:
             return None