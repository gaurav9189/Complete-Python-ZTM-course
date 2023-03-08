import unittest
import exercise_200


class TestExercise(unittest.TestCase):
    def setUp(self):
        print('Testing begins')

    def test1(self):
        answer = 10
        guess = 10
        result = exercise_200.rand(guess, answer)
        self.assertEqual(result, 1)

    def test2(self):
        answer = 9
        guess = 10
        result = exercise_200.rand(guess, answer)
        self.assertEqual(result, 'Again')
    # def test_do_stuff2(self):
    #     test_param = 'asdasd'
    #     result = exercise_200.do_stuff(test_param)
    #     self.assertIsInstance(result, ValueError)
    #     # Since result is an instance of the class ValueError hence used this method of unittest.TestCase class

    # def test_do_stuff3(self):
    #     test_param = None
    #     result = exercise_200.do_stuff(test_param)
    #     self.assertEqual(result, 'Please enter a number')
    #     # changed the main.py to add an if statement and a default param

    # def test_do_stuff4(self):
    #     test_param = ''
    #     result = exercise_200.do_stuff(test_param)
    #     self.assertEqual(result, 'Please enter a number')

    # def test_do_stuff5(self):
    #     test_param = ' '
    #     result = exercise_200.do_stuff(test_param)
    #     self.assertIsInstance(result, ValueError)

    # def test_do_stuff6(self):
    #     test_param = 0
    #     result = exercise_200.do_stuff(test_param)
    #     self.assertEqual(result, 5)

    def tearDown(self):
        print('Testing ends')


if __name__ == '__main__':
    unittest.main()
