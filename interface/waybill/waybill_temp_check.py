#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillTempCheck(object):
    '''
    验证外请车运单信息
    /api/tms/tmpWayBill/batchCheckTmpWayBill
    '''
    __slots__ = ('__wayBillTempCheckApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTempCheckApiUrl = 'https://{0}:{1}{2}/api/tms/tmpWayBill/batchCheckTmpWayBill'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_temp_check(self,wayBillIds=''):
         '''验证外请车运单信息单'''
         try:

             payload = {
                 'ids': wayBillIds,         # 临时运单IDs，必须为"1,2,3"样式整数字符串，必填
             }
             response = HttpClient().get(self.__wayBillTempCheckApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('验证外请车运单信息单发生异常:{0}'.format(e))
             return None
