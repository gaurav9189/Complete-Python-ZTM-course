import unittest
import Testing_196


class TestTesting_196(unittest.TestCase):
    def setUp(self):
        print('Testing begins')

    def test_do_stuff1(self):
        test_param = 10
        result = Testing_196.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdasd'
        result = Testing_196.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
        # Since result is an instance of the class ValueError hence used this method of unittest.TestCase class

    def test_do_stuff3(self):
        test_param = None
        result = Testing_196.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')
        # changed the main.py to add an if statement and a default param

    def test_do_stuff4(self):
        test_param = ''
        result = Testing_196.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff5(self):
        test_param = ' '
        result = Testing_196.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff6(self):
        test_param = 0
        result = Testing_196.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('Testing ends')


if __name__ == '__main__':
    unittest.main()
