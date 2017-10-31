#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class OutCarPriceReportExport(object):
    '''
    外请车价监控报表导出
    /api/tms/report/exportOutPrice
    '''
    __slots__ = ('__outCarPriceReportExportApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__outCarPriceReportExportApiUrl = "https://{0}:{1}{2}/api/tms/report/exportOutPrice".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def outCar_price_report_export(self,startDate='',endDate='',sendCity='',arriveCity='',carType='',carLength='',
                                    dataType=''):
         '''外请车价监控报表导出'''
         try:
             payload ={
                 'startDate': startDate,
                 'endDate': endDate,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'carType': carType,
                 'carLength': carLength,
                 'dataType':dataType,
             }
             response = HttpClient().post_form(self.__outCarPriceReportExportApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None