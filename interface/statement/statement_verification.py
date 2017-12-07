#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class StatementVerification(object):
    '''
    客户/供应商对账单核销确认
    /api/tms/finance/verificationWayBills
    '''
    __slots__ = ('__statementVerificationApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__statementVerificationApiUrl = "https://{0}:{1}{2}/api/tms/finance/verificationWayBills".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def statement_verification(self,billType='',wayBillIds=''):
         '''客户/供应商对账单核销确认'''
         try:
             payload ={
                 'billType': billType,
                 'wayBillIds': wayBillIds,         #运单id，必填
             }
             response = HttpClient().post_json(self.__statementVerificationApiUrl,payload,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('客户/供应商对账单导出发生异常:{0}'.format(e))
             return None