from unittest import TestCase
from View import View


class TestView(TestCase):
    def setUp(self):
        self.view = View(0.2, 25, 25)

    def test_update(self):
        self.view.update()

    def test_count_neighbours(self):
        for i in range(self.view.num_of_rows):
            for j in range(self.view.num_of_cols):
                self.view.count_neighbours(i, j, self.view.map)

