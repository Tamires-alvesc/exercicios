s = 0

for c in range (1,501):
    if c % 3 == 0 and c % 2 != 0:
       s = s + c # (s += c)
print(f'A soma dos números é {s}')

#for c in range (1,501,2):
#    if c % 3 == 0:
#       s = s + c
#print(f'A soma dos números é {s}')