#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class OutCarPriceReportSelect(object):
    '''
    外请车价监控报表查询
    /api/tms/report/outCarPriceReport
    '''
    __slots__ = ('__outCarPriceReportSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__outCarPriceReportSelectApiUrl = "https://{0}:{1}{2}/api/tms/report/outCarPriceReport".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def outCar_price_report_select(self,currentPage='1',rows='10',startDate='',endDate='',
                                    sendCity='',arriveCity='',carLength='',dataType=''):
         '''外请车价监控报表查询'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'startDate': startDate,
                 'endDate': endDate,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'carLength': carLength,
                 'dataType':dataType,
             }
             response = HttpClient().get(self.__outCarPriceReportSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None