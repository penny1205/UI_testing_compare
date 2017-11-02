#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import time
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.report.profit_report_export import ProfitReportExport

class TestProfitReportExport(unittest.TestCase):
    '''利润报表信息列表导出'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestProfitReportExport START ########################')
        self.sendDateStart = time.strftime('%Y-%m-%d', time.localtime(time.time() - 2592000))
        self.sendDateEnd = time.strftime('%Y-%m-%d')

    def tearDown(self):
        self.logger.info('######################## TestProfitReportExport END #########################')


    def test_profit_report_export_success(self):
        '''利润报表信息列表导出'''
        response = ProfitReportExport().profit_report_export(sendDateStart=self.sendDateStart,sendDateEnd=self.sendDateEnd)
        self.logger.info('利润报表信息列表导出返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        filename = FileUtil.getProjectObsPath()+ os.path.sep + 'file' + os.path.sep + 'profit_report_export.xlsx'
        with open(filename, 'wb') as writeIn:
            writeIn.write(response.content)
        self.logger.info('利润报表信息列表导出文件是：{0}'.format(filename))

if __name__ == '__main__':
    unittest.main()