#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MyCarImport(object):
    '''
    导入自有车辆
   /api/tms/car/importExcel
    '''
    __slots__ = ('__myCarImportApiUrl','partnerNo','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myCarImportApiUrl = "https://{0}:{1}{2}/api/tms/car/importExcel".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_car_import(self,file=''):
         '''导入自有车辆'''
         try:
             if file != '':
                 with open(file, 'rb') as f:
                    file = f.read()

             files ={
                 'file': (None,file),
                 'partnerNo':self.partnerNo,
             }
             response = HttpClient().post_multipart(self.__myCarImportApiUrl,files,self.__head_dict)
             return response
         except Exception as e:
             Log().error('导入自有车辆发生异常:{0}'.format(e))
             return None