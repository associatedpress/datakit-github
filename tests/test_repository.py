import os
import re
import subprocess
from unittest import mock

import pytest
from .conftest import repo_status, repo_log

from datakit_github.repository import Repository


CHECK_OUTPUT = 'datakit_github.repository.subprocess.check_output'


def test_init(fake_project):
    Repository.init()
    assert '.git' in os.listdir(fake_project)


@pytest.mark.usefixtures('init_repo', 'create_readme')
def test_add_untracked(fake_project):
    p = "Untracked files.*?README.md"
    assert re.search(p, repo_status(), re.DOTALL)
    Repository.add()
    assert "new file:   README.md" in repo_status()


@pytest.mark.usefixtures(
    'init_repo',
    'create_readme',
    'stage_files'
)
def test_commit(fake_project):
    Repository.commit("Initial commit")
    assert 'Initial commit' in repo_log()


@pytest.mark.usefixtures('init_repo')
def test_add_remote():
    repo_url = 'git@github.com:associatedpress/datakit-github.git'
    Repository.add_remote(repo_url)
    origin = subprocess.check_output(['git', 'remote', 'get-url', 'origin'])
    assert origin.decode().strip() == repo_url


def test_push_targets_given_remote_and_branch():
    with mock.patch(CHECK_OUTPUT) as check_output:
        Repository.push(remote='upstream', branch='trunk')
    check_output.assert_called_once_with(['git', 'push', '-u', 'upstream', 'trunk'])


def test_push_defaults_to_the_repos_default_branch():
    with mock.patch(CHECK_OUTPUT) as check_output:
        check_output.return_value = b'trunk\n'
        Repository.push()
    check_output.assert_any_call(['git', 'push', '-u', 'origin', 'trunk'])


def test_default_branch_from_config():
    with mock.patch(CHECK_OUTPUT) as check_output:
        check_output.return_value = b'trunk\n'
        assert Repository.default_branch() == 'trunk'
        check_output.assert_called_once_with(['git', 'config', 'init.defaultBranch'])


def test_default_branch_falls_back_to_main():
    with mock.patch(CHECK_OUTPUT) as check_output:
        # git exits non-zero when init.defaultBranch is unset
        check_output.side_effect = subprocess.CalledProcessError(1, 'git')
        assert Repository.default_branch() == 'main'
