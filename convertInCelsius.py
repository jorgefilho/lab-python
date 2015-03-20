#!/usr/bin/env python
# -*- coding: latin -*-
def convertInCelsius(value):
	f = (value-32)*5.0/9.0
	return f


temp = float(raw_input('Entre com a temperatura em Fahrenheit: '))

f = convertInCelsius(temp)
print "Temperatura em Celsius: ", f