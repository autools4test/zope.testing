##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Sample tests with a layer that produces output on stderr

$Id$
"""

import unittest
from zope.testing import doctest
import sys


sys.stderr.write('A message on stderr.\n')


class Layer:

    def setUp(self):
        pass
    setUp = classmethod(setUp)

    def tearDown(self):
        pass
    tearDown = classmethod(tearDown)


def test_something():
    """
    >>> 1 + 1
    2
    """


def test_suite():
    suite = unittest.TestSuite()
    d = doctest.DocTestSuite()
    d.layer = Layer
    suite.addTest(d)
    return suite


if __name__ == '__main__':
    unittest.main()