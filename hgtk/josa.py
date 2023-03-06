# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

from . import letter
from .exception import NotHangulException

################################################################################
# Josa Type Parameters
################################################################################

EUN_NEUN = {'not': u'은', 'has': '는', 'except': None}
I_GA = {'not': u'이', 'has': '가', 'except': None}
EUL_REUL = {'not': u'을', 'has': '를', 'except': None}
GWA_WA = {'not': u'과', 'has': '와', 'except': None}
IDA_DA = {'not': u'이다', 'has': '다', 'except': None}

EURO_RO = {'not': u'으로', 'has': u'로', 'except': u'ㄹ'}
RYUL_YUL = {'not': u'률', 'has': u'율', 'except': u'ㄴ'}

JOSA_TYPES = (EUN_NEUN, I_GA, EUL_REUL, GWA_WA, IDA_DA, EURO_RO, RYUL_YUL)
JOSAS = dict(sum([[[josa['not'], josa], [josa['has'], josa]] for josa in JOSA_TYPES], []))


################################################################################
# Josa functions
################################################################################

def get_josa_type(word):
    return JOSAS.get(word, None)


def attach(word, josa=EUN_NEUN):
    """add josa at the end of this word"""
    last_letter = word.strip()[-1]
    try:
        _, _, letter_jong = letter.decompose(last_letter)
    except NotHangulException:
        letter_jong = letter.get_substituent_of(last_letter)

    if letter_jong in ('', josa['except']):
        return word + josa['has']

    return word + josa['not']
