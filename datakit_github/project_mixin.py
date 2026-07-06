# -*- coding: utf-8 -*-
import logging
import os


from datakit import CommandHelpers, ConfigField


class ProjectMixin(CommandHelpers):

    "Mixin with code useful across plugin commands"

    plugin_slug = 'datakit-github'

    config_spec = [
        ConfigField(
            'github_api_key',
            required=True,
            secret=True,
            help='GitHub personal access token (repo scope)',
        ),
    ]

    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)

    @property
    def project_slug(self):
        return os.path.basename(os.getcwd())
