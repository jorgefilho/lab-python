#!/usr/bin/env python
# -*- coding: latin -*-
class Cesta:
    def __init__(self, conteudo=None):
        self.conteudo = conteudo or []

    def adicione(self, elemento):
        self.conteudo.append(elemento)

    def mostre_me(self):
        resultado = ""
        for elemento in self.conteudo:
            resultado = resultado + " " + `elemento`
        print "Contém:" + resultado



b = Cesta(['maçã', 'laranja'])
b.adicione("limão")
b.mostre_me()

print b
