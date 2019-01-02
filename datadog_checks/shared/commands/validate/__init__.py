# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import click

from .py3 import py3
from ..console import CONTEXT_SETTINGS

ALL_COMMANDS = (
    py3,
)

@click.group(
    context_settings=CONTEXT_SETTINGS,
    short_help='Verify certain aspects of checks'
)
def validate():
    pass


for command in ALL_COMMANDS:
    validate.add_command(command)
