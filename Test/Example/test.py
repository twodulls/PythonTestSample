import unittest

class StringTest(unittest.TestCase):
	def setup(self):
		pass

	def test1(self):
		self.assertEqual('Foo'.upper(), 'FOO')

	def test2(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test3(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'test'])
		#check that s.split fails when the seperator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(StringTest('test2'))
	#suite.addTest(TestClass('test_isupper'))
	return suite

if __name__ == '__main__':
	#unittest.main()
	unittest.TextTestRunner(verbosity=2).run(suite())
