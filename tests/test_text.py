# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

import hgtk

DECOMPOSED = 'ㅎㅏㄱᴥㄱㅛᴥㅈㅗㅇᴥㅇㅣᴥ ㄸㅐㅇᴥㄸㅐㅇᴥㄸㅐㅇᴥ! hello world 1234567890 ㅋᴥㅋᴥ!'
COMPOSED = '학교종이 땡땡땡! hello world 1234567890 ㅋㅋ!'


def test_compose():
    print ("compose", hgtk.text.compose(DECOMPOSED))
    assert hgtk.text.compose(DECOMPOSED) == COMPOSED


def test_decompose():
    print ("decompose", hgtk.text.decompose(COMPOSED))
    assert hgtk.text.decompose(COMPOSED) == DECOMPOSED
