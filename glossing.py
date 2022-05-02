from googletrans import Translator
from utils import csv

translator = Translator()
SYMBOLS = '{}()[].!?,:;+-*/&|<>=~‘’“”\'\"'


def trans(sentence):
    """

    :param sentence: Korean
    :return English translation:
    cf. Install googletrans-3.1.0a0 using pip3 install googletrans==3.1.0a0
    """
    if len(sentence) == 0:
        return ''
    return translator.translate(sentence, src='ko', dest='en').text


def gloss_content(morph):
    """
    For content morphemes, retrieve the base form and translate
    :param morph: tuple. (wordform, tag) e.g., ('들어가', 'V')
    :return: str. e.g., 'enter' (English translation of '들어가다')
    """
    if 'V' in morph[1]:
        baseform = morph[0]+'다'

    else:
        baseform = morph[0]

    if baseform in ['나','내']:
        return '1SG'
    elif baseform in ['우리']:
        return '1PL'
    elif baseform in ['너']:
        return '2SG'
    elif baseform in ['너희']:
        return '2PL'
    elif baseform in ['그','그녀']:
        return '3SG'
    elif baseform in ['그들','그녀들']:
        return '3PL'

    else:
        translated = trans(baseform)

    if ' ' in translated:
        translated = '.'.join(translated.split())

    return translated.lower()


def gloss(morphs):
    """

    :param morphs: the list of a morphs to be glossed. something like [('아버지', 'NNG'), ('께서', 'JKS')]
    :return: str 'Father-HON.NOM'
    """

    # see https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8 for tags
    tags, g = csv(path='tags.csv')
    translate_tags = []  # words to be translated e.g., nouns, verbs
    gloss_tags = tags  # words to be glossed e.g., josa (-kkeyse, or -ka)

    glossed_word = []
    for morpheme in morphs:
        if morpheme[0] in SYMBOLS:
            continue
        elif morpheme[1] in gloss_tags:
            if morpheme[1] == 'JKS' and morpheme[0] == '께서':  # special treatment for separating '께서' from '이/가'
                morpheme = list(morpheme)
                morpheme[1] = 'JKSH'
                morpheme = tuple(morpheme)
            if morpheme[1] == 'JX' and morpheme[0] in ['은', '는']:  # special treatment for the topic marker
                morpheme = list(morpheme)
                morpheme[1] = 'JXTP'
                morpheme = tuple(morpheme)
            if morpheme[1] == 'XSN' and morpheme[0] in ['들']:  # special treatment for pluralizer 들
                morpheme = list(morpheme)
                morpheme[1] = 'PLRL'
                morpheme = tuple(morpheme)
            glossed_word.append(g[gloss_tags.index(morpheme[1])])
        else:
            glossed_word.append(gloss_content(morpheme))

    return glossed_word
