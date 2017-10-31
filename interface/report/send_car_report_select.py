#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class SendCarReportSelect(object):
    '''
    发车综合报表分页查询
    /api/tms/report/sendCarReport
    '''
    __slots__ = ('__sendCarReportSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__sendCarReportSelectApiUrl = "https://{0}:{1}{2}/api/tms/report/sendCarReport".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def send_car_report_select(self,currentPage='1',rows='10',carType ='',project='',supplier='',sendCarDateStart='',
                               sendCarDateEnd='',sendCity='',arriveCity=''):
         '''发车综合报表分页查询'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'carType': carType,
                 'project': project,
                 'supplier': supplier,
                 'sendCarDateStart': sendCarDateStart,
                 'sendCarDateEnd': sendCarDateEnd,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,

             }
             response = HttpClient().get(self.__sendCarReportSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None