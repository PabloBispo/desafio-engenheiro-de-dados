#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:25:31 2021

@author: pablolbispo
"""

#import logging as log

import argparse
from multiprocessing import Pool
import pandas as pd

from time import time

from cep import buscar_nome_cidade_por_cep
from data.data import get_lista_ceps


parser = argparse.ArgumentParser()
parser.add_argument("-d", help="Path do arquivo .csv com a lista de CEPs")
parser.add_argument("-o", help="Nome do arquivo de saida.")

args = parser.parse_args()


if __name__ == '__main__':
    print("Iniciando o processamento...")

    saida_padrao = 'NomesCidades.csv'
    
    tempo_inicial = time()
    
    LISTA_DE_CEPS = get_lista_ceps("data/ceps.csv" if not args.d else args.d)
    
    p = Pool(8)
    busca_cidades = p.map(buscar_nome_cidade_por_cep, LISTA_DE_CEPS)
    p.close()
    
    saida = saida_padrao if not args.o else args.o

    df_cidades = pd.DataFrame(busca_cidades)
    df_cidades.to_csv(saida, index=False)
    
    print(f"Fim do processamento. {round(time() - tempo_inicial, 2)}s")
    print(f"Resultado salvo em \"{saida}\"")
