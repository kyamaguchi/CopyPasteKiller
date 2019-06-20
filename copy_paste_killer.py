import sublime
import sublime_plugin
from .copy_paste_killer_selection_converter import CopyPasteKillerSelectionConverter


class CopyPasteKillerCommand(sublime_plugin.WindowCommand):
    """CopyPasteKillerCommand Plugin."""

    def run(self):
        window = sublime.active_window()
        view = window.active_view()
        selection = view.substr(view.sel()[0])
        if len(selection) == 0:
            # Select the line on no selection
            selection = view.substr(view.line(view.sel()[0]))

        find_string = CopyPasteKillerSelectionConverter.convert_for_find(selection)
        self._open_tab_with_find_string(find_string, "CopyPasteKiller (Find)")

        self.window.run_command('select_all')
        self.window.run_command('slurp_find_string')

        replace_string = CopyPasteKillerSelectionConverter.convert_for_replace(selection)
        self._open_tab_with_find_string(replace_string, "CopyPasteKiller (Replace)")

        self.window.run_command('select_all')
        self.window.run_command('slurp_replace_string')
        panel_args = {
            "panel": "find_in_files",
            "regex": True,
            "case_sensitive": True
        }
        self.window.run_command("show_panel", panel_args)

    def _open_tab_with_find_string(self, selection, name):
        v = self.window.new_file()
        v.set_name(name)
        v.set_scratch(True)
        v.assign_syntax('Packages/Regular Expressions/RegExp.sublime-syntax')
        v.run_command('append', {'characters': selection})
