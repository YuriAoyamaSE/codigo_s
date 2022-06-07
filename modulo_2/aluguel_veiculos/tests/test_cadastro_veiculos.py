

import pytest
from src.business.cadastro_veiculo import CadastroVeiculo
from src.entities.veiculo import Veiculo


def test_retorno_inserir():
    # Dado
    veiculo = Veiculo()
    cadastro = CadastroVeiculo()
    
    # Quando
    resultado = cadastro.inserir(veiculo)
    
    # Entao
    assert resultado

def test_inserir_veiculo_placa():
    # dado
    veiculo = Veiculo("1235", "test", 1)
    
    #quando    
    #então
    with pytest.raises(AttributeError):
        veiculo.placa = 'teste'
    
def test_inserir_veiculo_km():
    # dado
    veiculo = Veiculo("1235", "test", 1)
    
    #quando    
    #então
    with pytest.raises(AttributeError):
        veiculo.km = 1.1

        
def test_inserir_veiculo_id():
    # dado
    veiculo = Veiculo("1235", "test", 1)
    
    #quando    
    #então
    with pytest.raises(AttributeError):
        veiculo.id = '12345'
        