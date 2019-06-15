import sublime
import sublime_plugin
import re


class FindWithoutIndentCommand(sublime_plugin.WindowCommand):
    """FindWithoutIndentCommand Plugin."""

    def run(self):
        window = sublime.active_window()
        view = window.active_view()
        selection = view.substr(view.sel()[0])
        if len(selection) == 0:
            # Select the line on no selection
            selection = view.substr(view.line(view.sel()[0]))

        find_string = self._convert_for_find(selection)
        self._open_tab_with_find_string(find_string)

        self.window.run_command("select_all")
        self.window.run_command('slurp_find_string')
        panel_args = {
            "panel": "find_in_files",
            "regex": True,
            "case_sensitive": True
        }
        self.window.run_command("show_panel", panel_args)

    def _convert_for_find(self, string):
        lines = []
        for line in string.split("\n"):
            if len(line) == 0:
                continue
            # Replace leading spaces(indent) with that of regex
            result = re.escape(re.sub(r'^\s+', "", line))
            lines.append(result)
        find_string = "\n".join(["^[ \\t]*" + l for l in lines])
        return find_string

    def _open_tab_with_find_string(self, selection):
        v = self.window.new_file()
        v.set_name("Find without indent")
        v.set_scratch(True)
        v.assign_syntax('Packages/Regular Expressions/RegExp.sublime-syntax')
        v.run_command('append', {'characters': selection})
