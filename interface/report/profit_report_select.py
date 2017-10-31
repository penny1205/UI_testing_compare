#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class ProfitReportSelect(object):
    '''
    利润报表信息列表查询
    /api/tms/finance/getProfitReportList
    '''
    __slots__ = ('__profitReportSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__profitReportSelectApiUrl = "https://{0}:{1}{2}/api/tms/finance/getProfitReportList".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def profit_report_select(self,currentPage='1',rows='10',vagueSearch ='',carType ='',carLength='',carModel='',
                               projectId='',sendDateStart='',sendDateEnd='',sendCity='',arriveCity=''):
         '''利润报表信息列表查询'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'vagueSearch': vagueSearch,        # 模糊查询
                 'carType': carType,
                 'carLength': carLength,
                 'carModel': carModel,
                 'projectId': projectId,
                 'sendDateStart': sendDateStart,
                 'sendDateEnd': sendDateEnd,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
             }
             response = HttpClient().post_json(self.__profitReportSelectApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None