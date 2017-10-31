#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class ProfitReportExport(object):
    '''
    利润报表信息列表导出
    /api/tms/finance/exportProfitReportList
    '''
    __slots__ = ('__profitReportExportApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__profitReportExportApiUrl = "https://{0}:{1}{2}/api/tms/finance/exportProfitReportList".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def profit_report_export(self,vagueSearch ='',carType ='',carLength='',carModel='',
                               projectId='',sendDateStart='',sendDateEnd='',sendCity='',arriveCity=''):
         '''利润报表信息列表导出'''
         try:
             payload ={
                 'vagueSearch': vagueSearch,
                 'carType': carType,
                 'carLength': carLength,
                 'carModel': carModel,
                 'projectId': projectId,
                 'sendDateStart': sendDateStart,
                 'sendDateEnd': sendDateEnd,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
             }
             response = HttpClient().get(self.__profitReportExportApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None