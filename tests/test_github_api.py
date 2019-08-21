import os

import pytest

from datakit_github.github_api import GithubApi


TOKEN = os.environ.get('DATAKIT_GITHUB_ACCESS_TOKEN', 'DUMMY')


@pytest.mark.vcr()
def test_accounts():
    expected = [
        'zstumgoren',
        'PythonJournos',
        'associatedpress',
        'datakit-cli',
        'documentcloud',
        'openelections',
        'overview',
        'stanfordjournalism'
    ]
    actual = [account.login for account in GithubApi.accounts(TOKEN)]
    assert actual == expected
