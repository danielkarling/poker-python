'''
Created on 24/11/2014

@author: daniel
'''

''' Funcao poker auxiliares '''


class rank_mao(mao):
    '''
    mao->natural[1,9]
    
    retorna o rank da mao de acordo com as regras do poker
    ex.
    strainght_flush retorn 9
    quadra retorna 8
    .
    .
    .
    '''


def poker (maos):
    ''' 
    Lista de mão -> mão
    Retorna mão com maior Ranking
     '''
    return max(maos, key=rank_mao)
