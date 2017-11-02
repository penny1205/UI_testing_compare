#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillTempCreate(object):
    '''
    生成运单
    /api/tms/tmpWayBill/batchCreateTmpWayBill
    '''
    __slots__ = ('__wayBillTempCreateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTempCreateApiUrl = 'https://{0}:{1}{2}/api/tms/tmpWayBill/batchCreateTmpWayBill'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_temp_create(self,wayBillIds='',replaceIds=''):
         '''生成运单'''
         try:

             payload = {
                 'ids': wayBillIds,         # 临时运单IDs，必须为"1,2,3"样式整数字符串，必填
                 'replaceIds': replaceIds,
             }
             response = HttpClient().post_form(self.__wayBillTempCreateApiUrl,payload,self.__head_dict,payload)
             return response
         except Exception:
             return None
