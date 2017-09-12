import unittest
from interface.waybill.waybill_cancel import WayBillCancel


class CancelWayBill_BvtCase(unittest.TestCase):
    def setUp(self):
        self.wayBillId = '123456'
        pass

    def tearDown(self):
        pass

    def test_normal_cancel(self):
        response = WayBillCancel().waybill_cancel(self.wayBillId)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
