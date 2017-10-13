#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class DriverRelevanceUpdate(object):
    '''
    修改外请车信息
    /api/tms/driver/updateTmsAppDriver
    '''
    __slots__ = ('__createDriverApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__createDriverApiUrl = 'https://{0}:{1}{2}/api/tms/driver/updateTmsAppDriver'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token']
        }

    def driver_relevance_update(self,loginId='', name='', mobile='', idNo='',photoIdFront='', photoIdReverse='',
                                photoDriverCard='',photoTransPort='',carNo='', carLength='', carModel='', carLoad=''):
        '''新增外请车'''

        try:
            if photoIdFront != '':
                with open(photoIdFront, 'rb') as f:
                    photoIdFront = f.read()

            if photoIdReverse != '':
                with open(photoIdReverse, 'rb') as f:
                    photoIdFront = f.read()

            if photoDriverCard != '':
                with open(photoDriverCard, 'rb') as f:
                    photoIdFront = f.read()

            if photoDriverCard != '':
                with open(photoDriverCard, 'rb') as f:
                    photoIdFront = f.read()

            files = {
                'loginId':(None, str(loginId)),
                'name': (None, str(name)),
                'mobile': (None, str(mobile)),
                'idNo': (None, str(idNo)),
                'photoIdFront': (None, photoIdFront),
                'photoIdReserve': (None, photoIdReverse),
                'photoDriverCard': (None, photoDriverCard),
                'photoTransPort': (None, photoTransPort),
                'carNo': (None, str(carNo)),
                'carLength': (None, str(carLength)),
                'carModel': (None, str(carModel)),
                'carLoad': (None, str(carLoad)),
            }
            response = HttpClient().post_multipart(self.__createDriverApiUrl, files, self.__head_dict)
            return response
        except Exception:
            return None
