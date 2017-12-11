#__author__ = 'pan'
# -*- coding:utf-8 -*-

import json
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class LineMileageMoreGet(object):
    '''
    计算线路中的里程数
    /api/tms/line/countLineMileage
    '''
    __slots__ = ('__lineMileageMoreGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__lineMileageMoreGetApiUrl = "https://{0}:{1}{2}/api/tms/line/countLineMileage".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def line_mileage_more_get(self,sendProvince='',sendCity='',sendDistrict='',stationAProvince='',stationACity='',
                              stationADistrict='',stationBProvince='',stationBCity='',stationBDistrict='',
                              arriveProvince ='',arriveCity ='',arriveDistrict='',):
         '''计算线路中的里程数'''

         cities = [{"province":sendProvince,"city":sendCity,"district":sendDistrict},
                   {"province":stationAProvince,"city":stationACity,"district":stationADistrict},
                   {"province":stationBProvince,"city":stationBCity,"district":stationBDistrict},
                   {"province": arriveProvince, "city": arriveCity, "district": arriveDistrict}]

         try:
             payload ={
                 'cities': json.dumps(cities),
             }
             response = HttpClient().get(self.__lineMileageMoreGetApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('计算线路中的里程数发生异常:{0}'.format(e))
             return None