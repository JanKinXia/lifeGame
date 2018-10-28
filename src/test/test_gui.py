from unittest import TestCase
from GUI import Gui


class TestGui(TestCase):
    def setUp(self):
        self.gui = Gui(25, 25)
        self.assertEqual(self.gui.rows,25)
        self.assertEqual(self.gui.cols, 25)

    def test_draw(self):
        self.gui.draw()

    def test_g_update(self):
        self.gui.g_update()

    def test_start(self):
        self.gui.start()

    def test_pause(self):
        self.gui.pause()
