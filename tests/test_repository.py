import os
import re
import subprocess
from unittest import mock

import pytest
from .conftest import repo_status, repo_log

from datakit_github.repository import Repository


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
    with mock.patch('datakit_github.repository.subprocess.check_output') as check_output:
        Repository.add_remote(repo_url)
        check_output.assert_called_once_with(['git', 'remote', 'add', 'origin', repo_url])


@pytest.mark.usefixtures(
    'init_repo',
    'create_readme',
    'stage_files'
)
def test_push():
    patch_target = 'datakit_github.repository.subprocess.check_output'
    with mock.patch(patch_target) as check_output:
        Repository.commit('Initial commit')
        Repository.rename_current_branch('main')
        Repository.push(branch='main')
        expected_calls = [
            (['git', 'commit', '-m', 'Initial commit'],),
            (['git', 'branch', '--move', 'main'],),
            (['git', 'push', '-u', 'origin', 'main'],)
        ]
        actual_calls = [call[1] for call in check_output.mock_calls]
        assert actual_calls == expected_calls


def test_default_branch_from_config():
    patch_target = 'datakit_github.repository.subprocess.check_output'
    with mock.patch(patch_target) as check_output:
        check_output.return_value = b'trunk\n'
        assert Repository.default_branch() == 'trunk'
        check_output.assert_called_once_with(['git', 'config', 'init.defaultBranch'])


def test_default_branch_falls_back_to_main():
    patch_target = 'datakit_github.repository.subprocess.check_output'
    with mock.patch(patch_target) as check_output:
        # git exits non-zero when init.defaultBranch is unset
        check_output.side_effect = subprocess.CalledProcessError(1, 'git')
        assert Repository.default_branch() == 'main'


def test_push_uses_default_branch():
    patch_target = 'datakit_github.repository.subprocess.check_output'
    with mock.patch(patch_target) as check_output:
        check_output.return_value = b'trunk\n'
        Repository.push()
        check_output.assert_any_call(['git', 'push', '-u', 'origin', 'trunk'])
