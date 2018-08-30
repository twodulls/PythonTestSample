import unittest, sys

version = 1.2

class SkipTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(version < 1.3, "not supported in this library version: %s" %version )
    def test_format(self):
        #Tests that work for only a certain version of the library
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        #windows specific testing code
        pass

if __name__ == '__main__':
    unittest.main()
