#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillDeletedEmpty(object):
    '''
    清空/恢复回收站
    /api/tms/wayBill/updateDelWayBillList
    '''
    __slots__ = ('__wayBillDeletedEmptyApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillDeletedEmptyApiUrl = "https://{0}:{1}{2}/api/tms/wayBill/updateDelWayBillList".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_deleted_empty(self,updateType=''):
         '''清空/恢复回收站'''
         try:
             payload ={
                 'updateType': updateType,
             }
             response = HttpClient().post_form(self.__wayBillDeletedEmptyApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None

