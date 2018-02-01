#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.supplier_create import SupplierCreate
from interface.driver.supplier_select import SupplierSelect
from interface.driver.supplier_delete import SupplierDelete

class CreateSupplier(object):
    '''供应商 新增供应商'''

    def __init__(self):
        self.logger = Log()

    def create_supplier(self,name,type,contactPersonName,contactPersonMobile,contactPersonIdNo,
                        contactPersonIdCardPhoto,businessLicencePhoto,businessPermitPhoto,
                        taxRegistrationCertificatePhoto,contractPhoto):
        '''供应商 新增供应商'''
        try:
            response = SupplierCreate().supplier_create(name=name,type=type,contactPersonName=contactPersonName,
                        contactPersonMobile = contactPersonMobile,contactPersonIdNo=contactPersonIdNo,
                        contactPersonIdCardPhoto=contactPersonIdCardPhoto,businessLicencePhoto=businessLicencePhoto,
                        businessPermitPhoto=businessPermitPhoto,
                        taxRegistrationCertificatePhoto=taxRegistrationCertificatePhoto,contractPhoto=contractPhoto)
            self.logger.info('新增的供应商名称是: {0},供应商性质是:{1}'.format(name,type))
            #判断供应商名称是否重复
            if response.json()['code'] == 0:
                return response.json()['content']
            elif response.json()['code'] == 907002:
                supplier_list = SupplierSelect().supplier_select(name=name).json()['content']['dataList']
                for supplier in supplier_list:
                    SupplierDelete().supplier_delete(supplier['supplierId'])
                response_ = SupplierCreate().supplier_create(name=name,type=type,contactPersonName=contactPersonName,
                        contactPersonMobile = contactPersonMobile,contactPersonIdNo=contactPersonIdNo,
                        contactPersonIdCardPhoto=contactPersonIdCardPhoto,businessLicencePhoto=businessLicencePhoto,
                        businessPermitPhoto=businessPermitPhoto,
                        taxRegistrationCertificatePhoto=taxRegistrationCertificatePhoto,contractPhoto=contractPhoto)
                return response_.json()['content']
        except Exception as e:
            self.logger.error('新增供应商发生异常:{0}'.format(e))
            return None