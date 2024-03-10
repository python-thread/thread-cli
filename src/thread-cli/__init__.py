"""
## ThreadCLI Library
Documentation: https://thread.ngjx.org


---

Released under the GPG-3 License

Copyright (c) 2020, thread.ngjx.org. All rights reserved.
"""

__version__ = '0.1.1'
from .utils.logging import ColorLogger, logging

# Export Core
from .base import cli_base as app
from .process import process as process_cli

app.command(
  name='process',
  no_args_is_help=True,
  context_settings={'allow_extra_args': True},
)(process_cli)


# Setup Logging
logging.setLoggerClass(ColorLogger)


# Wildcard export
__all__ = ['app']
