#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class DriverBankVINGet(object):
    '''
    根据外请车司机手机号获取银行卡号和车架号
    /api/tms/driver/getBankCardAndVehicleNo
    '''
    __slots__ = ('__driverBankVINGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverBankVINGetApiUrl = "https://{0}:{1}{2}/api/tms/driver/getBankCardAndVehicleNo".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def driver_bank_VIN_get(self,mobile=''):
         '''根据外请车司机手机号获取银行卡号和车架号'''
         try:
             payload = {'mobile': mobile,}
             response = HttpClient().get(self.__driverBankVINGetApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('根据外请车司机手机号获取银行卡号和车架号发生异常:{0}'.format(e))
             return None