from konlpy.tag import Kkma
from romanize import romanize
from utils import comb
import glossing
import sys


def main(sentence):
    if len(sentence) == 0:
        return sentence, '', '', ''
    romanized_by_words = []
    gloss_by_words = []
    whole_translated = glossing.trans(sentence)

    words = sentence.split(' ')
    morphs = morph_analysis(sentence)
    for word in morphs:
        romanized = [romanize(i[0]) for i in word]
        romanized_by_words.append(comb(romanized))

        glossed = (glossing.gloss(word))
        gloss_by_words.append(comb(glossed))

    whole_translated = f'\'{whole_translated}\''
    romanized_by_words[0] = romanized_by_words[0].capitalize()

    return sentence, romanized_by_words, gloss_by_words, whole_translated


def command_line_output(**kwargs):
    for key, value in kwargs.items():
        if type(value) == list:
            print_value = '\t\t'.join(value)
        else:
            print_value = value

        print(f'{key}:\t {print_value}')


def morph_analysis(sentence):
    words = Kkma().pos(sentence, flatten=False)
    return words


if sys.argv:
    sentence = ' '.join(sys.argv[1:])
    print(f'input:\t {sentence}')
    original, transliteration, glosses, translation = main(sentence)
    ## throw out the results to CLI
    command_line_output(Yale=transliteration,
                        gloss=glosses,
                        translation=translation)
