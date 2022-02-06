#importando a minh_lib inteira
import minh_lib
print(minh_lib.x)

#importando apenas a variavel x da minh_lib
from minh_lib import x
print(x)

#importando apenas a variavel x da minh_lib e dando outro nome a x
from minh_lib import x as k
x = 15
print(x)
print(k)

from minh_lib import soma_numero
y = soma_numero(2, 2)
print(y)

from minhas_funcoes.outras_funcoes import soma_numeros2
print(soma_numeros2(1, 4))