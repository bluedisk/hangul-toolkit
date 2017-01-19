# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

import hgtk

class Josa:
    EUN_NEUN = { 'not':u'은', 'has':'는', 'except': None }
    I_GA = { 'not':u'이', 'has':'가', 'except': None }
    EUL_REUL = { 'not':u'을', 'has':'를', 'except': None }
    GWA_WA = { 'not':u'과', 'has':'와', 'except': None }
    IDA_DA = { 'not':u'이다', 'has':'다', 'except': None }

    EURO_RO = { 'not': u'으로', 'has':u'로', 'except':u'ㄹ' }
    RYUL_YUL = { 'not': u'률', 'has':u'율', 'except':u'ㄴ' }


def test_eun_neun_1():
    assert hgtk.josa.attach('하늘', Josa.EUN_NEUN) == '하늘은'

def test_eun_neun_2():
    assert hgtk.josa.attach('바다', Josa.EUN_NEUN) == '바다는'

def test_i_ga_1():
    assert hgtk.josa.attach('하늘', Josa.I_GA) == '하늘이'

def test_i_ga_2():
    assert hgtk.josa.attach('바다', Josa.I_GA) == '바다가'

def test_eul_reul_1():
    assert hgtk.josa.attach('하늘', Josa.EUL_REUL) == '하늘을'

def test_eul_reul_2():
    assert hgtk.josa.attach('바다', Josa.EUL_REUL) == '바다를'

def test_gwa_wa_1():
    assert hgtk.josa.attach('하늘', Josa.GWA_WA) == '하늘과'

def test_gwa_wa_2():
    assert hgtk.josa.attach('바다', Josa.GWA_WA) == '바다와'

def test_ida_da_1():
    assert hgtk.josa.attach('하늘', Josa.IDA_DA) == '하늘이다'

def test_ida_da_2():
    assert hgtk.josa.attach('바다', Josa.IDA_DA) == '바다다'

def test_euro_ro_1():
    assert hgtk.josa.attach('하늘', Josa.EURO_RO) == '하늘로'

def test_euro_ro_2():
    assert hgtk.josa.attach('바다', Josa.EURO_RO) == '바다로'

def test_euro_ro_2():
    assert hgtk.josa.attach('태양', Josa.EURO_RO) == '태양으로'

def test_ryul_yul_1():
    assert hgtk.josa.attach('방어', Josa.RYUL_YUL) == '방어율'

def test_ryul_yul_2():
    assert hgtk.josa.attach('공격', Josa.RYUL_YUL) == '공격률'

def test_ryul_yul_3():
    assert hgtk.josa.attach('반환', Josa.RYUL_YUL) == '반환율'

