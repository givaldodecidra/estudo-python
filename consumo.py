#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

kmI = float(raw_input("Digite a kilometragem inicial: ")) ## pega o valor da kilometragem inicial do carro
kmF = float(raw_input("Digite a kilometragem Final: ")) ## pega o valor da kilometragem final do carro
vl = float(raw_input("Digite o valor do combustível: ")) ## pega o valor do combustível
l = float(raw_input("Digite a quantidade de litros: ")) ## pega a quantidade em litros de combustível

r = kmF - kmI  # calcula a kilometragem rodada

valorpago = vl *l # valor pago pelo combustível

consumo = r / l  #calcula o consumo do carro

print("Informações:")
print('Kilometragem Inicial:', kmI,'km')
print('Kilometragem Final:', kmF,'km')
print('Valor do combustível: R$', vl)
print('Quantidade de Lítros de combustível:', l,'lt')

print("Resultados:")
print('Valor do Combustível: R$', valorpago)
print('O carro rodou: ', r, 'km')
print('O carro está fazendo: ', consumo, 'Km/lt')
