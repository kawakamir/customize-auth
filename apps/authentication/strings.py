import re
import string
import random

ALPHABETS = string.digits + string.ascii_letters


def randstr(n):
    """ ランダムな文字列を指定された文字数で生成する　"""
    return ''.join(random.choice(ALPHABETS) for i in range(n))


class Strings:
    @staticmethod
    def is_alphabet(source):
        return re.fullmatch("[0-9a-zA-Z\-_\s]*$", source)

    @staticmethod
    def is_kana(source):
        return re.fullmatch("[ァ-ヴｦ-ﾟ]*$", source)
