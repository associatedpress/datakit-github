# -*- coding: utf-8 -*-
from cliff.command import Command
from github.GithubException import GithubException
from datakit_github.github_api import GithubApi
from datakit_github.repository import Repository
from datakit_github.project_mixin import ProjectMixin


def ask(question):
    return input(question)


class Integrate(ProjectMixin, Command):
    "Integrate local project code with Github"

    def take_action(self, parsed_args):
        # Check for Github API key from configs
        # TODO: Provide more helpful error message on how to create API key
        # and configure plugin locally
        api_key = self.configs.get('github_api_key')
        if not api_key:
            err_msg = "You must configure a Github API key to use this command!!\n"
            self.log.error(err_msg)
        elif Repository.initialized():
            self.log.error("\nERROR: Repo has already been initialized locally!!")
            self.log.error(
                "You must either remove the .git/ directory " +
                "before re-running this command, or manually " +
                "configure Github integration.\n"
            )
        else:
            accounts = GithubApi.accounts(api_key)
            # Prompt user to select an account.
            if len(accounts) == 1:
                account = accounts[0]
            else:
                msg = "Choose an account where the new project should be created:\n"
                account_lkup = {}
                self.log.info(msg)
                for idx, account in enumerate(accounts):
                    num = idx + 1
                    account_lkup[num] = account
                    self.log.info("({}) {}".format(num, account.login))

                # TODO: Check plugin for default account configuration,
                # otherwise default to personal account
                default = account_lkup[1]
                choice_msg = "\nType a number or leave blank for default [{}]: ".format(default.login)
                choice = ask(choice_msg)
                if choice.strip() == '':
                    target_account = default
                else:
                    target_account = account_lkup[int(choice)]
                self.log.info("You chose: {}".format(target_account.login))
                confirm = ask("Is this correct? y/n [y]: ").strip().lower()
                if confirm in ["y", ""]:
                    # TODO: Handle overrides for project settings from
                    # configs and/or command-line flags (e.g. privacy)
                    privacy_choice = ask("Should this repo be private? y/n [y]: ").strip().lower()
                    privacy = True if privacy_choice in ['', 'y'] else False
                    try:
                        resp = target_account.create_repo(self.project_slug, private=privacy)
                        self.log.info("Repo created at {}".format(resp.html_url))
                        self.log.info("Running local Git initialization...")
                        # TODO: Create a project-level config/datakit-github.json?
                        # containing name of selected account and possibly account type (org or user)?
                        # This can be used downstream to configure org or user-specific API calls
                        # if any (hold off on the "type" config until we
                        # determine if there are different call ypes)
                        Repository.init()
                        Repository.add()
                        Repository.commit("Initial commit")
                        Repository.add_remote(resp.ssh_url)
                        alert_msg = 'Local repo linked to remote origin: \n\t{}'.format(resp.html_url)
                        self.log.info(alert_msg)
                        Repository.push()
                        self.log.info("First commit made locally and pushed to remote")
                        self.log.info("View the project on Github at {}".format(resp.html_url))
                    except GithubException as err:
                        try:
                            error_msg = err.data['errors'][0]['message']
                        except KeyError:
                            error_msg = err.data['message']
                        msg = "\nERROR: Failed to create {} for {}: {}!!\n".format(
                            self.project_slug,
                            target_account.login,
                            error_msg
                            )
                        self.log.error(msg)
