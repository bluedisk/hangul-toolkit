[![CircleCI](https://dl.circleci.com/status-badge/img/gh/bluedisk/hangul-toolkit/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/bluedisk/hangul-toolkit/tree/main)

Simple Toolkit for Hangul
=========================
base code forked from https://github.com/rhobot/Hangulpy

한글 자모 분해, 조합(오토마타), 조사 붙이기, 초/중/종 분해조합, 한글/한자/영문 여부 체크 등을 지원합니다.

## INSTALL
```
pip install hgtk
```

## Samples
### Letter
#### Decompose character
```python
>>> hgtk.letter.decompose('감')
('ㄱ', 'ㅏ', 'ㅁ')
```
#### Compose character
```python
>>> hgtk.letter.compose('ㄱ', 'ㅏ', 'ㅁ')
'감'
```

### Text
#### Decompose text
```python
>>> hgtk.text.decompose('학교종이 땡땡땡! hello world 1234567890 ㅋㅋ!')
'ㅎㅏㄱᴥㄱㅛᴥㅈㅗㅇᴥㅇㅣᴥ ㄸㅐㅇᴥㄸㅐㅇᴥㄸㅐㅇᴥ! hello world 1234567890 ㅋᴥㅋᴥ!'
```

기본 조합 완료 기호는 ᴥ이고, 아래와 같이 compose_code 옵션으로 변경 가능합니다.
```python
>>> hgtk.text.decompose('학교종이 땡땡땡! hello world 1234567890 ㅋㅋ!', compose_code='/')
'ㅎㅏㄱ/ㄱㅛ/ㅈㅗㅇ/ㅇㅣ/ㄸㅐㅇ/ㄸㅐㅇ/ㄸㅐㅇ/! hello world 1234567890 ㅋ/ㅋ/!'
```
기본 조합기호의 의미는 곰돌이 입니다. 👇  
<img src='https://user-images.githubusercontent.com/3307964/136328328-a5dea3b0-4731-48a5-881a-fae9b2c83dba.png' width=300/>

#### Compose text (Automata)
```python
>>> hgtk.text.compose('ㅎㅏㄱᴥㄱㅛᴥㅈㅗㅇᴥㅇㅣᴥ ㄸㅐㅇᴥㄸㅐㅇᴥㄸㅐㅇᴥ! hello world 1234567890 ㅋᴥㅋᴥ!')
'학교종이 땡땡땡! hello world 1234567890 ㅋㅋ!'
```

### Checker

#### is hangul text
```python
>>> hgtk.checker.is_hangul('한글입니다')
True
>>> hgtk.checker.is_hangul('no한글입니다')
False
>>> hgtk.checker.is_hangul('it is english')
False
```

#### is hanja text
```python
>>> hgtk.checker.is_hanja('大韓民國')
True
>>> hgtk.checker.is_hanja('大한민국')
False
>>> hgtk.checker.is_hanja('대한민국')
False
```

#### is latin1 text
```python
>>> hgtk.checker.is_latin1('abcdefghijklmnopqrstuvwxyz')
True
>>> hgtk.checker.is_latin1('한글latin1한')
False
````

#### has batchim
```python
>>> hgtk.checker.has_batchim('한')   # '한' has batchim 'ㄴ'
True
>>> hgtk.checker.has_batchim('하')
False
```


### Josa
#### EUN_NEUN - 은/는
```python
>>> hgtk.josa.attach('하늘', hgtk.josa.EUN_NEUN)
'하늘은'
>>> hgtk.josa.attach('바다', hgtk.josa.EUN_NEUN)
'바다는'
```
#### I_GA - 이/가
```python
>>> hgtk.josa.attach('하늘', hgtk.josa.I_GA)
'하늘이'
>>> hgtk.josa.attach('바다', hgtk.josa.I_GA)
'바다가'
```
#### EUL_REUL - 을/를 
```python
>>> hgtk.josa.attach('하늘', hgtk.josa.EUL_REUL)
'하늘을'
>>> hgtk.josa.attach('바다', hgtk.josa.EUL_REUL)
'바다를'
```
#### GWA_WA - 과/와 
```python
>>> hgtk.josa.attach('하늘', hgtk.josa.GWA_WA)
'하늘과'
>>> hgtk.josa.attach('바다', hgtk.josa.GWA_WA)
'바다와'
```
#### IDA_DA - 이다/다 
```python
>>> hgtk.josa.attach('하늘', hgtk.josa.IDA_DA)
'하늘이다'
>>> hgtk.josa.attach('바다', hgtk.josa.IDA_DA)
'바다다'
```
#### EURO_RO - 로/으로
```python
>>> hgtk.josa.attach('하늘', hgtk.josa.EURO_RO)
'하늘로'
>>> hgtk.josa.attach('바다', hgtk.josa.EURO_RO)
'바다로'
>>> hgtk.josa.attach('태양', hgtk.josa.EURO_RO)
'태양으로'
```
#### RYUL_YUL - 율/률
```python
>>> hgtk.josa.attach('방어', hgtk.josa.RYUL_YUL)
'방어율'
>>> hgtk.josa.attach('공격', hgtk.josa.RYUL_YUL)
'공격률'
>>> hgtk.josa.attach('반환', hgtk.josa.RYUL_YUL)
'반환율'
```

### Const
* CHO: 초성 리스트
* JOONG: 중성 리스트
* JONG: 종성 리스트, 종성이 없는 경우를 대비해 공백 문자가 추가됨

* JAMO: 공백을 제외한 모든 자모(비조합문자)

* NUM_CHO: 초성 개수
* NUM_JOONG: 중성 개수
* NUM_JONG: 종성 개수 

* FIRST_HANGUL_UNICODE: 유니코드 상의 한글 코드(조합문자) 시작 시점
* LAST_HANGUL_UNICODE: 유니코드 상의 한글 코드(조합문자) 종료 시점 

### Exception
예외 처리를 위한 Exception들, 의미는 보이는 대로..
* NotHangulException
* NotLetterException
* NotWordException


## Tested in
- python 2.7

- python 3.7
- python 3.8
- python 3.9
- python 3.10
- python 3.11
- python 3.12

- PyPy 2.x
- PyPy 3.x


----

Apache 2.0 License
