import sublime
import sys, os
from unittest import TestCase

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from copy_paste_killer_selection_converter import CopyPasteKillerSelectionConverter


class TestCopyPasteKillerSelectionConverter(TestCase):

    def test_indent(self):
        self._run_test_with_scenario('indent')

    def test_no_indent(self):
        self._run_test_with_scenario('no_indent')

    def test_single_line(self):
        self._run_test_with_scenario('single_line')

    def test_tab_indent(self):
        self._run_test_with_scenario('tab_indent')

    def _run_test_with_scenario(self, scenario):
        base_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(base_path, 'data', "{}.txt".format(scenario)), "r") as file:
            selection = file.read()
        with open(os.path.join(base_path, 'data', "{}_find.txt".format(scenario)), "r") as file:
            expected_find_string = file.read()
        with open(os.path.join(base_path, 'data', "{}_replace.txt".format(scenario)), "r") as file:
            expected_replace_string = file.read()
        find_string, replace_string = CopyPasteKillerSelectionConverter.convert_for_find_and_replace(selection)
        self.assertEqual(find_string, expected_find_string)
        self.assertEqual(replace_string, expected_replace_string)
