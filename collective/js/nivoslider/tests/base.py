"""Test setup for registration and functional tests."""

import sys
from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_addon():
    fiveconfigure.debug_mode = True
    import collective.js.nivoslider
    zcml.load_config('configure.zcml', collective.js.nivoslider)
    fiveconfigure.debug_mode = False
    ztc.installPackage('collective.js.nivoslider')

setup_addon()
ptc.setupPloneSite(extension_profiles=['collective.js.nivoslider:default'])

class TestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here. This applies to unit 
    test cases.
    """


class FunctionalTestCase(ptc.FunctionalTestCase):
    """We use this class for functional integration tests that use doctest
    syntax. Again, we can put basic common utility or setup code in here.
    """

