from lib2to3.pgen2.pgen import DFAState
from bank import *



def home_():
   home= print("Olá, Seja bem vindo !\n")

def menu_():
    menu =(input("Informe o tipo do arquivo : \n"+
                   "<X> - Execel.xlsx : \n"+
                   "<C> - execel.csv : \n"+
                   "<J> - json : \n"+                
                   "<E> - Para Sair : \n")).upper()
    return menu

def acao():
    item =(input("O que deseja realizar ? : \n"+
                   "<W> - Abrir o Arquivo ? : \n"+
                   "<G> - Grafico Qunatidade de vendas por ID : \n"+
                   "<I> - Grafico Qunatidade de vendas por Ano : \n"+                
                   "<E> - Para Sair : \n")).upper()
    return item 

