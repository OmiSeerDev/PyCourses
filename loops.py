#While
count = 0
sym = ['-','|','-','|']
while count <= 30:
  for a in sym:
    print(a, end='')
  count += 1
print("\nLoop ended")

#For
nums = [2, 4, 6, 8, 10, 12]
for n in range(6, 13):
  print('Num\t', n)

print('========================')
for n in nums:
  print('Even', n)

anim = {
  'dog': 'perro',
  'cat': 'gato',
  'bird': 'pájaro',
  'fish': 'pez',
  'horse': 'caballo',
  'cow': 'vaca'
}
print('========================')
for el in anim:
  print(el, "\tmaps to ==> ", anim[el])
