import pytest
import os
import sys
import json
import logging
import core.utils.logging as logger

def test_lload_logger():
    log_this = logger.load_logger('include-beer')
    log_this.info('test')
