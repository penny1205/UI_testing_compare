#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillTempTemplateDownload(object):
    '''
    下载批量开单excel模板
    /api/tms/tmpWayBill/downloadTmpWayBillExcel
    '''
    __slots__ = ('__wayBillTempTemplateDownloadApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTempTemplateDownloadApiUrl = 'https://{0}:{1}{2}/api/tms/tmpWayBill/downloadTmpWayBillExcel'\
            .format(config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_temp_template_download(self):
         '''下载批量开单excel模板'''
         try:
             payload = {}
             response = HttpClient().post_form(self.__wayBillTempTemplateDownloadApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None
