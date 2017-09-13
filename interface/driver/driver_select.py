#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class DriverSelect(object):
    '''
    我的外请车列表
    /api/tms/driver/listTmsAppDriver
    接口调用：查询外请车、获取外请车列表、录单时按照司机、手机号查询我的外请车
    '''
    __slots__ = ('__selectDriverApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__selectDriverApiUrl = "https://{0}:{1}{2}/api/tms/driver/listTmsAppDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def driver_select(self,currentPage='1',rows='10',partnerNo='',mobile ='',name='',carNo=''):
         '''我的外请车列表'''
         try:
             payload ={
             'currentPage': currentPage,
             'rows': rows,
             'partnerNo': partnerNo,
             'name': name,
             'mobile': mobile,
             'carNo': carNo
             }
             request = HttpClient().get(self.__selectDriverApiUrl,self.__head_dict,payload)
             response = request.json()
             return response
         except Exception:
             return None
#          if response['code'] == 0:
#              return response['content']['dataList']
#          else:
#              self.logger.info('/api/tms/driver/listTmsAppDriver return status code error:{0}'.format(response))
#
# if __name__ == '__main__':
#     driver_list = DriverSelect().driver_select(currentPage='1', partnerNo='', rows='10')
#     print(driver_list)