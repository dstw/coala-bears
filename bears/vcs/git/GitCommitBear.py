import os
import shutil

from bears.vcs.CommitBear import _CommitBear
from coala_utils.ContextManagers import change_directory
from coalib.misc.Shell import run_shell_command


class GitCommitBear(_CommitBear):
    LANGUAGES = {'Git'}
    ASCIINEMA_URL = 'https://asciinema.org/a/e146c9739ojhr8396wedsvf0d'

    @classmethod
    def check_prerequisites(cls):
        if shutil.which('git') is None:
            return 'git is not installed.'
        else:
            return True

    def get_remotes():
        remotes, _ = run_shell_command(
            "git config --get-regex '^remote.*.url$'")
        return remotes

    def get_head_commit(self):
        with change_directory(self.get_config_dir() or os.getcwd()):
            return run_shell_command('git log -1 --pretty=%B')
