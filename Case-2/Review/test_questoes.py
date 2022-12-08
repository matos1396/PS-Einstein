import pytest

from questao_1_review import questao_1
from questao_2_review import questao_2_A
from questao_3_review import questao_3

def test_questao_1():
    sut = questao_1(['aaa','bbb','ccc'],[3.00, 1.00, 4.00, 12.0], 9)

    assert sut == ['aaa', 'bbb', 'ccc']


valores_para_teste_questao_2 = [([1,2,3,3,4,5], 3), ([1,2,3,3,4,10,10,10,10,10,5], 10), ([0,0,0,0,1], 0), ([3,3,3,2,2,2,10,10,20,20,20], 20)]
@pytest.mark.parametrize("lista, expected", valores_para_teste_questao_2)
def test_questao_2_A(lista, expected):
    sut = questao_2_A(lista)

    assert sut == expected


valores_para_teste_questao_3 = [([0,5,6,7], 0), ([],0), ([1,2,3,4,5], 1), ([9,0,1,3,7,10,9,8], 20)]
@pytest.mark.parametrize("lista, expected", valores_para_teste_questao_3)
def test_questao_3(lista, expected):
    sut = questao_3(lista)

    assert sut == expected

