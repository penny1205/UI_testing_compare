#__author__ = 'pan'
# -*- coding:utf-8 -*-


from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class UserCreate(object):
    '''
    新增账号
    /api/tms/system/createTmsUser
    '''
    __slots__ = ('__userCreateApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__userCreateApiUrl = 'https://{0}:{1}{2}/api/tms/system/createTmsUser'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def user_create(self,roleId='',name='',userName='',mobile='',isLoginApp='',projectId='',carType=''):
         '''新增账号'''
         try:
             dataAuth = "{{'tableAuthList':[{{'name':'AppTransportCashModel','propAuthList':[{{'name':'projectId'," \
                        "'values':'{0}'}},{{'name':'carType','values':'{1}'}}]}},{{'name':'TmsProjectModel','propAuthList'" \
                        ":[{{'name':'projectId','values':'{1}'}}]}}]}}".format(projectId,carType)
             payload ={
                 'partnerNo': self.partnerNo,
                 'role':  roleId,
                 'name': name,
                 'userName': userName,
                 'mobile': mobile,
                 'isLoginApp': isLoginApp,
                 'dataAuth':dataAuth,
             }
             response = HttpClient().post_form(self.__userCreateApiUrl,None,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('新增账号发生异常:{0}'.format(e))
             return None