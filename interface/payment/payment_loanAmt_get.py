# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class LoanAmtGet(object):
    """ 可借款金额统计值获取
    [/api/tms/pay/LoanAmt][get]"""

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__getLoanAmtApiUrl = "https://{0}:{1}{2}/api/tms/pay/LoanAmt".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def loan_amt_get(self):
        try:
            response = HttpClient().get(self.__getLoanAmtApiUrl, self.__head_dict)
            return response
        except Exception:
            return None

if __name__ == '__main__':
    test = LoanAmtGet().loan_amt_get()
    print(test.json())
