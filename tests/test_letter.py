# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

import hgtk


def test_compose():
    assert hgtk.letter.compose('ㄱ', 'ㅏ', 'ㅁ') == '감'


def test_decompose():
    assert hgtk.letter.decompose('감') == ('ㄱ', 'ㅏ', 'ㅁ')
