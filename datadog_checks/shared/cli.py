# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import click

from .commands import ALL_COMMANDS
from .commands.console import CONTEXT_SETTINGS


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def ddshared():
    pass


for command in ALL_COMMANDS:
    ddshared.add_command(command)
