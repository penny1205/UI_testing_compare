#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class DriverCreate(object):
    '''
    新增外请车
    /api/tms/driver/createTmsAppDriver/all
    '''
    __slots__ = ('__driverCreateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverCreateApiUrl = 'https://{0}:{1}{2}/api/tms/driver/createTmsAppDriver/all'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token']
        }

    def driver_create(self, name='', mobile='', idNo='',photoIdFront='', photoIdReserve='', photoDriverCard='',
                      photoTransPort='',carNo='', carLength='', carModel='', carLoad=''):
        '''新增外请车'''

        try:
            if photoIdFront != '':
                with open(photoIdFront, 'rb') as f:
                    photoIdFront = f.read()

            if photoIdReserve != '':
                with open(photoIdReserve, 'rb') as f:
                    photoIdFront = f.read()

            if photoDriverCard != '':
                with open(photoDriverCard, 'rb') as f:
                    photoIdFront = f.read()

            if photoDriverCard != '':
                with open(photoDriverCard, 'rb') as f:
                    photoIdFront = f.read()

            files = {
                'name': (None, str(name)),
                'mobile': (None, str(mobile)),
                'idNo': (None, str(idNo)),
                'photoIdFront': (None, photoIdFront),
                'photoIdReserve': (None, photoIdReserve),
                'photoDriverCard': (None, photoDriverCard),
                'photoTransPort': (None, photoTransPort),
                'carNo': (None, str(carNo)),
                'carLength': (None, str(carLength)),
                'carModel': (None, str(carModel)),
                'carLoad': (None, str(carLoad)),
            }
            response = HttpClient().post_multipart(self.__driverCreateApiUrl, files, self.__head_dict)
            return response
        except Exception as e:
            Log().error('新增外请车发生异常:{0}'.format(e))
            return None
