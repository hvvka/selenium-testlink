import os
from datetime import datetime
from pprint import pprint
from unittest import (
    TestLoader,
    TextTestResult,
    TextTestRunner)

import testlink

from test_module import *

# args = ["python", "test_module.py"]
# subprocess.call(args)
# tls.reportTCResult(a_TestCaseID, a_TestPlanID, 'a build name', 'f', 'some notes', user='a user login name', platformid=a_platformID)

# https://www.reddit.com/r/learnpython/comments/28eoz9/python_unittest_do_something_different_if_test/


# suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
# out = unittest.TextTestRunner(verbosity=2).run(suite)
# print (out)

OK = 'ok'
FAIL = 'fail'
ERROR = 'error'
SKIP = 'skip'


class JsonTestResult(TextTestResult):

    def __init__(self, stream, descriptions, verbosity):
        super_class = super(JsonTestResult, self)
        super_class.__init__(stream, descriptions, verbosity)

        # TextTestResult has no successes attr
        self.successes = []

    def addSuccess(self, test):
        # addSuccess do nothing, so we need to overwrite it.
        super(JsonTestResult, self).addSuccess(test)
        self.successes.append(test)

    def json_append(self, test, result, out):
        suite = test.__class__.__name__
        if suite not in out:
            out[suite] = {OK: [], FAIL: [], ERROR: [], SKIP: []}
        if result is OK:
            out[suite][OK].append(test._testMethodName)
        elif result is FAIL:
            out[suite][FAIL].append(test._testMethodName)
        elif result is ERROR:
            out[suite][ERROR].append(test._testMethodName)
        elif result is SKIP:
            out[suite][SKIP].append(test._testMethodName)
        else:
            raise KeyError("No such result: {}".format(result))
        return out

    def jsonify(self):
        json_out = dict()
        for t in self.successes:
            json_out = self.json_append(t, OK, json_out)

        for t, _ in self.failures:
            json_out = self.json_append(t, FAIL, json_out)

        for t, _ in self.errors:
            json_out = self.json_append(t, ERROR, json_out)

        for t, _ in self.skipped:
            json_out = self.json_append(t, SKIP, json_out)

        return json_out


if __name__ == '__main__':
    # redirect default output of unittest to /dev/null
    with open(os.devnull, 'w') as null_stream:
        # new a runner and overwrite resultclass of runner
        runner = TextTestRunner(stream=null_stream)
        runner.resultclass = JsonTestResult

        # create a testsuite
        suite = TestLoader().loadTestsFromTestCase(TestSimple)

        # run the testsuite
        result = runner.run(suite)

        # print json output
        pprint(result.jsonify())

        TESTLINK_API_PYTHON_SERVER_URL = "http://192.168.43.83/lib/api/xmlrpc/v1/xmlrpc.php"
        TESTLINK_API_PYTHON_DEVKEY = "e5d71d849a10dd9722437d407f79c549"

        # tls = testlink.TestLinkHelper( TESTLINK_API_PYTHON_SERVER_URL, TESTLINK_API_PYTHON_DEVKEY).connect(testlink.TestlinkAPIClient)

        tlh = testlink.TestLinkHelper(TESTLINK_API_PYTHON_SERVER_URL, TESTLINK_API_PYTHON_DEVKEY)
        tls = testlink.TestlinkAPIClient(tlh._server_url, tlh._devkey, verbose=True)
        print(tls.countProjects())

        tc_info = tls.getTestCase(None, testcaseexternalid='SE-1')
        print(tc_info)
        tc_info = tls.getProjectTestPlans('1')
        print("Plan ID: %s" % tc_info)
        # tls.reportTCResult(4, 7, 'Build', 'f', 'some notes', user='user', platformid='1')

        test_result = 'p'
        if result.jsonify()["TestSimple"]["error"]:
            test_result = 'f'
        print(test_result)

        tls.reportTCResult(None, 7, None, test_result, 'some notes', guess=True,
                           testcaseexternalid='SE-1',
                           platformname='NewPlatform',
                           execduration=3.9, timestamp=str(datetime.now().strftime("%Y-%m-%d %H:%M")),
                           steps=[{'step_number': 1, 'result': 'p', 'notes': 'result note for passed step 1'},
                                  {'step_number': 2, 'result': 'p', 'notes': 'result note for passed step 2'}]
                           )
