#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class LineSelect(object):
    '''
    线路时效维护列表
    /api/tms/line/listLine
    '''
    __slots__ = ('__lineSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__lineSelectApiUrl = "https://{0}:{1}{2}/api/tms/line/listLine".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def line_select(self,currentPage='1',rows='1000',projectId='',sendCity='',arriveCity='',
                    servicingTimeFirst='',servicingTimeLast=''):
         '''线路时效维护列表'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'projectId': projectId,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'servicingTimeFirst': servicingTimeFirst, #维护时间：开始时间"yyyy-MM-dd"
                 'servicingTimeLast': servicingTimeLast,   #维护时间：结束时间，格式为“yyyy-MM-dd”
             }
             response = HttpClient().get(self.__lineSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('线路时效维护列表生异常:{0}'.format(e))
             return None