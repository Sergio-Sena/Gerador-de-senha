#Gerador de senha
#Importar Biblioteca Random para Randomizar
import random
#variavel para Letras maiúscula
para_maiúscula = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
#variavel para Letras maiúscula
para_minúsculo = 'abcdefghijklmnopqrstuvxwyz'
#variavel para Simbolos
para_simbolos = '!#$%&\?/'
#variavel para Números
para_números = '0123456789'
#Itens para Randomizar
use = para_minúsculo+para_maiúscula+para_números+para_simbolos
# Digitos para senha de 8 caracteres
tamanho_da_senha = 9
#Variavel com a senha e o join para juntar as caracteres randomizados  
senha = ''.join(random.sample(use,tamanho_da_senha))
#print com a senha gerada
print('#-'*30)
print('Sua senha é {:-^30}'.format(senha))
print('#-'*30)