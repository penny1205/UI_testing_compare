from util.config.yaml.readyaml import ReadYaml
from util.http.httpclient import HttpClient
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillWarn(object):
    '''
    运单预警
    /api/tms/wayBill/wayBillWarn
    '''
    __slots__ = ('__wayBillWarnApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillWarnApiUrl = 'https://{0}:{1}{2}/api/tms/wayBill/wayBillWarn'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_warn(self, wayBillId='',lat='',lng=''):
        '''运单预警'''
        try:
            payload = {
                'wayBillNo': str(wayBillId),  # 运单号，必填,
                'location': {
                    'lat':lat,           # 纬度，float类型的值,必填,
                    'lng':lng,           # 经度，float类型的值,必填,
                     },
            }
            response = HttpClient().post_json(self.__wayBillWarnApiUrl, payload, self.__head_dict)
            print(response.request.body,response.request.url)
            return response
        except Exception as e:
            Log().error('运单预警发生异常:{0}'.format(e))
            return None