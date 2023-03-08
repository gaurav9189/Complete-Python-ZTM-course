import unittest
import exercise_200


class TestExercise(unittest.TestCase):
    def setUp(self):
        print('Testing begins')

    def test1_right(self):
        answer = 10
        guess = 10
        result = exercise_200.rand(guess, answer)
        self.assertEqual(result, 1)

    def test2_wrong(self):
        answer = 9
        guess = 10
        result = exercise_200.rand(guess, answer)
        self.assertEqual(result, 2)

    def test2_range(self):
        answer = 9
        guess = 11
        result = exercise_200.rand(guess, answer)
        self.assertFalse(result)

    def tearDown(self):
        print('Testing ends')


if __name__ == '__main__':
    unittest.main()
