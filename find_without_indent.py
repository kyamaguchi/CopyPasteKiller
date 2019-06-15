import sublime
import sublime_plugin


class FindWithoutIndentCommand(sublime_plugin.WindowCommand):
    """FindWithoutIndentCommand Plugin."""

    def run(self):
        window = sublime.active_window()
        view = window.active_view()
        selection = view.substr(view.sel()[0])
        if len(selection) == 0:
            # Select the line on no selection
            selection = view.substr(view.line(view.sel()[0]))
        self._open_tab_with_find_string(selection)

    def _open_tab_with_find_string(self, selection):
        v = self.window.new_file()
        v.set_name("Find without indent")
        v.set_scratch(True)
        v.assign_syntax('Packages/Regular Expressions/RegExp.sublime-syntax')
        v.run_command('append', {'characters': selection})
