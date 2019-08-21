import os
from unittest import mock

import pytest

from ..conftest import create_plugin_config
from datakit_github.commands import Integrate


TOKEN = os.environ.get('DATAKIT_GITHUB_ACCESS_TOKEN', 'DUMMY')


def test_config_missing_error(caplog):
    cmd = Integrate(None, None, cmd_name='github integrate')
    parsed_args = mock.Mock()
    cmd.run(parsed_args)
    err_msg = "You must configure a Github API key to use this command!!"
    assert err_msg in caplog.text


@pytest.mark.vcr()
@pytest.mark.usefixtures('create_readme')
def test_choose_default_account(caplog, plugin_dir):
    with mock.patch('datakit_github.commands.integrate.ask', side_effect=['','y', 'y']) as mocked, \
        mock.patch('datakit_github.commands.integrate.Repository.push', return_value=None) as repo_push:
        create_plugin_config(plugin_dir, {'github_api_key': TOKEN})
        cmd = Integrate(None, None, cmd_name='github integrate')
        parsed_args = mock.Mock()
        cmd.run(parsed_args)
        assert "(1) zstumgoren" in caplog.text
        assert "(3) associatedpress" in caplog.text
        assert "Repo created at https://github.com/zstumgoren/fake-project" in caplog.text
        assert "First commit made locally and pushed to remote" in caplog.text
        assert "View the project on Github at https://github.com/zstumgoren/fake-project" in caplog.text
        assert repo_push.call_count == 1


@pytest.mark.vcr()
@pytest.mark.usefixtures('create_readme')
def test_choose_org_account_private_error(caplog, plugin_dir):
    with mock.patch('datakit_github.commands.integrate.ask', side_effect=['3','y','y']) as mocked, \
        mock.patch('datakit_github.commands.integrate.Repository.push', return_value=None) as repo_push:
        create_plugin_config(plugin_dir, {'github_api_key': TOKEN})
        cmd = Integrate(None, None, cmd_name='github integrate')
        parsed_args = mock.Mock()
        cmd.run(parsed_args)
        assert "(1) zstumgoren" in caplog.text
        assert "(3) associatedpress" in caplog.text
        err_msg = "Visibility can't be private. Please upgrade your subscription to create a new private repository."
        assert err_msg in caplog.text


@pytest.mark.vcr()
@pytest.mark.usefixtures('create_readme')
def test_choose_org_account_public_repo(caplog, plugin_dir):
    with mock.patch('datakit_github.commands.integrate.ask', side_effect=['3','y','n']) as mocked, \
        mock.patch('datakit_github.commands.integrate.Repository.push', return_value=None) as repo_push:
        create_plugin_config(plugin_dir, {'github_api_key': TOKEN})
        cmd = Integrate(None, None, cmd_name='github integrate')
        parsed_args = mock.Mock()
        cmd.run(parsed_args)
        assert "(1) zstumgoren" in caplog.text
        assert "(3) associatedpress" in caplog.text
        assert "Repo created at https://github.com/associatedpress/fake-project" in caplog.text
        assert "First commit made locally and pushed to remote" in caplog.text
        assert "View the project on Github at https://github.com/associatedpress/fake-project" in caplog.text
        assert repo_push.call_count == 1


@pytest.mark.vcr()
def test_repo_already_exists_org_account(caplog, plugin_dir):
    with mock.patch('datakit_github.commands.integrate.ask', side_effect=['3','y', 'n']) as mocked:
        create_plugin_config(plugin_dir, {'github_api_key': TOKEN})
        cmd = Integrate(None, None, cmd_name='github integrate')
        parsed_args = mock.Mock()
        cmd.run(parsed_args)
        assert "ERROR: Failed to create fake-project for associatedpress: name already exists on this account" in caplog.text


@pytest.mark.vcr()
def test_repo_already_exists(caplog, plugin_dir):
    with mock.patch('datakit_github.commands.integrate.ask', side_effect=['','y', 'y']) as mocked:
        create_plugin_config(plugin_dir, {'github_api_key': TOKEN})
        cmd = Integrate(None, None, cmd_name='github integrate')
        parsed_args = mock.Mock()
        cmd.run(parsed_args)
        assert "(1) zstumgoren" in caplog.text
        assert "ERROR: Failed to create fake-project for zstumgoren: name already exists on this account" in caplog.text


@pytest.mark.vcr()
@pytest.mark.usefixtures('init_repo')
def test_repo_already_initialized(caplog, plugin_dir):
    with mock.patch('datakit_github.commands.integrate.ask', side_effect=['','y','y']) as mocked:
        create_plugin_config(plugin_dir, {'github_api_key': TOKEN})
        cmd = Integrate(None, None, cmd_name='github integrate')
        parsed_args = mock.Mock()
        cmd.run(parsed_args)
        assert "Repo has already been initialized locally!!" in caplog.text
