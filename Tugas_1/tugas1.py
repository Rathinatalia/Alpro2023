batas = int(input('masukkan angka batas: '))

for i in range (batas):
    hasil = ''
    fizz = (i + 1) % 2 == 0
    buzz = (i + 1) % 3 == 0

    if fizz:
        hasil += 'Fizz'

    if buzz:
        hasil += 'Buzz'

    print('{} -> {}'.format(i + 1, hasil))