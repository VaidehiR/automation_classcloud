import unittest
import HTMLTestRunner
import os
import student
import setting

class MainTestRunner(unittest.TestCase):

    def test_student_flow(self):

        student_flow_suite = unittest.TestSuite()
        student_flow_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromModule(student)])
        outfile = open('/home/alqama/workspace/classcloud' +
                       '/studentflowReport.html', 'w')

        runner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='student flow test report'
        )

        runner.run(student_flow_suite)


if __name__ == '__main__':
    unittest.main()
