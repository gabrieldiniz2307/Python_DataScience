# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BZ1EuN4GyOngAKcVSUy2LH4gcQWoAeO8
"""

import statistics as st

tempoLista = []
transporteLista = []

while True:
   tempo = int(input('Digite o tempo'))

   if tempo == 0:
    break

   tempoLista.append(tempo)
   transporte = str(input('Digite o transporte:'))

media = st.mean(tempoLista)
mediana = st.median(tempoLista)