# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

from . import letter as lt
from .exception import NotHangulException
from .const import CHO, JOONG, JONG, JAMO, FIRST_HANGUL_UNICODE, LAST_HANGUL_UNICODE, NUM_JONG

import re

# 한자와 라틴 문자 범위 by bluedisk
FIRST_HANJA_UNICODE = 0x4E00
LAST_HANJA_UNICODE = 0x9FFF

FIRST_HANJA_EXT_A_UNICODE = 0x3400
LAST_HANJA_EXT_A_UNICODE = 0x4DBF

FIRST_LATIN1_UNICODE = 0x0000 # NUL
LAST_LATIN1_UNICODE = 0x00FF # 'ÿ'
# EXT B~E 는 무시

################################################################################
# Boolean Hangul functions
################################################################################


def is_hangul(phrase): # TODO: need tuning!!
    for letter in phrase:
        code = ord(letter)
        if (code < FIRST_HANGUL_UNICODE or code > LAST_HANGUL_UNICODE) and not is_jamo(letter):
            return False

    return True


def is_jamo(letter):
    return letter in JAMO


def is_hanja(phrase):
    for unicode_value in map(lambda letter:ord(letter), phrase):
        if ((unicode_value < FIRST_HANJA_UNICODE or unicode_value > LAST_HANJA_UNICODE) and
            (unicode_value < FIRST_HANJA_EXT_A_UNICODE or unicode_value > LAST_HANJA_EXT_A_UNICODE)):
            return False
    return True

def is_latin1(phrase):
    for unicode_value in map(lambda letter:ord(letter), phrase):
        if unicode_value < FIRST_LATIN1_UNICODE or unicode_value > LAST_LATIN1_UNICODE:
            return False
    return True


def has_jongsung(letter):
    """Check whether this letter contains Jongsung"""
    if len(letter) != 1:
        raise Exception('The target string must be one letter.')
    if not is_hangul(letter):
        raise NotHangulException('The target string must be Hangul')

    code = lt.hangul_index(letter)
    return code % NUM_JONG > 0

def has_batchim(letter):
    """This method is the same as has_jongsung()"""
    return has_jongsung(letter)

def has_approximant(letter):
    """Approximant makes complex vowels, such as ones starting with y or w.
    In Korean there is a unique approximant euㅡ making uiㅢ, but ㅢ does not make many irregularities."""
    if len(letter) != 1:
        raise Exception('The target string must be one letter.')
    if not is_hangul(letter):
        raise NotHangulException('The target string must be Hangul')

    jaso = lt.decompose(letter)
    diphthong = (u'ㅑ',u'ㅒ',u'ㅕ',u'ㅖ',u'ㅘ',u'ㅙ',u'ㅛ',u'ㅝ',u'ㅞ',u'ㅠ')
    # excluded 'ㅢ' because y- and w-based complex vowels are irregular.
    # vowels with umlauts (ㅐ, ㅔ, ㅚ, ㅟ) are not considered complex vowels.
    return jaso[1] in diphthong

