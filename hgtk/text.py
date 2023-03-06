# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

from . import checker
from . import letter
from .const import CHO, JOONG, JONG

# 코딩 효율과 가독성을 위해서 index대신 unicode사용 by bluedisk
JONG_COMP = {
    u'ㄱ': {
        u'ㄱ': u'ㄲ',
        u'ㅅ': u'ㄳ',
    },
    u'ㄴ': {
        u'ㅈ': u'ㄵ',
        u'ㅎ': u'ㄶ',
    },
    u'ㄹ': {
        u'ㄱ': u'ㄺ',
        u'ㅁ': u'ㄻ',
        u'ㅂ': u'ㄼ',
        u'ㅅ': u'ㄽ',
        u'ㅌ': u'ㄾ',
        u'ㅍ': u'ㄿ',
        u'ㅎ': u'ㅀ',
    },
    u"ㅂ": {
        u"ㅅ": u"ㅄ",
    },
    u"ㅅ": {
        u"ㅅ": u"ㅆ",
    },
}

DEFAULT_COMPOSE_CODE = u'ᴥ'


################################################################################
# Hangul Automata functions by bluedisk@gmail.com
################################################################################


def decompose(text, latin_filter=True, compose_code=DEFAULT_COMPOSE_CODE):
    result = u""

    for c in list(text):
        if checker.is_hangul(c):

            if checker.is_jamo(c):
                result = result + c + compose_code
            else:
                result = result + "".join(letter.decompose(c)) + compose_code

        else:
            if latin_filter:  # 한글 외엔 Latin1 범위까지만 포함 (한글+영어)
                if checker.is_latin1(c):
                    result = result + c
            else:
                result = result + c

    return result


STATUS_CHO = 0
STATUS_JOONG = 1
STATUS_JONG1 = 2
STATUS_JONG2 = 3


def compose(text, compose_code=DEFAULT_COMPOSE_CODE):
    res_text = u""

    status = STATUS_CHO

    for c in text:

        if status == STATUS_CHO:

            if c in CHO:
                chosung = c
                status = STATUS_JOONG
            else:
                if c != compose_code:
                    res_text = res_text + c

        elif status == STATUS_JOONG:

            if c != compose_code and c in JOONG:
                joongsung = c
                status = STATUS_JONG1
            else:
                res_text = res_text + chosung

                if c in CHO:
                    chosung = c
                    status = STATUS_JOONG
                else:
                    if c != compose_code:
                        res_text = res_text + c
                    status = STATUS_CHO

        elif status == STATUS_JONG1:

            if c != compose_code and c in JONG:
                jongsung = c

                if c in JONG_COMP:
                    status = STATUS_JONG2
                else:
                    res_text = res_text + letter.compose(chosung, joongsung, jongsung)
                    status = STATUS_CHO

            else:
                res_text = res_text + letter.compose(chosung, joongsung)

                if c in CHO:
                    chosung = c
                    status = STATUS_JOONG
                else:
                    if c != compose_code:
                        res_text = res_text + c

                    status = STATUS_CHO

        elif status == STATUS_JONG2:

            if c != compose_code and c in JONG_COMP[jongsung]:
                jongsung = JONG_COMP[jongsung][c]
                c = compose_code  # 종성 재 출력 방지

            res_text = res_text + letter.compose(chosung, joongsung, jongsung)

            if c != compose_code:
                res_text = res_text + c

            status = STATUS_CHO

    return res_text
