import unittest

from counter_service import CounterService


class CounterServiceTests(unittest.TestCase):
    def test_returns_two_after_two_increments(self):
        service = CounterService()

        service.increment()
        service.increment()

        self.assertEqual(2, service.get_current_value())


if __name__ == "__main__":
    unittest.main()
