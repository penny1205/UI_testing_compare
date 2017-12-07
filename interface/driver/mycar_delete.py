#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MyCarDelete(object):
    '''
    删除自有车信息
   /api/tms/car/deleteCar
    '''
    __slots__ = ('__myCarDeleteApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myCarDeleteApiUrl = "https://{0}:{1}{2}/api/tms/car/deleteCar".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_car_delete(self,carId):
         '''删除自有车信息'''
         try:
             payload ={
                 'carId': carId,
             }
             response = HttpClient().post_form(self.__myCarDeleteApiUrl,payload,self.__head_dict,)
             return response
         except Exception as e:
             Log().error('删除自有车信息发生异常:{0}'.format(e))
             return None