import re


class CopyPasteKillerSelectionConverter:

    @classmethod
    def convert_for_find_and_replace(cls, string):
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
