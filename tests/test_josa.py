# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

import hgtk


# 은/는
def test_eun_neun_1():
    assert hgtk.josa.attach('하늘', hgtk.josa.EUN_NEUN) == '하늘은'


def test_eun_neun_2():
    assert hgtk.josa.attach('바다', hgtk.josa.EUN_NEUN) == '바다는'


# 이/가
def test_i_ga_1():
    assert hgtk.josa.attach('하늘', hgtk.josa.I_GA) == '하늘이'


def test_i_ga_2():
    assert hgtk.josa.attach('바다', hgtk.josa.I_GA) == '바다가'


# 을/를
def test_eul_reul_1():
    assert hgtk.josa.attach('하늘', hgtk.josa.EUL_REUL) == '하늘을'


def test_eul_reul_2():
    assert hgtk.josa.attach('바다', hgtk.josa.EUL_REUL) == '바다를'


# 과/와
def test_gwa_wa_1():
    assert hgtk.josa.attach('하늘', hgtk.josa.GWA_WA) == '하늘과'


def test_gwa_wa_2():
    assert hgtk.josa.attach('바다', hgtk.josa.GWA_WA) == '바다와'


# 이다/다
def test_ida_da_1():
    assert hgtk.josa.attach('하늘', hgtk.josa.IDA_DA) == '하늘이다'


def test_ida_da_2():
    assert hgtk.josa.attach('바다', hgtk.josa.IDA_DA) == '바다다'


# 으로/로
def test_euro_ro_1():
    assert hgtk.josa.attach('하늘', hgtk.josa.EURO_RO) == '하늘로'


def test_euro_ro_2():
    assert hgtk.josa.attach('바다', hgtk.josa.EURO_RO) == '바다로'


def test_euro_ro_3():
    assert hgtk.josa.attach('태양', hgtk.josa.EURO_RO) == '태양으로'


# 률/율
def test_ryul_yul_1():
    assert hgtk.josa.attach('방어', hgtk.josa.RYUL_YUL) == '방어율'


def test_ryul_yul_2():
    assert hgtk.josa.attach('공격', hgtk.josa.RYUL_YUL) == '공격률'


def test_ryul_yul_3():
    assert hgtk.josa.attach('반환', hgtk.josa.RYUL_YUL) == '반환율'
