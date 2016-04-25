from coalib.bearlib.abstractions.Linter import linter


@linter(executable='luacheck',
        use_stdin=True,
        output_format='regex',
        output_regex=r'.+:(?P<line>\d+):(?P<column>\d+): (?P<message>.+)')
class LuaLintBear:
    """
    Checks the code with ``luacheck``.
    """

    @staticmethod
    def create_arguments(filename, file, config_file):
        return "-",