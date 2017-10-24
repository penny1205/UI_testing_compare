import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_temp_template_download import WayBillTempTemplateDownload


class TestWayBillTempTemplateDownload(unittest.TestCase):
    '''下载批量开单excel模板'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('##################### TestWayBillTempTemplateDownload START #####################')

    def tearDown(self):
        self.logger.info('##################### TestWayBillTempTemplateDownload END #######################')

    def test_waybill_temp_template_download_success(self):
        '''下载批量开单excel模板'''
        response = WayBillTempTemplateDownload().waybill_temp_template_download()
        filename = FileUtil.getProjectObsPath() + '/file/' + 'waybill_template_download.xlsx.'
        with open(filename, 'wb') as writeIn:
            writeIn.write(response.content)
        self.logger.info('下载批量开单excel模板返回状态码：{0}'.format(response))
        self.logger.info('下载批量开单excel模板文件是：{0}'.format(filename))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()