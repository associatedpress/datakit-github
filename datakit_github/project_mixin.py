# -*- coding: utf-8 -*-
import logging
import os


from datakit import CommandHelpers


class ProjectMixin(CommandHelpers):

    "Mixin with code useful across plugin commands"

    plugin_slug = 'datakit-github'

    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)

    @property
    def project_slug(self):
        return os.path.basename(os.getcwd())
