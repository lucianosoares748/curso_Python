# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

print(type('1'), type(int('1'))) #convercao para inteiro
print(type(float('1') + 1)) #convercao para float
print(bool(' ')) #string sem espaco tem valor false, e com espaco true
print(str(11) + 'b') #convercao de numero inteiro para string
# concatenando com outro tipo de dado string