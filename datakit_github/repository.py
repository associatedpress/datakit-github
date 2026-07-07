import os
import subprocess


class Repository:

    @staticmethod
    def initialized():
        return os.path.exists('.git')

    @staticmethod
    def init():
        return subprocess.check_output(['git', 'init'])

    @staticmethod
    def add():
        return subprocess.check_output(['git', 'add', '.'])

    @staticmethod
    def commit(message):
        return subprocess.check_output(['git', 'commit', '-m', message])

    @staticmethod
    def add_remote(repo_url, name='origin'):
        return subprocess.check_output(['git', 'remote', 'add', name, repo_url])

    @staticmethod
    def default_branch():
        """Name of the branch git creates on `init`.

        Honors the user's `init.defaultBranch` git config, falling back to
        `main` when it is unset (older gits default to `master`, but we prefer
        `main` when we have to guess).
        """
        try:
            branch = subprocess.check_output(
                ['git', 'config', 'init.defaultBranch']
            ).decode().strip()
        except subprocess.CalledProcessError:
            branch = ''
        return branch or 'main'

    @staticmethod
    def rename_current_branch(new_name):
        return subprocess.check_output(['git', 'branch', '--move', new_name])

    @staticmethod
    def push(remote='origin', branch=None):
        if branch is None:
            branch = Repository.default_branch()
        return subprocess.check_output(['git', 'push', '-u', remote, branch])
