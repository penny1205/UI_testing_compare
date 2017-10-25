#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class LoanSelect(object):
    '''
    获取大额放款申请的列表
    /api/tms/loan/listLargerLoan
    '''
    __slots__ = ('__loanSelectApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__loanSelectApiUrl = 'https://{0}:{1}{2}/api/tms/loan/listLargerLoan'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def loan_select(self,currentPage='1',rows='10',createDate='',demandLoanDate='',loanAmount=''):
         '''获取大额放款申请的列表'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'partnerNo': self.partnerNo,
                 'createDate': createDate,         # 创建时间
                 'demandLoanDate': demandLoanDate, # 放款时间
                 'loanAmount': loanAmount,         # 放款金额
             }
             response = HttpClient().get(self.__loanSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None