#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from util.db.dbutil import DBUtil
from util.file.fileutil import FileUtil
from util.config.yaml.readyaml import ReadYaml
from interface.settings.system_params_settings_update import SystemParamsSettingsUpdate


class Settings(object):
    '''系统设置'''

    def __init__(self):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()

    def system_params_update(self):
        '''更新系统属性配置信息'''
        try:
            cargoParamsSet = '{"hasCargoName":true,"cargoNameRequired":true,"hasCargoWeight":true,"cargoWeightRequired":true,"hasCargoVolume":true,"cargoVolumeRequired":true,"hasCargoNumberOfCases":true,"cargoNumberRequired":true,"hasCargocargoWorth":true,"cargoWorthRequired":true,"hasInsuranceCosts":true,"insuranceCostsRequired":true,"hasUpWayBillId":true,"upWayBillIdRequired":true,"hasOilCardNo":true,"oilCardNoRequired":true}'
            userDefinedFee = '{"hasHandlingFee":true,"hasDeliveryFee":true,"hasOilCardDeposit":true,"hasOtherFee":true}'
            carParamsSet = '{"hasDriverCardNo":true,"driverCardNoRequired":true,"hasVehicleIdNo":true,"vehicleIdNoRequired":true,"driverCardBankRequired":true,"hasDriverCardBank":true,"accountNameRequired":true,"hasAccountName":true}'
            userDefinedFunction = '{"authTodelWayBill":true}'
            SystemParamsSettingsUpdate().system_params_settings_update(cargoParamsSet,userDefinedFee,carParamsSet,userDefinedFunction)
        except Exception:
            raise

    def system_params_init_update(self):
        '''初始化系统属性配置信息'''
        try:
            cargoParamsSet = '{"hasDriverCardNo":false,"driverCardNoRequired":false,"hasVehicleIdNo":false,"vehicleIdNoRequired":false,"hasDriverCardBank":false,"driverCardBankRequired":false}"'
            userDefinedFee = '{"hasHandlingFee":false,"hasDeliveryFee":false,"hasOilCardDeposit":false,"hasOtherFee":false}'
            carParamsSet = '{"hasDriverCardNo":false,"driverCardNoRequired":false,"hasVehicleIdNo":false,"vehicleIdNoRequired":false,"driverCardBankRequired":false,"hasDriverCardBank":false,"accountNameRequired":false,"hasAccountName":false}'
            userDefinedFunction = '{"authTodelWayBill":false}'
            SystemParamsSettingsUpdate().system_params_settings_update(cargoParamsSet, userDefinedFee, carParamsSet,
                                                                       userDefinedFunction)
        except Exception:
            raise