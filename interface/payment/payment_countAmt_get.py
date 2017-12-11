# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class CountAmtGet(object):
    """ 待支付合计金额统计值获取
    /api/tms/pay/countAmt"""

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__getCountAmtApiUrl = "https://{0}:{1}{2}/api/tms/pay/countAmt".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def count_amt_get(self, countName, applyDateFirst='', applyDateLast='', sendCity='', arriveCity='', carNo='',
                      driverName='', isCanLoan=''):
        try:
            payload = {
                "countName": countName,  # 需统计的金额：amtFee 总运费，cash 预付款，oilFee 油卡，destAmtConfirm 到付金额，retAmtConfirm 尾款金额
                "applyDateFirst": applyDateFirst,  # 用车日期查询开始
                "applyDateLast": applyDateLast,    # 用车日期查询截止
                "sendCity": sendCity,              # 出发城市
                "arriveCity": arriveCity,          # 到达城市
                "carNo": carNo,                    # 车牌号
                "driverName": driverName,          # 司机姓名
                "isCanLoan": isCanLoan             # 是否可贷款，1：可贷款，0：不可贷款
            }
            response = HttpClient().get(self.__getCountAmtApiUrl, self.__head_dict, payload)
            return response
        except Exception as e:
            Log().error('待支付合计金额统计值获取发生异常:{0}'.format(e))
            return None

if __name__ == '__main__':
    test = CountAmtGet().count_amt_get('cash')
    print(test.json())
