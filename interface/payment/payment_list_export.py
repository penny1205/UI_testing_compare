# -*- coding:utf-8 -*-

import xlwt
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class PaymentListExport(object):
    """ 支付列表导出
    /api/tms/pay/exportPayList """

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__exportPayListApiUrl = "https://{0}:{1}{2}/api/tms/pay/exportPayList".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def payment_list_export(self, currentPage='', rows='', searchMode='', globalCondition='', sendCity='',
                                arriveCity='', carNo='', driverName='', applyDateFirst='2017-10-01', applyDateLast='2017-10-31', carType='',
                                amountType='', approveDateFirst='', approveDateLast='', paySchedule='', isLoan=''):
        """ 支付列表导出 """
        try:
            payload = {
                "searchMode": searchMode,  # global:全部字段模糊查询 general：普通条件查询
                "currentPage": currentPage,  # 当前页
                "rows": rows,  # 行数
                "globalCondition": globalCondition,  # 全部字段模糊查询条件
                "sendCity": sendCity,  # 出发城市
                "arriveCity": arriveCity,  # 到达城市
                "carNo": carNo,  # 车牌号
                "driverName": driverName,  # 司机姓名
                "applyDateFirst": applyDateFirst,  # 用车日期查询开始
                "applyDateLast": applyDateLast,  # 用车日期查询截止
                "carType": carType,  # 用车性质
                "amountType": amountType,  # 运费类型，cash - 预付款、oilFee - 油卡金额、destAmt - 到付款、retAmt - 尾款
                "approveDateFirst": approveDateFirst,  # 支付审批日期开始
                "approveDateLast": approveDateLast,  # 支付审批日期截止
                "paySchedule": paySchedule,  # 支付进度，UNPAID - 未支付、SUCCESS - 已支付、PAYING - 支付中、FAIL - 支付失败
                "isLoan": isLoan  # 是否贷款，1 - 是，0 - 否
            }
            response = HttpClient().post_json(self.__exportPayListApiUrl,
                                              header_dict=self.__head_dict, param_dict=payload)
            return response
        except Exception:
            return None

if __name__ == '__main__':
    test = PaymentListExport().payment_list_export()
    with open('E:/1.xlsx', 'wb') as writeIn:
        writeIn.write(test.content)
