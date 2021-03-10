# -*- coding: utf-8 -*-

from functools import partial
import pandas as pd
from os import path
import re


_get_numbers_only = partial(re.sub, '[^0-9]', '')


def get_lista_ceps(path_: str):
    assert path.exists(path_), f'Caminho inválido: {path_}'
    LISTA_DE_CEPS = pd.read_csv(path_)
    LISTA_DE_CEPS = LISTA_DE_CEPS['zipcode'].apply(_get_numbers_only)
    return LISTA_DE_CEPS


def _get_banco_de_ceps(path_ : str = "data/Banco_ceps.xlsx"):
    BANCO_DE_CEPS = pd.read_excel(path_)
    return BANCO_DE_CEPS


BANCO_DE_CEPS = _get_banco_de_ceps()