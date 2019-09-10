import os
import shutil
import subprocess

import pytest
from datakit.utils import makedirs, mkdir_p, write_json

from datakit_github.github_api import GithubApi
from datakit_github.repository import Repository


@pytest.fixture(scope='module')
def vcr_config():
    return {
        'filter_headers': [('authorization', 'DUMMY')],
    }

def create_gh_project(project_slug):
    token = os.environ.get('DATAKIT_GITHUB_ACCESS_TOKEN', 'DUMMY')
    return GithubApi('associatedpress', project_slug, {'api_key': token})


@pytest.fixture
def datakit_home(tmpdir):
    return os.path.join(str(tmpdir), '.datakit')


@pytest.fixture
def plugin_dir(datakit_home):
    return os.path.join(datakit_home, 'plugins/datakit-github')


@pytest.fixture
def fake_project(tmpdir):
    return os.path.join(tmpdir.strpath, 'fake-project')


@pytest.fixture(autouse=True)
def setup(datakit_home, plugin_dir, fake_project, monkeypatch, tmpdir):
    mkdir_p(datakit_home)
    mkdir_p(plugin_dir)
    mkdir_p(fake_project)
    monkeypatch.setenv('DATAKIT_HOME', datakit_home)
    monkeypatch.chdir(fake_project)


@pytest.fixture
def init_repo():
    Repository.init()


@pytest.fixture
def create_readme(fake_project):
    readme = os.path.join(fake_project, "README.md")
    content = "Example readme for a test project"
    with open(readme, 'w') as fh:
        fh.write(content)


@pytest.fixture
def stage_files():
    Repository.add()


@pytest.fixture
def create_plugin_config_default(plugin_dir):
    config_file = os.path.join(plugin_dir, 'config.json')
    config = {'default_template': ''}
    write_json(config_file, config)


def create_plugin_config(plugin_dir, content):
    mkdir_p(plugin_dir)
    config_file = os.path.join(plugin_dir, 'config.json')
    write_json(config_file, content)
    return content


def create_project_config(project_root, contents={}):
    config_dir = os.path.join(project_root, 'config')
    mkdir_p(config_dir)
    project_config = os.path.join(config_dir, 'datakit-github.json')
    write_json(project_config, contents)


def dir_contents(path):
    dirs_and_files = []
    for root, subdirs, files in os.walk(path):
        for directory in subdirs:
            dirs_and_files.append(directory)
            for fname in files:
                dirs_and_files.append(os.path.join(directory, fname))
    return dirs_and_files


def read_fixture(name):
    tests_dir = os.path.dirname(__file__)
    fixture_pth = os.path.join(tests_dir, "fixtures/{}.json".format(name))
    with open(fixture_pth, 'r') as fh:
        return fh.read()


def repo_status():
    return subprocess.check_output(['git', 'status']).decode('utf-8')


def repo_log(num=1):
    return subprocess.check_output(['git', 'log']).decode('utf-8')
