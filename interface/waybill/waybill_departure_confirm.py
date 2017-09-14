#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillDepartureConfirm(object):
    '''
    发车确认
    /payment/tmsConfirmWayBill
    '''
    __slots__ = ('__departureConfirmWayBillApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__departureConfirmWayBillApiUrl = 'http://{0}:{1}{2}/payment/tmsConfirmWayBill'.format(
            config['app_api_host'],config['app_api_port'],config['app_api_path'])
        self.__head_dict = {
            'content-type': "application/json",
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_departure_confirm(self,billId=''):
        '''发车确认'''
        try:
            payload ={ 'billId':billId}
            response = HttpClient().post_json(self.__departureConfirmWayBillApiUrl,payload,self.__head_dict)
            return response
        except Exception:
            return None