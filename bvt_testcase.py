from util.unittest.unittestutil import UnitTestUtil
from util.report.reporting import ReportUtil
from util.file.fileutil import FileUtil
from util.mail.sendmail import SendMail

import time

if __name__ == '__main__':
    try:
        bvtcases = UnitTestUtil().discover_pattern(FileUtil.getProjectObsPath() + '/bvt/waybill', '*.py')
        ReportUtil().generate_report(bvtcases, 'TMS迭代BVT测试报告 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'qa testing report', FileUtil.getProjectObsPath() + '/report/report.html')
        reader = open(FileUtil.getProjectObsPath() + '/report/report.html', 'rb')
        mail_body = reader.read()
        reader.close()
        SendMail().send_mail(['zhangdawei@keking.cn', 'liuxinyu@keking.cn', 'panyuanyuan@keking.cn', 'qihong@keking.cn'],
                             'ahkj@keking.cn', 'redmineonly','mail.keking.cn',
                             'TMS迭代BVT测试报告 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), mail_body,
                             {FileUtil.getProjectObsPath() + '/report/report.html'})
    except Exception:
        raise
        print('BvtCase run fail!')