# -*- coding: utf-8 -*-
# %load Hangulpy/Hangulpy.py
#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from __future__ import division

import hgtk

def test_compose():
    assert hgtk.letter.compose('ㄱ', 'ㅏ', 'ㅁ') == '감'

def test_decompose():
    assert hgtk.letter.decompose('감') == ('ㄱ', 'ㅏ', 'ㅁ')

