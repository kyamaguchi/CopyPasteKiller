import sublime
import sys
import os
import glob
from unittest import TestCase

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from copy_paste_killer_selection_converter import CopyPasteKillerSelectionConverter


class TestCopyPasteKillerSelectionConverter(TestCase):

    def test_scenarios(self):
        files = glob.glob(os.path.join(self._data_dir(), '*_source.txt'))
        for filepath in files:
            scenario = os.path.basename(filepath).replace('_source.txt', '')
            self._run_test_with_scenario(scenario)

    def _run_test_with_scenario(self, scenario):
        with open(os.path.join(self._data_dir(), "{}_source.txt".format(scenario)), "r") as file:
            selection = file.read()
        with open(os.path.join(self._data_dir(), "{}_find.txt".format(scenario)), "r") as file:
            expected_find_string = file.read()
        with open(os.path.join(self._data_dir(), "{}_replace.txt".format(scenario)), "r") as file:
            expected_replace_string = file.read()
        find_string, replace_string = CopyPasteKillerSelectionConverter.convert_for_find_and_replace(selection)
        self.assertEqual(find_string, expected_find_string)
        self.assertEqual(replace_string, expected_replace_string)

    def _data_dir(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(base_path, 'data')