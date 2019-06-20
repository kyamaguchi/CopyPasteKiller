import re


class CopyPasteKillerSelectionConverter:

    @classmethod
    def convert_for_find(cls, string):
        lines = []
        for line in string.split("\n"):
            result = re.escape(re.sub(r'^\s+', "", line))
            # Revert quotes and some special characters to fix "Find"
            result = re.sub(r"\\'", "'", result)
            result = re.sub(r'\\"', '"', result)
            result = re.sub(r'\\<', '<', result)
            result = re.sub(r'\\>', '>', result)
            result = re.sub(r'\\`', '`', result)
            lines.append(result)
        return "\n".join(["^([ \\t]*)" + l for l in lines])

    @classmethod
    def convert_for_replace(cls, string):
        lines = []
        for line in string.split("\n"):
            result = re.sub(r'^\s+', "", line)
            result = result.replace('\\', '\\\\')
            result = result.replace('$', '\\$')
            lines.append(result)
        return "\n".join(["${}".format(i+1) + l for i, l in enumerate(lines)])
