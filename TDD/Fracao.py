# fracao.py
import math

class Fracao:
  def __init__(self, numerador, denominador):
    if denominador == 0:
      raise ValueError('Denominador deve ser diferente de zero')
    # reduzindo numerador e denominador
    #mdc = self._mdc(numerador, denominador)
    #mdc = 1
    self._numerador = numerador / math.gcd(numerador, denominador)
    self._denominador = denominador / math.gcd(numerador, denominador)
 
  #def _mdc(self, a, b):
  #  mdc = 1
  #  for i in range(min(a, b), 1, -1):
  #    if a % i == 0 and b % i == 0:
  #      mdc = i
  #      break
  #  return mdc
 
  @property
  def numerador(self):
    return self._numerador

  @property
  def denominador(self):
    return self._denominador


