# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class LoanAmtGet(object):
     '''
     可借款金额统计
     /api/tms/pay/LoanAmt
     '''
     __slots__ = ('__loanAmtGetApiUrl', '__head_dict')

     def __init__(self):
         config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
         self.__loanAmtGetApiUrl = 'https://{0}:{1}{2}/api/tms/pay/LoanAmt'.format(
             config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
         self.__head_dict = {
             'token': config['tms_api_token'],
             'YD_OAUTH': config['tms_api_YD_OAUTH'],
         }

     def loan_amt_get(self):
          '''可借款金额统计'''
          try:
              response = HttpClient().get(self.__loanAmtGetApiUrl,self.__head_dict)
              return response
          except Exception as e:
              Log().error('可借款金额统计接口调用异常:{0}'.format(e))
              return None
