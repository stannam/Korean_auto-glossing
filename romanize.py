from hanutil import han_to_jamo
from utils import csv
import re

def romanize(w, method ='yale', bilabial_round=False):
    """
    romanize a Korean word
    :param w: str. word to be romanized
    :param method: str. romanization convention. default to yale. currently supports 'yale' and 'klattese'
    :param bilabial_round: bool. merge [u] to [ɯ] after [u] is illegal after a bilabial in Korean phonotactics.
    :return: str. string of transliterated Korean.
    """

    if method == 'yale':
        conventionfilename = 'yale.csv'
    elif method == 'ipa':
        conventionfilename = 'ipa.csv'
    elif method == 'klattese':
        conventionfilename = 'klattese.csv'  # default = klattese. to be changed if other conventions are added
    else:
        conventionfilename = 'yale.csv'

    jamo, alphabet = csv(conventionfilename)

    j = han_to_jamo(w)

    if bilabial_round is not True and 'ㅜ' in j:
        j = re.sub('ㅂㅜ', 'ㅂㅡ', j)
        j = re.sub('ㅍㅜ', 'ㅍㅡ', j)
        j = re.sub('ㅃㅜ', 'ㅃㅡ', j)
        j = re.sub('ㅁㅜ', 'ㅁㅡ', j)

    for i, character in enumerate(jamo):
        j = re.sub(character, alphabet[i], j)

    return j

if __name__ == '__main__':
    w = input('input')
    print(romanize(w))