from util.config.yaml.readyaml import ReadYaml
from util.http.httpclient import HttpClient
from util.file.fileutil import FileUtil


class WayBillTrackingTrajectoryCreate(object):
    '''
    添加跟踪备注信息
    /api/tms/wayBill/createManualTrajectory
    '''
    __slots__ = ('__wayBillTrackingTrajectoryCreateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTrackingTrajectoryCreateApiUrl = 'https://{0}:{1}{2}/api/tms/wayBill/createManualTrajectory'.\
            format(config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_tracking_trajectory_create(self, wayBillId='',address=''):
        '''添加跟踪备注信息'''
        try:
            payload = {
                'wayBillId': wayBillId,  # 运单号，必填,
                'address':address,
            }
            response = HttpClient().post_json(self.__wayBillTrackingTrajectoryCreateApiUrl, payload, self.__head_dict)
            return response
        except Exception:
            return None