import unittest
from main import app


class FlaskTest(unittest.TestCase):

    def test_add(self):
        tester = app.test_client(self)
        num1 = 10
        num2 = 20
        response = tester.post('/add', json={"num1":num1, "num2":num2})
        statuscode = response.get_json()["status"]
        val1 = response.get_json()["msg"]
        self.assertEqual(statuscode, 200)
        self.assertEqual(val1, num1+num2)

    def test_sub(self):
        tester = app.test_client(self)
        num1 = 10
        num2 = 20
        response = tester.post('/sub', json={"num1":num1, "num2":num2})
        statuscode = response.get_json()["status"]
        val1 = response.get_json()["msg"]
        self.assertEqual(statuscode, 200)
        self.assertEqual(val1, abs(num1 - num2))

    def test_mul(self):
        tester = app.test_client(self)
        num1 = 10
        num2 = 20
        response = tester.post('/mul', json={"num1":num1, "num2":num2})
        statuscode = response.get_json()["status"]
        val1 = response.get_json()["msg"]
        self.assertEqual(statuscode, 200)
        self.assertEqual(val1, num1 * num2)

    def test_div(self):
        tester = app.test_client(self)
        num1 = 10
        num2 = 20
        response = tester.post('/div', json={"num1": num1, "num2": num2})
        statuscode = response.get_json()["status"]
        val1 = response.get_json()["msg"]
        self.assertEqual(statuscode, 200)
        self.assertEqual(val1, num1 / num2)


if __name__ == "__main__":
    unittest.main()


