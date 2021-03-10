# -*- coding: utf-8 -*-

from config import BASE_URL
from data.data import (
    BANCO_DE_CEPS
    )

from enum import Enum
from requests import get


class CepAPI:

    def buscar_cidade_por_cep(self, cep: int):
        '''
        Parameters
        ----------
        cep : int
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        url = BASE_URL.format(cep)        
        response = get(url)
        
        if response.status_code != 200:
            return None
        
        dados_cidade = response.json()  
        localidade = dados_cidade.get("localidade")
        
        return localidade
        
    
        
class CepLocal:
    
    def buscar_cidade_por_cep(self, cep: int):
        '''
        Parameters
        ----------
        cep : int
            DESCRIPTION.
    
        Returns
        -------
        TYPE
            DESCRIPTION.
        '''
        
        cidades_encontradas = BANCO_DE_CEPS[
            (BANCO_DE_CEPS['CEP Final'] >= cep) &
            (cep >= BANCO_DE_CEPS['CEP Inicial'])
            ]['Localidade'].reset_index(drop=True)
        
        if cidades_encontradas.shape[0] != 1:
            return None
        return cidades_encontradas[0]
    
    

class Origem(Enum):
    API = "api"
    LOCAL = "local"
    NOT_FOUND = "not_found"



def buscar_nome_cidade_por_cep(cep: int) -> str:
    '''
    Parameters
    ----------
    cep : int
        Cep da cidade a ser buscado.

    Returns
    -------
    Nome.
    '''
    
    localidade = CepLocal().buscar_cidade_por_cep(int(cep))
    
    if localidade is None:
        localidade = CepAPI().buscar_cidade_por_cep(str(cep))
        if localidade:
            origem = Origem.API
        else:
            localidade = ""
            origem = Origem.NOT_FOUND
    else:
        origem = Origem.LOCAL
    
    return {
        'cep': cep,
        'nome_cidade': localidade,
        'origem': origem.value
        }

