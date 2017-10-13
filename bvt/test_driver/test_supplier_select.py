#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.supplier_select import SupplierSelect
from bvt.common.create_supplier import CreateSupplier

class TestSupplierSelect(unittest.TestCase):
    '''查询供应商'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSupplierSelect START ###########################')
        self.name = '哇哈哈集团'
        self.contactPersonMobile = DataUtil().createmoble()
        self.contactPersonIdNo = DataUtil().genneratorIdNo()
        self.contactPersonIdCardPhoto = "http://yudian.ufile.ucloud.com.cn/18d4d203-3712-43c7-93d9-9b791aa4806d.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=CGRGouKFXGdBh3aI4+gK+nA5XmU="
        self.businessLicencePhoto = "http://yudian.ufile.ucloud.com.cn/9503b68e-6e0b-40df-b30f-c7af545da878.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=42hC+hmiXMNbRIoR8H4wipW0SI8="
        self.businessPermitPhoto = "http://yudian.ufile.ucloud.com.cn/8539002d-b90f-4a1a-b19c-22b2135cbf6b.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=hwTz+Pk8yffBXUwEbgSsoVU9QT4="
        self.taxRegistrationCertificatePhoto = "http://yudian.ufile.ucloud.com.cn/b117b5e1-e4d5-47f6-8e81-50bb344c3896.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=4+YLofibFNAqF1PhOFoNSqu4CN4="
        self.contractPhoto = "http://yudian.ufile.ucloud.com.cn/b2098698-56e7-425e-9186-61dbb966310a.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=IknyOZi+hHvHpyajfp8HI3aANqA="
        self.supplierId = CreateSupplier().create_supplier(self.name, '1', '李经理', self.contactPersonMobile,
                                                      self.contactPersonIdNo, self.contactPersonIdCardPhoto,
                                                      self.businessLicencePhoto,
                                                      self.businessPermitPhoto, self.taxRegistrationCertificatePhoto,
                                                      self.contractPhoto)

    def tearDown(self):
        self.logger.info('############################ TestSupplierSelect END ############################')

    def test_supplier_select_name_success(self):
        '''按供应商名称查询'''
        response = SupplierSelect().supplier_select(name= self.name)
        self.logger.info('按供应商名称查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('按供应商名称查询返回：{0}'.format(response.json()))
        supplier_list = response.json()['content']['dataList']
        if supplier_list != []:
            L = []
            for supplier in supplier_list:
                L.append(str(supplier['supplierId']))
            self.assertIn(self.supplierId, L, 'supplier selected fail!')
        else:
            self.logger.error('Please check the results of the supplier for empty!')


if __name__ == '__main__':
    unittest.main()