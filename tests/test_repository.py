import os
import re
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
    repo_url = 'git@github.com:associatedpress/datakit-github.git'
    patch_target = 'datakit_github.repository.subprocess.check_output'
    with mock.patch(patch_target) as check_output:
        Repository.commit('Initial commit')
        Repository.push()
        expected_calls = [
            (['git', 'commit', '-m', 'Initial commit'],),
            (['git', 'push', '-u', 'origin', 'main'],)
        ]
        actual_calls = [call[1] for call in check_output.mock_calls]
        assert actual_calls == expected_calls
