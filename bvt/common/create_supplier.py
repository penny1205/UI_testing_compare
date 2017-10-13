#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.supplier_create import SupplierCreate

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
            #现在接口名称可以重复
            return response.json()['content']
        except Exception:
            return None