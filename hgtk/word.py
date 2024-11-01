import re

## Ref
# 우리글진흥원: https://www.goodwriter.or.kr/bbs/board.php?bo_table=s0405&wr_id=25

def apply_dueum_rule(word):
    # 두음법칙 규칙
    dueum_rules = {
        '녀': '여', '뇨': '요', '뉴': '유', '니': '이',
        '랴': '야', '려': '여', '례': '예', '료': '요', '류': '유', '리': '이',
        '라': '나', '래': '내', '로': '노', '뢰': '뇌', '루': '누', '르': '느'
    }

    # 첫 두 글자가 두음법칙 대상인지 확인하고 적용
    first_two = word[:2]
    if first_two in dueum_rules:
        word = dueum_rules[first_two] + word[2:]

    # '렬, 률' 법칙 적용: 모음 또는 'ㄴ' 뒤에 오면 '열, 율'로 바뀜
    # 첫 글자가 아닌 경우에만 적용되므로 첫 글자가 아닌 위치에서만 확인
    for i in range(1, len(word) - 1):
        if word[i:i+2] == '렬':
            if word[i-1] in '모음목록' or word[i-1] == 'ㄴ':  # 여기서 '모음목록'은 실제로는 aeiou 모음 리스트로 변경 필요
                word = word[:i] + '열' + word[i+2:]
        elif word[i:i+2] == '률':
            if word[i-1] in '모음목록' or word[i-1] == 'ㄴ':
                word = word[:i] + '율' + word[i+2:]

    return word

# 테스트 예시
words = ['녀자', '랴년', '로인', '뉴대', '려사', '리발', '라면', '뇨소', '루각', '치렬', '선률', '나렬', '분률']
converted_words = [apply_dueum_rule(word) for word in words]

for original, converted in zip(words, converted_words):
    print(f"{original} -> {converted}")