import os
from unittest import mock

import pytest

from ..conftest import create_plugin_config
from datakit_github.commands import Integrate


TOKEN = os.environ.get('DATAKIT_TESTER_GITHUB_ACCESS_TOKEN', 'DUMMY')


@pytest.mark.vcr()
@pytest.mark.usefixtures('create_readme')
def test_choose_default_account_basic(caplog, plugin_dir):
    with mock.patch('datakit_github.commands.integrate.ask', side_effect=['','y', 'y']) as mocked, \
        mock.patch('datakit_github.commands.integrate.Repository.push', return_value=None) as repo_push:
        create_plugin_config(plugin_dir, {'github_api_key': TOKEN})
        cmd = Integrate(None, None, cmd_name='github integrate')
        parsed_args = mock.Mock()
        cmd.run(parsed_args)
        assert "Repo will be created on account: dkit-tester" in caplog.text
        assert "Repo created at https://github.com/dkit-tester/fake-project" in caplog.text
        assert "First commit made locally and pushed to remote" in caplog.text
        assert "View the project on Github at https://github.com/dkit-tester/fake-project" in caplog.text
        assert repo_push.call_count == 1

@pytest.mark.vcr()
@pytest.mark.usefixtures('create_readme')
def test_return_chosen_inputs(plugin_dir):
    with mock.patch('datakit_github.commands.integrate.ask', side_effect=['','y', 'y']) as mocked, \
        mock.patch('datakit_github.commands.integrate.Repository.push', return_value=None) as repo_push:
        create_plugin_config(plugin_dir, {'github_api_key': TOKEN})
        cmd = Integrate(None, None, cmd_name='github integrate')
        parsed_args = mock.Mock()
        choices = cmd.run(parsed_args)
        assert choices['repo_name'] == 'fake-project'
        assert choices['account'] == 'dkit-tester'
        assert choices['private_repo'] == True
