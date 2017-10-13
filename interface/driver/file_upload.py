#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class FileUpload(object):
    '''
    上传图片
    /api/tms/upload/uploadFile
    '''
    __slots__ = ('__fileUploadApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__fileUploadApiUrl = "https://{0}:{1}{2}/api/tms/upload/uploadFile".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def file_upload(self,photoDriverCard='',photoCar=''):
         '''上传图片'''
         try:
             if photoDriverCard != '':
                 with open(photoDriverCard, 'rb') as f:
                     photoDriverCard = f.read()

             if photoCar != '':
                 with open(photoCar, 'rb') as f:
                     photoCar = f.read()

             payload ={
                 "photoDriverCard":(None, str(photoDriverCard)),
                 "photoCar":(None, str(photoCar)),

             }
             response = HttpClient().post_multipart(self.__fileUploadApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None