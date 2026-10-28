from utils import saudacao


def test_saudacao_returns_name_in_greeting():
    assert saudacao('Julia') == 'Olá Julia'


def test_saudacao_accepts_empty_name():
    assert saudacao('') == 'Olá '
