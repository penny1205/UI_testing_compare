from util.config.yaml.readyaml import ReadYaml
from util.http.httpclient import HttpClient
from util.file.fileutil import FileUtil

class WayBillDelete(object):
    __slots__ = ('__deleteWayBillApiUrl', '__token_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__deleteWayBillApiUrl = 'https://{0}:{1}{2}/api/tms/wayBill/createWayBill'.format(config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__token_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_cancel(self, wayBillId):
        try:
            delete_data_dict = {'billId': wayBillId, 'cancleReason': 'CancelByQaPythonTesting'}
            response = HttpClient().post_json(self.__deleteWayBillApiUrl, delete_data_dict, self.__token_dict)
            return response
        except Exception:
            return None