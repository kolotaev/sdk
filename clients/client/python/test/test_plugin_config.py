"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.3
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.plugin_config_args import PluginConfigArgs
from ory_client.model.plugin_config_interface import PluginConfigInterface
from ory_client.model.plugin_config_linux import PluginConfigLinux
from ory_client.model.plugin_config_network import PluginConfigNetwork
from ory_client.model.plugin_config_rootfs import PluginConfigRootfs
from ory_client.model.plugin_config_user import PluginConfigUser
from ory_client.model.plugin_env import PluginEnv
from ory_client.model.plugin_mount import PluginMount
globals()['PluginConfigArgs'] = PluginConfigArgs
globals()['PluginConfigInterface'] = PluginConfigInterface
globals()['PluginConfigLinux'] = PluginConfigLinux
globals()['PluginConfigNetwork'] = PluginConfigNetwork
globals()['PluginConfigRootfs'] = PluginConfigRootfs
globals()['PluginConfigUser'] = PluginConfigUser
globals()['PluginEnv'] = PluginEnv
globals()['PluginMount'] = PluginMount
from ory_client.model.plugin_config import PluginConfig


class TestPluginConfig(unittest.TestCase):
    """PluginConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPluginConfig(self):
        """Test PluginConfig"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PluginConfig()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
