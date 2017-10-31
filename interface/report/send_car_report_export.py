#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class SendCarReportExport(object):
    '''
    发车综合报表导出
    /api/tms/report/exportSendCarReport
    '''
    __slots__ = ('__sendCarReportExportApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__sendCarReportExportApiUrl = "https://{0}:{1}{2}/api/tms/report/exportSendCarReport".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def send_car_report_export(self,carType ='',project='',supplier='',sendCarDateStart='',sendCarDateEnd='',
                               sendCity='',arriveCity=''):
         '''发车综合报表导出'''
         try:
             payload ={
                 'carType': carType,
                 'project': project,
                 'supplier': supplier,
                 'sendCarDateStart': sendCarDateStart,
                 'sendCarDateEnd': sendCarDateEnd,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,

             }
             response = HttpClient().post_json(self.__sendCarReportExportApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None