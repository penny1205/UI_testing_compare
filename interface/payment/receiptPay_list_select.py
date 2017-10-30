# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class ReceiptPayListSelect(object):
    """ 回单支付列表查询 [/api/tms/pay/listReceiptPay][GET]"""

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__selectReceiptPayListApiUrl = "https://{0}:{1}{2}/api/tms/pay/listReceiptPay".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def receiptPay_list_select(self, currentPage='1', rows='10', applyDateFirst='', applyDateLast='', sendCity='',
                                 arriveCity='', carNo='', driverName='', isCanLoan=''):
        try:
            payload = {
                "currentPage": currentPage,        # 当前页
                "rows": rows,                      # 行数
                "applyDateFirst": applyDateFirst,  # 用车日期查询开始
                "applyDateLast": applyDateLast,    # 用车日期查询截止
                "sendCity": sendCity,              # 出发城市
                "arriveCity": arriveCity,          # 到达城市
                "carNo": carNo,                    # 车牌号
                "driverName": driverName,          # 司机姓名
                "isCanLoan": isCanLoan             # 是否可贷款，1：可贷款，0：不可贷款
            }
            response = HttpClient().get(self.__selectReceiptPayListApiUrl, self.__head_dict, payload)
            return response

        except Exception:
            return None

if __name__ == '__main__':
    test = ReceiptPayListSelect()
    print(test.receiptPay_list_select().json())