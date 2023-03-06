# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

import hgtk

DECOMPOSED = 'ㅎㅏㄱᴥㄱㅛᴥㅈㅗㅇᴥㅇㅣᴥ ㄸㅐㅇᴥㄸㅐㅇᴥㄸㅐㅇᴥ! hello world 1234567890 ㅋᴥㅋᴥ!'
COMPOSED = '학교종이 땡땡땡! hello world 1234567890 ㅋㅋ!'


def test_compose():
    print("compose", hgtk.text.compose(DECOMPOSED))
    assert hgtk.text.compose(DECOMPOSED) == COMPOSED


def test_decompose():
    print("decompose", hgtk.text.decompose(COMPOSED))
    assert hgtk.text.decompose(COMPOSED) == DECOMPOSED


def test_regresstion_pr_1():
    REGRESSION_EXAMPLE = 'ㅇㅓㅂㅅᴥㄷㅏᴥㅇㅣㅅㅅᴥㄷㅏᴥ'
    REGRESSION_RESULT = "없다있다"
    print("compose", hgtk.text.compose(REGRESSION_EXAMPLE))
    assert hgtk.text.compose(REGRESSION_EXAMPLE) == REGRESSION_RESULT
