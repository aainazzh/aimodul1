print ("hei")
contoh_teks ='halo semua'
print(type(contoh_teks))

contoh_list = [1,2,3,4,5,6]
print(type(contoh_list))

contoh_list_kedua = ['a', 'b', 'c', 'd', 'e']
print(contoh_list_kedua[3])

print(contoh_list)
contoh_list.append('abc')
print(contoh_list)

contoh_list = [[1,2,3,4,5], 'a', 'b', 77]
print(contoh_list[0][1])


contoh_set = set(['d', 'i', 'b', 'i', 'm', 'b', 'i', 'n', 'g'])
print(contoh_set)

daftar_harga = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800,'duku': 6500}
print(daftar_harga['mangga'])
print(list(daftar_harga.keys()))
print(list(daftar_harga.values()))

buah_belanjaan =['apel', 'apel', 'jeruk', 'mangga', 'mangga', 'jeruk', 'duku']
list_harga = [daftar_harga[x] for x in buah_belanjaan]
print(list_harga)

total_harga = sum(list_harga)
print(total_harga)

dictionary = {'Apple': ['iPhone 11', 'Airpods', 'Macbook Pro'], 'Samsung': ['Galaxy Note 10', 'Galaxy S9', 'Galaxy Watch'], 'Sony': ['Xperia 1', 'Xperia 2', 'Xperia 3']}
print (dictionary['Apple'][2])

print(1+2)
print(2+3)
print(3+4)

nama = 'Steven'
print(f'Nama peserta adalah {nama}. Peserta tersebut telah tercatat')

nilai_1 = 90
nilai_2 = 100
nilai_3 = 80
print(f'Rata-rata nilai: {(nilai_1 + nilai_2 + nilai_3/3)} poin.')

print(buah_belanjaan)
print(len(buah_belanjaan))

def luas_keliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang+lebar)
    return luas, keliling
print(luas_keliling(10,5))
print(luas_keliling(10,5)[0])

jwb_luas, jwb_keliling = luas_keliling(7,4)
print(jwb_luas)
print(jwb_keliling)

def luas_keliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang+lebar)

    print('Luas persegi panjang:', luas)
    print('Keliling persegi panjang', keliling)
    luas_keliling(9,5)

def luas_keliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang+lebar)

    print('Luas persegi panjang:', luas_keliling)
    print('Keliling persegi panjang', keliling)

    return luas, keliling

jwb_luas, jwb_keliling = luas_keliling(9,5)
print(jwb_luas)

def luas_keliling(panjang, lebar):
    if panjang < lebar:
        lebar, panjang = panjang, lebar
        print('Waduh kok panjang lebih pendek daripada lebar. Kita switch ya!')
    else:
        pass

    luas = panjang * lebar
    keliling = 2 * (panjang+lebar)

    print(f'Luas persegi panjang yang memiliki panjang{panjang} dan lebar {lebar} adalah (luas)')
    print(f'Keliling persegi panjang yang memiliki panjang {panjang} dan lebar {lebar} adalah {keliling}')

    return luas, keliling
luas_keliling(9,10)

list_contoh = [1,2,3,4,5,6]
list_contoh.append(8)
list_contoh

new_set ={1,2,3,4,5}
new_set.add(6)
print (new_set)

list_loop = ['Aldp', 'Budi', 'Cindy', 'Dilan', 'Ed Sheeran']

for x in list_loop:
    print('Nama peserta:', x)

nama = 'Abc'

for u in range(10):
    print(nama)

nilai = 80 

if nilai > 70:
    print('Lulus')
else:
    print('Tidak Lulus')

teks = 'SMK Telkom Malang'
print(teks.split())


text = 'Coding-dengan-Python'
print(text.split('-'))


