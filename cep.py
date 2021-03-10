# -*- coding: utf-8 -*-

from config import (
    BASE_URL_VIACEP,
    BASE_URL_BRASIL_API
    )
from data.data import (
    BANCO_DE_CEPS
    )

from enum import Enum
import requests

requests.adapters.DEFAULT_RETRIES = 1


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
        URL_VIACEP = BASE_URL_VIACEP.format(cep)     
        URL_BRASIL_API = BASE_URL_BRASIL_API.format(cep)     
        
        try:
            use_brasil_api = False
            response = requests.get(BASE_URL_VIACEP, timeout = 2)
            
        except:
            response = requests.get(URL_BRASIL_API)
            use_brasil_api = True
        
        if response.status_code != 200:
            return None
        
        dados_cidade = response.json()  

        localidade = dados_cidade.get("localidade") if (
            not use_brasil_api
            ) else dados_cidade.get("city")
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
        try:
            localidade = CepAPI().buscar_cidade_por_cep(str(cep))
        except:
            localidade = ""
        if localidade:
            origem = Origem.API
        else:
            localidade = ""
            origem = Origem.NOT_FOUND
    else:
        origem = Origem.LOCAL
    print(f'{cep} -> {localidade}')
    return {
        'cep': cep,
        'nome_cidade': localidade,
        'origem': origem.value
        }

