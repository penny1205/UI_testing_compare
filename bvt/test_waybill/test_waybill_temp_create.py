import os
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_temp_check import WayBillTempCheck
from interface.waybill.waybill_temp_create import WayBillTempCreate
from bvt.common.settings import Settings
from bvt.common.create_waybill import CreateWayBill

class TestWayBillTempCreate(unittest.TestCase):
    '''生成运单'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('##################### TestWayBillTempCreate START #####################')
        Settings().system_params_update()
        file = FileUtil.getProjectObsPath() + os.path.sep + 'file' + os.path.sep + 'waybill_temp_import.xlsx'
        self.logger.info('批量导入运单的文件是：{0}'.format(file))
        self.temp_waybillId = CreateWayBill().create_temp_waybill(file, '德邦物流', '德邦集团', 'DB20171101100')

    def tearDown(self):
        self.logger.info('##################### TestWayBillTempCreate END #######################')

    def test_waybill_temp_create_success(self):
        '''生成运单'''
        temp_waybill_check = WayBillTempCheck().waybill_temp_check(self.temp_waybillId).json()['content']
        if temp_waybill_check != None:
            replaceIds = []
            for temp_waybill in temp_waybill_check:
                replaceIds.append(str(temp_waybill['id']))
        else:
            replaceIds = ''
        response = WayBillTempCreate().waybill_temp_create(self.temp_waybillId,','.join(replaceIds))
        self.logger.info('生成运单返回状态码：{0}'.format(response))
        self.logger.info('生成运单返回结果是：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)


if __name__ == '__main__':
    unittest.main()