import os
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_temp_check import WayBillTempCheck
from bvt.common.settings import Settings
from bvt.common.create_waybill import CreateWayBill

class TestWayBillTempCheck(unittest.TestCase):
    '''验证外请车运单信息'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('##################### TestWayBillTempCheck START #####################')
        Settings().system_params_update()
        file = FileUtil.getProjectObsPath() + os.path.sep + 'file' + os.path.sep + 'waybill_temp_import.xlsx'
        self.logger.info('批量导入运单的文件是：{0}'.format(file))
        self.temp_waybillId = CreateWayBill().create_temp_waybill(file, '德邦物流', '德邦集团', 'DB20171101100')

    def tearDown(self):
        self.logger.info('##################### TestWayBillTempCheck END #######################')

    def test_waybill_temp_check_success(self):
        '''验证外请车运单信息'''
        response = WayBillTempCheck().waybill_temp_check(self.temp_waybillId)
        self.logger.info('验证外请车运单信息返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('验证外请车运单信息返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()