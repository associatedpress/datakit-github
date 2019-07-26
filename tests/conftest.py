import os
import shutil

import pytest
from datakit.utils import makedirs, mkdir_p, write_json


@pytest.fixture
def datakit_home(tmpdir):
    return os.path.join(str(tmpdir), '.datakit')


@pytest.fixture
def plugin_dir(datakit_home):
    return os.path.join(datakit_home, 'plugins/datakit-github')


@pytest.fixture
def create_plugin_config_default(plugin_dir):
    config_file = os.path.join(plugin_dir, 'config.json')
    config = {'default_template': ''}
    write_json(config_file, config)


@pytest.fixture(autouse='session')
def setup_environment(monkeypatch, datakit_home):
    mkdir_p(datakit_home)
    monkeypatch.setenv('DATAKIT_HOME', datakit_home)

@pytest.fixture(autouse="module")
def create_plugin_dir(plugin_dir):
    mkdir_p(plugin_dir)
    yield
    shutil.rmtree(plugin_dir)
