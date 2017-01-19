# -*- coding: utf-8 -*-
# %load Hangulpy/Hangulpy.py
#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from __future__ import division

from six import unichr
import string

################################################################################
# Hangul Unicode Variables
################################################################################

# Code = 0xAC00 + (Chosung_index * NUM_JOONG * NUM_JONG) + (Joongsung_index * NUM_JONG) + (Jongsung_index)
CHO = [u'ㄱ',u'ㄲ',u'ㄴ',u'ㄷ',u'ㄸ',u'ㄹ',u'ㅁ',u'ㅂ',u'ㅃ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅉ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
JOONG = [u'ㅏ',u'ㅐ',u'ㅑ',u'ㅒ',u'ㅓ',u'ㅔ',u'ㅕ',u'ㅖ',u'ㅗ',u'ㅘ',u'ㅙ',u'ㅚ',u'ㅛ',u'ㅜ',u'ㅝ',u'ㅞ',u'ㅟ',u'ㅠ',u'ㅡ',u'ㅢ',u'ㅣ']
JONG = [u'',u'ㄱ',u'ㄲ',u'ㄳ',u'ㄴ',u'ㄵ',u'ㄶ',u'ㄷ',u'ㄹ',u'ㄺ',u'ㄻ',u'ㄼ',u'ㄽ',u'ㄾ',u'ㄿ',u'ㅀ',u'ㅁ',u'ㅂ',u'ㅄ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']

# 코딩 효율과 가독성을 위해서 index대신 unicode사용 by bluedisk
JONG_COMP = {
    u'ㄱ':{
        u'ㄱ': u'ㄲ',
        u'ㅅ': u'ㄳ',
    },
    u'ㄴ':{
        u'ㅈ': u'ㄵ',
        u'ㅎ': u'ㄶ',
    },
    u'ㄹ':{
        u'ㄱ': u'ㄺ',
        u'ㅁ': u'ㄻ',
        u'ㅂ': u'ㄼ',
        u'ㅅ': u'ㄽ',
        u'ㅌ': u'ㄾ',
        u'ㅍ': u'ㄿ',
        u'ㅎ': u'ㅀ',
    }
}

NUM_CHO = len(CHO)
NUM_JOONG = len(JOONG)
NUM_JONG = len(JONG)

FIRST_HANGUL_UNICODE = 0xAC00 #'가'
LAST_HANGUL_UNICODE = 0xD7A3 #'힣'

# 한자와 라틴 문자 범위 by bluedisk
FIRST_HANJA_UNICODE = 0x4E00
LAST_HANJA_UNICODE = 0x9FFF

FIRST_HANJA_EXT_A_UNICODE = 0x3400
LAST_HANJA_EXT_A_UNICODE = 0x4DBF

FIRST_LATIN1_UNICODE = 0x0000 # NUL
LAST_LATIN1_UNICODE = 0x00FF # 'ÿ'

# EXT B~E 는 무시

################################################################################
# Hangul Automata functions by bluedisk@gmail.com
################################################################################
DEFAULT_COMPOSE_CODE = u'ᴥ'

def decompose_text(text, latin_filter=True, compose_code=DEFAULT_COMPOSE_CODE):
    result=u""

    for c in list(text):
        if is_hangul(c):

            result = result + "".join(decompose(c)) + compose_code

        else:
            if latin_filter:    # 한글 외엔 Latin1 범위까지만 포함 (한글+영어)
                if is_latin1(c):
                    result = result + c
            else:
                result = result + c

    return result

def automata(text):
    res_text = u""
    status="CHO"

    for c in text:

        if status == "CHO":

            if c in CHO:
                chosung = c
                status="JOONG"
            else:
                if c != COMPOSE_CODE:

                    res_text = res_text + c

        elif status == "JOONG":

            if c != COMPOSE_CODE and c in JOONG:
                joongsung = c
                status="JONG1"
            else:
                res_text = res_text + chosung

                if c in CHO:
                    chosung = c
                    status="JOONG"
                else:
                    if c != COMPOSE_CODE:

                        res_text = res_text + c
                    status="CHO"

        elif status == "JONG1":

            if c != COMPOSE_CODE and c in JONG:
                jongsung = c

                if c in JONG_COMP:
                    status="JONG2"
                else:
                    res_text = res_text + compose(chosung, joongsung, jongsung)
                    status="CHO"

            else:
                res_text = res_text + compose(chosung, joongsung)

                if c in CHO:
                    chosung = c
                    status="JOONG"
                else:
                    if c != COMPOSE_CODE:

                        res_text = res_text + c

                    status="CHO"

        elif status == "JONG2":

            if c != COMPOSE_CODE and c in JONG_COMP[jongsung]:
                jongsung = JONG_COMP[jongsung][c]
                c = COMPOSE_CODE # 종성 재 출력 방지

            res_text = res_text + compose(chosung, joongsung, jongsung)

            if c != COMPOSE_CODE:

                res_text = res_text + c

            status="CHO"


    return res_text

################################################################################
# Boolean Hangul functions
################################################################################

def is_hangul(phrase):
    """Check whether the phrase is Hangul.
    This method ignores white spaces, punctuations, and numbers.
    @param phrase a target string
    @return True if the phrase is Hangul. False otherwise."""

    # If the input is only one character, test whether the character is Hangul.
    if len(phrase) == 1: return is_all_hangul(phrase)

    # Remove all white spaces, punctuations, numbers.
    exclude = set(string.whitespace + string.punctuation + '0123456789')
    phrase = ''.join(ch for ch in phrase if ch not in exclude)

    return is_all_hangul(phrase)

def is_all_hangul(phrase):
    """Check whether the phrase contains all Hangul letters
    @param phrase a target string
    @return True if the phrase only consists of Hangul. False otherwise."""

    for unicode_value in map(lambda letter:ord(letter), phrase):
        if unicode_value < FIRST_HANGUL_UNICODE or unicode_value > LAST_HANGUL_UNICODE:
            # Check whether the letter is chosungs, joongsungs, or jongsungs.
            if unicode_value not in map(lambda v: ord(v), CHO + JOONG + JONG[1:]):
                return False
    return True

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

    unicode_value = ord(letter)
    return (unicode_value - FIRST_HANGUL_UNICODE) % NUM_JONG > 0

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

    jaso = decompose(letter)
    diphthong = (2, 3, 6, 7, 9, 10, 12, 14, 15, 17)
    # [u'ㅑ',u'ㅒ',',u'ㅕ',u'ㅖ',u'ㅘ',u'ㅙ',u'ㅛ',u'ㅝ',u'ㅞ',u'ㅠ']
    # excluded 'ㅢ' because y- and w-based complex vowels are irregular.
    # vowels with umlauts (ㅐ, ㅔ, ㅚ, ㅟ) are not considered complex vowels.
    return jaso[1] in diphthong

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

def hangul_index(hangul_letter):
    
    if len(hangul_letter) < 1:
        raise NotLetterException('')
    elif not is_hangul(hangul_letter):
        raise NotHangulException('')
        
    return ord(hangul_letter) - FIRST_HANGUL_UNICODE

def extract_jamo_from_index(hangul_index):
    code = ord(hangul_letter) - FIRST_HANGUL_UNICODE
    jong = int(code % NUM_JONG)
    code /= NUM_JONG
    joong = int(code % NUM_JOONG)
    code /= NUM_JOONG
    cho = int(code)
    
    return (cho, joong, jong)


def decompose(hangul_letter):
    """This function returns letters by decomposing the specified Hangul letter."""

    code = hangul_index(hangul_letter)
    cho, joong, jong = extract_jamo_from_index(code)

    if cho < 0:
        cho = 0

    try:
        return (CHO[cho], JOONG[joong], JONG[jong])
    except:
        print ("%d / %d  / %d"%(cho, joong, jong))
        print ("%s / %s " %( (JOONG[joong].encode("utf8"), JONG[jong].encode('utf8'))))
        raise Exception()


################################################################################
# Josa functions
################################################################################


# avail josa list

class Josa:
    eun_neun = { 'not':u'은', 'has':'는', 'except': None }
    i_ga = { 'not':u'이', 'has':'가', 'except': None }
    eul_reul = { 'not':u'을', 'has':'를', 'except': None }
    gwa_wa = { 'not':u'과', 'has':'와', 'except': None }
    ida_da = { 'not':u'이다', 'has':'다', 'except': None }
    
    euro_ro = { 'not': u'으로', 'has':u'로', 'except':u'ㄹ' }
    ryul_yul = { 'not': u'률', 'has':u'율', 'except':u'ㄴ' }

    
def attach_josa(word, josa=Josa.eun_neun):
    """add josa at the end of this word"""
    last_letter = word.strip()[-1]
    
    jong_except = JONG.index(josa['except']) if josa['except'] or -1
    letter_jong = extract_jamo(last_letter)[2]
    
    if letter_jong in (0, jong_except):
        return word + josa['has']
    
    return word + josa['not']


################################################################################
# Exceptions
################################################################################

class NotHangulException(Exception):
    pass

class NotLetterException(Exception):
    pass

class NotWordException(Exception):
    pass
