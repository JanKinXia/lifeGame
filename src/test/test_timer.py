from unittest import TestCase
from Timer import Timer


class TestTimer(TestCase):
    def setUp(self):
        self.timer = Timer(1, self.test())

    def test(self):
        print('test')

    def test_start(self):
        self.timer.start()

    def test_run(self):
        self.timer.run()

    def test_pause(self):
        self.timer.pause()
