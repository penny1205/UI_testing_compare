#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class LoanUpdate(object):
    '''
    修改大额贷款记录
    /api/tms/loan/createLoan
    '''
    __slots__ = ('__loanUpdateApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__loanUpdateApiUrl = 'https://{0}:{1}{2}/api/tms/loan/createLoan'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def loan_update(self,Id='',loanAmount='',recipientName='',recipientAccount='',depositBank='',remarks='',
                    demandLoanDate=''):
         '''修改大额贷款记录'''
         try:
             payload ={
                 'id': Id,
                 'loanAmount': loanAmount,              # 贷款金额，
                 'loanCustomer': self.partnerNo,        # 贷款客户，
                 'recipientName': recipientName,        # 收款户名，
                 'recipientAccount': recipientAccount,  # 收款账号，
                 'depositBank': depositBank,            # 开户行，
                 'remarks': remarks,                    # 备注信息，
                 'partnerNo': self.partnerNo,           # 物流公司标识，
                 'demandLoanDate': demandLoanDate,      # 需求放款日期，
             }
             response = HttpClient().post_json(self.__loanUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None