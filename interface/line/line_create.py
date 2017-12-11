#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class LineCreate(object):
    '''
    创建线路
    /api/tms/line/createLine
    '''
    __slots__ = ('__lineCreateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__lineCreateApiUrl = "https://{0}:{1}{2}/api/tms/line/createLine".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def line_create(self,sendProvince='',sendCity='',sendDistrict='',arriveProvince ='',arriveCity ='',arriveDistrict='',
                    stationAProvince='',stationACity='',stationADistrict='',stationBProvince='',stationBCity='',
                    stationBDistrict='',mileage='',arriveTime='',projectId=''):
         '''创建线路'''
         try:
             payload ={
                 'sendProvince': sendProvince,
                 'sendCity': sendCity,
                 'sendDistrict': sendDistrict,
                 'arriveProvince': arriveProvince,
                 'arriveCity': arriveCity,
                 'arriveDistrict': arriveDistrict,
                 'mileage': mileage,
                 'arriveTime': arriveTime,
                 'projectId': projectId,
                 'stationAProvince' : stationAProvince,
                 'stationACity' : stationACity,
                 'stationADistrict' : stationADistrict,
                 'stationBProvince': stationBProvince,
                 'stationBCity' : stationBCity,
                 'stationBDistrict' : stationBDistrict
             }
             response = HttpClient().post_json(self.__lineCreateApiUrl,payload,self.__head_dict)
             return response
         except Exception as e:
             Log().error('创建线路发生异常:{0}'.format(e))
             return None