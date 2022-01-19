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
    def push(remote='origin', branch='main'):
        return subprocess.check_output(['git', 'push', '-u', remote, branch])
