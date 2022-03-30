import pytest

from passageiro import Passageiro

def test_sem_passageiros():
    passageiro = Passageiro("Numero de passageiros", 0)
    assert passageiro.num_passageiros == 0

def test_um_passageiro():
    passageiro = Passageiro("Numero de passageiros", 0)
    passageiro.incluir_passageiro()
    assert passageiro.num_passageiros == 1

def test_dois_passageiro():
    passageiro = Passageiro("Numero de passageiros", 1)
    passageiro.incluir_passageiro()
    assert passageiro.num_passageiros == 2

def test_saida_passageiro():
    passageiro = Passageiro("Numero de passageiros", 1)
    passageiro.saida_passageiro()
    assert passageiro.num_passageiros == 0
