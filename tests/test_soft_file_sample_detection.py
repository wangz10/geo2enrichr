import unittest

from g2e.signature_factory.soft_file_factory.file_manager import _build_selections


class TestSoftFileSampleDetection(unittest.TestCase):

    def test_AABB(self):
        selections = {}
        selections['a_indices'] = [0, 1]
        selections['b_indices'] = [2, 3]
        ans = _build_selections(selections)
        self.assertEqual(ans, ['0', '0', '1', '1'])

    def test_ABAB(self):
        selections = {}
        selections['a_indices'] = [0, 2]
        selections['b_indices'] = [1, 3]
        ans = _build_selections(selections)
        self.assertEqual(ans, ['0', '0', '1', '1'])

    def test_BABA(self):
        selections = {}
        selections['a_indices'] = [2, 4]
        selections['b_indices'] = [1, 3]
        ans = _build_selections(selections)
        self.assertEqual(ans, ['0', '0', '1', '1'])

    def test_BBABBBB(self):
        selections = {}
        selections['a_indices'] = [3]
        selections['b_indices'] = [1, 2, 4, 5, 6, 7]
        ans = _build_selections(selections)
        self.assertEqual(ans, ['0', '1', '1', '1', '1', '1', '1'])

    def test_indices(self):
        selections = {}
        selections['a_indices'] = [3, 99]
        selections['b_indices'] = [45, 67]
        ans = _build_selections(selections)
        self.assertEqual(ans, ['0', '0', '1', '1'])
