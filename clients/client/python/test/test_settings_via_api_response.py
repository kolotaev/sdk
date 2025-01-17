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
from ory_client.model.identity import Identity
from ory_client.model.settings_flow import SettingsFlow
globals()['Identity'] = Identity
globals()['SettingsFlow'] = SettingsFlow
from ory_client.model.settings_via_api_response import SettingsViaApiResponse


class TestSettingsViaApiResponse(unittest.TestCase):
    """SettingsViaApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSettingsViaApiResponse(self):
        """Test SettingsViaApiResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SettingsViaApiResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
