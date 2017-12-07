#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MyCarSelect(object):
    '''
    我的车辆列表
    /api/tms/car/listCars
    '''
    __slots__ = ('__myCarSelectApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myCarSelectApiUrl = "https://{0}:{1}{2}/api/tms/car/listCars".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_car_select(self,currentPage='1',rows='10',carNo='',carModel ='',carLength=''):
         '''我的车辆列表'''
         try:
             payload ={
             'currentPage': currentPage,
             'rows': rows,
             'carNo': carNo,
             'carModel': carModel,
             'carLength': carLength
             }
             response = HttpClient().get(self.__myCarSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('新增自有车发生异常:{0}'.format(e))
             return None