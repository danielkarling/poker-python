'''
Created on 24/11/2014

@author: daniel
'''


'''
Carta eh Carta (Natiral [2, 14] , {"C", "E", "O", "P"})
'''

class Carta(object):
    
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        
'''Exemplos'''
nove_copas = Carta(9,"C")
dez_copas = Carta(12,"C")
valete_copas = Carta(11,"C")
dama_copas = Carta(12,"C")
rei_copas = Carta(13,"C")


'''funcoes auxiliares para texte'''

def string_to_mao (str):
    '''String -> mao
    Exemplo: "8C 9C DC JC QC" -> [Carta(8,"C"), Carta(9,"C"), Carta(10,"C"),
         Carta(11,"C"), Carta(12,"C")]'''
    
    return [Carta(char_to_valor(k[0]),k[1]) for k in str.split()]

def char_to_valor(char):
    return "--23456789DJQKA".index(char)

 

def print_carta(carta):
    for c in carta:
        print "Valor= "+str(c.valor)+" Naipe= "+c.naipe
 

'''
 Mao eh Lista de Carta
'''
'''Exemplo'''

straight_flush1= [dez_copas,valete_copas,dama_copas,rei_copas]
straight_flush2 = string_to_mao("8C 9C DC JC QC")
quadra1 = string_to_mao("4E 4C 4P 4O 6C")
full_house1 = string_to_mao("KE KC KP DC DP")
flush1 = string_to_mao("QP 8P 6P 4P 3P")
straigh1 = string_to_mao("2O 3P 4E 5O 6P")
trinca1 = string_to_mao("JP JC JO 5P 8O")
doi_pares1 = string_to_mao("DO DP 6E 6P KO")
um_par1 = string_to_mao("AC AP 8E 6O 2O")
carta_alta1 = string_to_mao("KC JE DP 6C 3O")


print char_to_valor("D")

print_carta (straight_flush2)



