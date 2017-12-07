#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MyCarCreate(object):
    '''
    新增自有车
    /api/tms/car/createCar
    '''
    __slots__ = ('__myCarCreateApiUrl','partnerNo','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myCarCreateApiUrl = "https://{0}:{1}{2}/api/tms/car/createCar".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_car_create(self,carNo='',carModel='',carLength='',carLoad ='',carAge='',buycarTime='',
                      carBrand='',photoDriverCard='',photoCar=''):
         '''新增自有车'''
         try:
             payload ={

                 'carNo': carNo,
                 'carModel': carModel,
                 'carLength': carLength,
                 'carLoad': carLoad,
                 'carAge': carAge,
                 'buycarTime': buycarTime,
                 'carBrand': carBrand,
                 'photoDriverCard': photoDriverCard,
                 'photoCar':photoCar,
                 'partnerNo':self.partnerNo,
             }
             response = HttpClient().post_json(self.__myCarCreateApiUrl,payload,self.__head_dict)
             return response
         except Exception as e:
             Log().error('新增自有车发生异常:{0}'.format(e))
             return None