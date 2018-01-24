# #__author__ = 'pan'
# # -*- coding:utf-8 -*-
#
# import os
# import time
# import unittest
# from util.log.log import Log
# from util.file.fileutil import FileUtil
# from interface.report.send_car_report_export import SendCarReportExport
#
# class TestSendCarReportExport(unittest.TestCase):
#     '''发车综合报表导出'''
#     def setUp(self):
#         self.logger = Log()
#         self.logger.info('######################## TestSendCarReportExport START ########################')
#         self.sendCarDateStart = time.strftime('%Y-%m-%d', time.localtime(time.time() - 2592000))
#         self.sendCarDateEnd = time.strftime('%Y-%m-%d')
#
#     def tearDown(self):
#         self.logger.info('######################## TestSendCarReportExport END #########################')
#
#
#     def test_send_car_report_export_success(self):
#         '''发车综合报表导出'''
#         response = SendCarReportExport().send_car_report_export(sendCarDateStart=self.sendCarDateStart,
#                                                                 sendCarDateEnd=self.sendCarDateEnd)
#         self.logger.info('发车综合报表导出返回状态码：{0}'.format(response))
#         self.assertEqual(response.status_code, 200)
#         filename = FileUtil.getProjectObsPath()+ os.path.sep + 'file' + os.path.sep + 'send_car_report_export.xlsx.'
#         with open(filename, 'wb') as writeIn:
#             writeIn.write(response.content)
#         self.logger.info('利润报表信息列表导出文件是：{0}'.format(filename))
#
# if __name__ == '__main__':
#     unittest.main()