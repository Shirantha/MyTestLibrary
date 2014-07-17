# MyLibrary tests are here...

from selenium import webdriver
import unittest, os, shutil
import MyLibrary
#from lib import MyLibrary



class TestMyLibrary(unittest.TestCase):

    testInstance = MyLibrary.keywords()
    wd = webdriver.Firefox()

    def setUp(self):
        print ('---- setUp---')

    def tearDown(self):
        self.wd.close()

    def testAssertion(self):
        print ('----- testAssertion ----')
        self.testInstance.ML_get_page(self.wd,'top')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()