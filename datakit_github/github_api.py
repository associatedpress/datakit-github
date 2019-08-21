from operator import attrgetter
from github import Github


class GithubApi:

    @staticmethod
    def accounts(api_key):
        g = Github(api_key)
        user = g.get_user()
        accounts = [user]
        orgs = [org for org in user.get_orgs()]
        sorted_orgs = sorted(orgs, key=attrgetter('login'))
        accounts.extend(sorted_orgs)
        return accounts
