import unittest

class TestMethod(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        #cls._connection = createExpensiveConnectionObject()
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        #cls._connection.destroy()
        print("tearDownClass")

    def test1(self):
        print("test1")
        pass

    def test2(self):
        print("test2")
        pass

if __name__ == '__main__':
    unittest.main()
