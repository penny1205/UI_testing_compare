#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import random
import time
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.report.outcar_price_report_export import OutCarPriceReportExport

class TestOutCarPriceReportExport(unittest.TestCase):
    '''外请车价监控报表导出'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestOutCarPriceReportExport START ########################')
        self.startDate = time.strftime('%Y-%m-%d', time.localtime(time.time() - 2592000))
        self.endDate = time.strftime('%Y-%m-%d')
        self.dataType = random.choice(['week', 'day', 'month'])

    def tearDown(self):
        self.logger.info('######################## TestOutCarPriceReportExport END #########################')


    def test_outCar_price_report_export_success(self):
        '''外请车价监控报表导出'''
        response = OutCarPriceReportExport().outCar_price_report_export(startDate=self.startDate,endDate=self.endDate,
                                                            sendCity='杭州',arriveCity='合肥',dataType=self.dataType)
        self.logger.info('外请车价监控报表导出返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        filename = FileUtil.getProjectObsPath() + os.path.sep + 'file' + os.path.sep + 'outCar_price_report_export.xlsx'
        with open(filename, 'wb') as writeIn:
            writeIn.write(response.content)
        self.logger.info('外请车价监控报表导出文件是：{0}'.format(filename))

if __name__ == '__main__':
    unittest.main()