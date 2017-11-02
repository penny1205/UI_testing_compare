import os
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_temp_get import WayBillTempGet
from bvt.common.settings import Settings
from bvt.common.create_waybill import CreateWayBill

class TestWayBillTempGet(unittest.TestCase):
    '''根据ID查询临时运单'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('##################### TestWayBillTempGet START #####################')
        Settings().system_params_update()
        file = FileUtil.getProjectObsPath() + os.path.sep + 'file' + os.path.sep + 'waybill_temp_import.xlsx'
        self.logger.info('批量导入运单的文件是：{0}'.format(file))
        self.temp_waybillId = CreateWayBill().create_temp_waybill(file, '德邦物流', '德邦集团', 'DB20171101100')

    def tearDown(self):
        self.logger.info('##################### TestWayBillTempGet END #######################')

    def test_waybill_temp_get_success(self):
        '''根据ID查询临时运单'''
        response = WayBillTempGet().waybill_temp_get(self.temp_waybillId)
        self.logger.info('根据ID查询临时运单返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('根据ID查询临时运单结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()