#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillTempGet(object):
    '''
    根据ID查询临时运单
    /api/tms/tmpWayBill/getTmpWayBillById
    '''
    __slots__ = ('__wayBillTempGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTempGetApiUrl = 'https://{0}:{1}{2}/api/tms/tmpWayBill/getTmpWayBillById'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_temp_get(self,wayBillId=''):
         '''根据ID查询临时运单'''
         try:

             payload = {
                 'id': wayBillId,         #临时运单ID，整数数字，必填；
             }
             response = HttpClient().get(self.__wayBillTempGetApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('根据ID查询临时运单发生异常:{0}'.format(e))
             return None

