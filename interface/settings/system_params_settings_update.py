#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class SystemParamsSettingsUpdate(object):
    '''
    运单拓展属性配置
   /api/tms/system/updateParamsSet
    '''
    __slots__ = ('__systemParamsSettingsUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__systemParamsSettingsUpdateApiUrl = "https://{0}:{1}{2}/api/tms/system/updateParamsSet".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def system_params_settings_update(self,cargoParamsSet,userDefinedFee,carParamsSet,userDefinedFunction):
         '''运单拓展属性配置'''
         try:
             # hasCargoName = '', hasCargoWeight = '', hasCargoVolume = '', hasCargoNumberOfCases = '',
             # hasCargocargoWorth = '', hasInsuranceCosts = '', hasUpWayBillId = '', hasOilCardNo = '',
             # cargoNameRequired = '', cargoWeightRequired = '', cargoVolumeRequired = '', cargoNumberRequired = '',
             # cargoWorthRequired = '', insuranceCostsRequired = '', upWayBillIdRequired = '', oilCardNoRequired = '',
             # hasHandlingFee = '', hasDeliveryFee = '', hasOilCardDeposit = '', hasOtherFee = '',
             # hasDriverCardNo = '', hasVehicleIdNo = '', driverCardNoRequired = '', vehicleIdNoRequired = '',
             # hasDepositBank = '', depositBankRequired = '', hasAccountName = '', accountNameRequired = '',
             # authToDelWayBill = ''

             # cargoParamsSet = "{'hasCargoName':{0},'hasCargoWeight':{1},'hasCargoVolume':{2},'hasCargoNumberOfCases':{3}," \
             #                  " 'hasCargocargoWorth':{4}, 'hasInsuranceCosts':{5}, 'hasUpWayBillId':{6}, " \
             #                  " 'hasOilCardNo':{7}, 'cargoNameRequired':{8},'cargoWeightRequired':{9}," \
             #                  " 'cargoVolumeRequired':{10},'cargoNumberRequired':{11}, 'cargoWorthRequired':{12}," \
             #                  " 'insuranceCostsRequired':{13}, 'upWayBillIdRequired':{14}, 'oilCardNoRequired':{15},}"\
             #     .format(hasCargoName,hasCargoWeight,hasCargoVolume,hasCargoNumberOfCases,hasCargocargoWorth,
             #             hasInsuranceCosts,hasUpWayBillId,hasOilCardNo,cargoNameRequired,cargoWeightRequired,
             #             cargoVolumeRequired,cargoNumberRequired,cargoWorthRequired,insuranceCostsRequired,
             #             upWayBillIdRequired,oilCardNoRequired)

             # userDefinedFee = "{'hasHandlingFee':{0},'hasDeliveryFee':{1},'hasOilCardDeposit':{2},'hasOtherFee':{3}}"\
             #     .format(hasHandlingFee,hasDeliveryFee,hasOilCardDeposit,hasOtherFee)
             #
             # carParamsSet = "{'hasDriverCardNo':{0},'hasVehicleIdNo':{1},'driverCardNoRequired':{2}," \
             #                "'vehicleIdNoRequired':{3},'hasDepositBank':{4},'depositBankRequired':{5}," \
             #                "'hasAccountName':{6},'accountNameRequired:{7}}".format(
             #     hasDriverCardNo,hasVehicleIdNo,driverCardNoRequired,vehicleIdNoRequired,hasDepositBank,
             #     depositBankRequired,hasAccountName,accountNameRequired
             #     )
             #
             # userDefinedFunction = "{'authToDelWayBill':{0}}".format(authToDelWayBill)

             payload ={
                 'cargoParamsSet': cargoParamsSet,
                 'userDefinedFee': userDefinedFee,
                 'carParamsSet': carParamsSet ,
                 'userDefinedFunction':userDefinedFunction,
             }
             response = HttpClient().post_json(self.__systemParamsSettingsUpdateApiUrl,payload,self.__head_dict,payload)
             return response
         except Exception:
             raise
             # return None