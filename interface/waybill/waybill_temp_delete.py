#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillTempDelete(object):
    '''
    根据IDs批量删除临时运单
    /api/tms/tmpWayBill/batchDeleteTmpWayBillByIds
    '''
    __slots__ = ('__wayBillTempDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTempDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/tmpWayBill/batchDeleteTmpWayBillByIds'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_temp_delete(self,wayBillIds=''):
         '''根据IDs批量删除临时运单'''
         try:

             payload = {
                 'ids': wayBillIds,         # 临时运单IDs，必须为"1,2,3"样式整数字符串，必填
             }
             response = HttpClient().post_json(self.__wayBillTempDeleteApiUrl,payload,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('根据IDs批量删除临时运单发生异常:{0}'.format(e))
             return None
