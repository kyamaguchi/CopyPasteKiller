import sublime
import sublime_plugin
import re


class CopyPasteKillerCommand(sublime_plugin.WindowCommand):
    """CopyPasteKillerCommand Plugin."""

    def run(self):
        window = sublime.active_window()
        view = window.active_view()
        selection = view.substr(view.sel()[0])
        if len(selection) == 0:
            # Select the line on no selection
            selection = view.substr(view.line(view.sel()[0]))

        find_string, replace_string = self._convert_for_find_and_replace(selection)
        self._open_tab_with_find_string(find_string)

        self.window.run_command('select_all')
        self.window.run_command('slurp_find_string')

        self._open_tab_with_find_string(replace_string)

        self.window.run_command('select_all')
        self.window.run_command('slurp_replace_string')
        panel_args = {
            "panel": "find_in_files",
            "regex": True,
            "case_sensitive": True
        }
        self.window.run_command("show_panel", panel_args)

    def _convert_for_find_and_replace(self, string):
        find_lines = []
        for line in string.split("\n"):
            result = re.escape(re.sub(r'^\s+', "", line))
            # Revert quotes to fix "Find"
            result = re.sub(r"\\'", "'", result)
            result = re.sub(r'\\"', '"', result)
            find_lines.append(result)
        find_string = "\n".join(["^([ \\t]*)" + l for l in find_lines])

        replace_lines = []
        for line in string.split("\n"):
            result = re.sub(r'^\s+', "", line)
            replace_lines.append(result)
        replace_string = "\n".join(["${}".format(i+1) + l for i, l in enumerate(replace_lines)])
        return [find_string, replace_string]

    def _open_tab_with_find_string(self, selection):
        v = self.window.new_file()
        v.set_name("Find without indent")
        v.set_scratch(True)
        v.assign_syntax('Packages/Regular Expressions/RegExp.sublime-syntax')
        v.run_command('append', {'characters': selection})
