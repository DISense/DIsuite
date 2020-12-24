__title__ = 'Pockill'
__version__ = '1.6.6'
__author__ = 'disenso.co Security Team'
__author_email__ = 's1@disense.co'
__license__ = 'GPL 2.0'
__copyright__ = 'Copyright 2020 disenso.co'
__name__ = 'pocsuite3'
__package__ = 'pocsuite3'

from .lib.core.common import set_paths
from .cli import module_path


set_paths(module_path())
