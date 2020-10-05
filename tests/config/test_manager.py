import pytest
import os
import sys
import json
import core.config.manager as cfg_mgr
from core.utils.dicts import DotNotation as DotNotation


def test_config_mgr_class():
    os.environ["INCLUDE_BEER_CONFIG"] = ('%s/test_config.yml' % os.path.dirname(__file__))
    cfg = cfg_mgr.ConfigManager()
    print(DotNotation(cfg.operating_dict))

