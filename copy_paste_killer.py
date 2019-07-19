import sublime
import sublime_plugin
from .copy_paste_killer_selection_converter import CopyPasteKillerSelectionConverter


class CopyPasteKillerCommand(sublime_plugin.TextCommand):
    """CopyPasteKillerCommand Plugin."""

    def run(self, edit):
        settings = sublime.load_settings("CopyPasteKiller.sublime-settings")
        view = self.view
        window = self.view.window()
        selection = view.substr(view.sel()[0])
        if len(selection) == 0:
            # Select the line on no selection
            selection = view.substr(view.line(view.sel()[0]))

        find_string = CopyPasteKillerSelectionConverter.convert_for_find(selection)
        find_view = self._open_tab_with_snippet(find_string, "CopyPasteKiller (Find)")

        window.run_command('select_all')
        window.run_command('slurp_find_string')

        replace_string = CopyPasteKillerSelectionConverter.convert_for_replace(selection)
        replace_view = self._open_tab_with_snippet(replace_string, "CopyPasteKiller (Replace)")

        window.run_command('select_all')
        window.run_command('slurp_replace_string')

        if not settings.get("keep_panels_open", True):
            find_view.close()
            replace_view.close()

        panel_args = {
            "panel": "find_in_files",
            "regex": True,
            "case_sensitive": True,
            "whole_word": False
        }
        window.run_command("show_panel", panel_args)

    def _open_tab_with_snippet(self, selection, name):
        v = self.view.window().new_file()
        v.set_name(name)
        v.set_scratch(True)
        v.assign_syntax('Packages/Regular Expressions/RegExp.sublime-syntax')
        v.run_command('append', {'characters': selection})
        return v
