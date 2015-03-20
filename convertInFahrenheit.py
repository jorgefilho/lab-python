#!/usr/bin/env python
# -*- coding: latin -*-
def convertInFahrenheit(value):
	f = (9/5)*value+32
	return f


temp = float(raw_input('Entre com a temperatura em Celsius: '))

f = convertInFahrenheit(temp)
print f