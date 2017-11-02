import os
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_temp_get import WayBillTempGet
from interface.waybill.waybill_temp_update import WayBillTempUpdate
from bvt.common.settings import Settings
from bvt.common.create_waybill import CreateWayBill

class TestWayBillTempUpdate(unittest.TestCase):
    '''根据ID修改临时运单'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('##################### TestWayBillTempUpdate START #####################')
        Settings().system_params_update()
        file = FileUtil.getProjectObsPath() + os.path.sep + 'file' + os.path.sep + 'waybill_temp_import.xlsx'
        self.logger.info('批量导入运单的文件是：{0}'.format(file))
        self.temp_waybillId = CreateWayBill().create_temp_waybill(file, '德邦物流', '德邦集团', 'DB20171101100')

    def tearDown(self):
        self.logger.info('##################### TestWayBillTempUpdate END #######################')

    def test_waybill_temp_update_success(self):
        '''根据ID修改临时运单'''
        temp_waybill = WayBillTempGet().waybill_temp_get(self.temp_waybillId).json()['content']

        response = WayBillTempUpdate().waybill_temp_update(self.temp_waybillId ,temp_waybill['carType'],
                                                           temp_waybill['applyDate'],temp_waybill['projects'],
                                                           temp_waybill['projectId'],temp_waybill['supplierName'],
                                                           temp_waybill['name'], temp_waybill['idNo'],
                                                           temp_waybill['mobile'], temp_waybill['carNo'],
                                                           temp_waybill['carLength'], temp_waybill['carModel'],
                                                           temp_waybill['sendProvince'], temp_waybill['sendCity'],
                                                           temp_waybill['sendDistrict'], temp_waybill['arriveProvince'],
                                                           temp_waybill['arriveCity'], temp_waybill['arriveDistrict'],
                                                           temp_waybill['income'], temp_waybill['feeAmt'],
                                                           temp_waybill['cash'], temp_waybill['oilFee'],
                                                           temp_waybill['destAmt'], temp_waybill['retAmt'],
                                                           temp_waybill['hasReceipt'], temp_waybill['content'],
                                                           temp_waybill['cargoName'], temp_waybill['cargoWeight'],
                                                           temp_waybill['cargoVolume'], temp_waybill['cargoNumberOfCases'],
                                                           temp_waybill['cargoWorth'], temp_waybill['insuranceCosts'],
                                                           temp_waybill['handlingFee'], temp_waybill['deliveryFee'],
                                                           temp_waybill['oilCardDeposit'], temp_waybill['otherFee'],
                                                           temp_waybill['upWayBillId'], temp_waybill['oilCardNo'],
                                                           temp_waybill['vehicleIdNo'], temp_waybill['driverCardNo'],
                                                           '', '')
        self.logger.info('根据ID修改临时运单返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('根据ID修改临时运单返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()