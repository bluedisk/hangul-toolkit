# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

from .const import CHO, JOONG, JONG, FIRST_HANGUL_UNICODE, NUM_CHO, NUM_JOONG, NUM_JONG
from .exception import NotHangulException

from six import unichr

################################################################################
# Decomposition & Combination
################################################################################

def compose(chosung, joongsung, jongsung=u''):
    """This function returns a Hangul letter by composing the specified chosung, joongsung, and jongsung.
    @param chosung
    @param joongsung
    @param jongsung the terminal Hangul letter. This is optional if you do not need a jongsung."""

    if jongsung is None: jongsung = u''

    try:
        chosung_index = CHO.index(chosung)
        joongsung_index = JOONG.index(joongsung)
        jongsung_index = JONG.index(jongsung)
    except Exception:
        raise NotHangulException('No valid Hangul character can be generated using given combination of chosung, joongsung, and jongsung.')

    return unichr(0xAC00 + chosung_index * NUM_JOONG * NUM_JONG + joongsung_index * NUM_JONG + jongsung_index)

def hangul_index(letter):
    return ord(letter) - FIRST_HANGUL_UNICODE

def decompose_index(code):
    jong = int(code % NUM_JONG)
    code /= NUM_JONG
    joong = int(code % NUM_JOONG)
    code /= NUM_JOONG
    cho = int(code)

    return (cho, joong, jong)


def decompose(hangul_letter):
    """This function returns letters by decomposing the specified Hangul letter."""

    from . import checker

    if len(hangul_letter) < 1:
        raise NotLetterException('')
    elif not checker.is_hangul(hangul_letter):
        raise NotHangulException('')

    if hangul_letter in CHO:
        return (hangul_letter, '', '')

    if hangul_letter in JOONG:
        return ('', hangul_letter, '')

    if hangul_letter in JONG:
        return ('', '', hangul_letter)


    code = hangul_index(hangul_letter)
    cho, joong, jong = decompose_index(code)

    if cho < 0:
        cho = 0

    try:
        return (CHO[cho], JOONG[joong], JONG[jong])
    except:
        print ("%d / %d  / %d"%(cho, joong, jong))
        print ("%s / %s " %( (JOONG[joong].encode("utf8"), JONG[jong].encode('utf8'))))
        raise Exception()
