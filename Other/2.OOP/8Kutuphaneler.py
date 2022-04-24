import numpy  as np
import matplotlib.pyplot as matplot
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
maasListesi=np.random.normal(4000,500,1000)
#4000 lira civarında,500tl standart sapmalı, 1000 tane veri oluştur(random)

print(np.mean(maasListesi)) #oluşan verilerin ortalamasını aldık


matplot.hist(maasListesi,50)
matplot.show()