import unittest
from interface.waybill.waybill_delete import WayBillDelete


class DeleteWayBillCase(unittest.TestCase):
    def setUp(self):
        self.wayBillId = '123456'
        pass

    def tearDown(self):
        pass

    # '''ddt demo'''
    # from parameterized import parameterized
    # from biz.waybill.mockparamsdata import MockParamsData
    # @parameterized.expand(MockParamsData.generate(1))
    def test_bvt_normal_delete(self):
        response = WayBillDelete().waybill_delete(self.wayBillId)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
