# -*- coding: utf-8 -*-
"""BiblioStatistics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X40vulyyUMTQ2mvUjqVkYko5gFp1IDPF
"""

import statistics as st
notas = [7.5, 8.2, 6.9, 9.5, 5.8, 7.1, 8.6, 6.3,
         9.0, 8.8]

mediana=st.mean(notas)

media=st.median(notas)

moda=st.mode(notas)

desvio_padrao=st.stdev(notas)

print('Conjunto de Dados:', notas)
print('Media:', media)
print('Mediana:', mediana)
print('Moda:', moda)
print('Desvio_padrao:', desvio_padrao)