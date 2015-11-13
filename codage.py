import time
mes = input()
a = input("clef de codage(a) : ")
b = input("clef de codage(b) : ")
def num(caractere):
	return ord(caractere)-65

def lettre(n):
	return chr(n+65)

for c in mes:
	print(c, end=" | ")
print()
for c in mes:
	print(num(c), end = " | ")
print('\n\n', 'le message codé')
for c in mes:
	y=(num(c)*11+7) % 26
	print(lettre(y), end = "")
print()
time.sleep(50)