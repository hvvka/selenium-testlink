import os
from datetime import datetime
from pprint import pprint
from unittest import (
    TestLoader,
    TextTestRunner)

import testlink

from pythonorg import *
from run_test_module import JsonTestResult

OK = 'ok'
FAIL = 'fail'
ERROR = 'error'
SKIP = 'skip'

if __name__ == '__main__':
    # redirect default output of unittest to /dev/null
    with open(os.devnull, 'w') as null_stream:
        # new a runner and overwrite resultclass of runner
        runner = TextTestRunner(stream=null_stream)
        runner.resultclass = JsonTestResult

        # create a testsuite
        suite = TestLoader().loadTestsFromTestCase(PythonOrg)

        # run the testsuite
        result = runner.run(suite)

        # print json output
        pprint(result.jsonify())

        TESTLINK_API_PYTHON_SERVER_URL = "http://192.168.43.83/lib/api/xmlrpc/v1/xmlrpc.php"
        TESTLINK_API_PYTHON_DEVKEY = "e5d71d849a10dd9722437d407f79c549"

        tlh = testlink.TestLinkHelper(TESTLINK_API_PYTHON_SERVER_URL, TESTLINK_API_PYTHON_DEVKEY)
        tls = testlink.TestlinkAPIClient(tlh._server_url, tlh._devkey, verbose=True)
        print(tls.countProjects())

        tc_info = tls.getTestCase(None, testcaseexternalid='SE-3')
        print(tc_info)
        tc_info = tls.getProjectTestPlans('1')
        print("Plan ID: %s" % tc_info)

        test_result = 'p'
        if result.jsonify()["PythonOrg"]["error"]:
            test_result = 'f'
        print(test_result)

        tls.reportTCResult(None, 7, None, test_result, 'PythonOrg', guess=True,
                           testcaseexternalid='SE-3',
                           platformname='NewPlatform',
                           execduration=3.9, timestamp=str(datetime.now().strftime("%Y-%m-%d %H:%M")),
                           steps=[{'step_number': 1, 'result': 'p', 'notes': 'result note for passed step 1'},
                                  {'step_number': 2, 'result': 'p', 'notes': 'result note for passed step 2'},
                                  {'step_number': 3, 'result': 'p', 'notes': 'result note for passed step 3'},
                                  {'step_number': 4, 'result': 'p', 'notes': 'result note for passed step 4'},
                                  {'step_number': 5, 'result': 'p', 'notes': 'result note for passed step 5'}]
                           )
