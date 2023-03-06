# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

import hgtk


# hangul test - true/false
def test_is_hangul_1():
    assert hgtk.checker.is_hangul('한글입니다')


def test_is_hangul_2():
    assert not hgtk.checker.is_hangul('no한글입니다')


# hanja test - true/false
def test_is_hanja_1():
    assert hgtk.checker.is_hanja('大韓民國')


def test_is_hanja_2():
    assert not hgtk.checker.is_hanja('大한민국')


# latin test - true/false
def test_is_latin1_1():
    assert hgtk.checker.is_latin1('abcdefghijklmnopqrstuvwxyz')


def test_is_latin1_2():
    assert not hgtk.checker.is_latin1('한글latin1한')


# batchim test - true/false
def test_has_batchim_1():
    assert hgtk.checker.has_batchim('한')


def test_has_batchim_2():
    assert not hgtk.checker.has_batchim('하')

# DEPRECATED! - not a general function
# def test_has_approximant_1():
#     assert hgtk.checker.has_approximant('롹')

# def test_has_approximant_2():
#     assert hgtk.checker.has_approximant('락') == False
