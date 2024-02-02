#JUDUL : Sub Program
#Deskripsi : Kumpulan Function dan Array untuk menunjang Main Program

#Penanggung Jawab :
# KELOMPOK 11
# Alfian Hanif FY / 19623281
# Yusuf Aji Nugraha / 16523008
# Hanif Kalyana Aditya / 19623120
# Naufal Ridho Wicaksono / 16523022
# Christian Fernando Asterias Manurung /16523127

#KAMUS
#judulFilm : list of string
#hargaFilm : list of integer
#jadwalFilm : list of string
#durasiFilm : list of integer
#statusKursiFilm : matrix of boolean
#statusFilm : list of boolean
#namaUser : list of string
#filmUser : list of integer
#kursiUser : list of integer
#kodebayarOnline : list of string
#kodebayarOffline : list of string
#statusUser : list of boolean


#ALGORITMA

import random                             #import modul random untuk mengacak angka

#array yang berhubungan dengan data film
#parameter buat manggil array ini = id_film
judulFilm = ["" for i in range(1000)]
hargaFilm = [0 for i in range(1000)]
jadwalFilm = ["" for i in range(1000)]
durasiFilm = [0 for i in range(1000)]
statusKursiFilm = [[True for i in range(60)] for i in range(1000)] #array dalam array #status kursi terisi atau tidak
statusFilm = [False for i in range(1000)] #apakah film aktif atau tidak

#array yang berhubungan dengan user
#parameter buat manggil array ini = id_user
namaUser = ["" for i in range(1000)]
filmUser = [0 for i in range(1000)] #film pilihan user
kursiUser = [0 for i in range(1000)]
kodebayarOnline = ["" for i in range(1000)]
kodebayarOffline = ["" for i in range(1000)]
statusUser = [False for i in range(1000)] #apakah user udh bayar atau belum


#FUNCTION MODEL / TAMPILAN PROGRAM

#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program membuat header
def Header(isi, panjang): #str, int
	for j in range(5):
		if j == 0 or j == 4:
			for i in range(panjang):
				print("=",end="")
			print("")
		if j ==1 or j == 3:
			for i in range(panjang):
				if i == 0 or i == (panjang-1):
					print("|", end="")
				else:
					print(" ", end="")
			print("")
		if j == 2:
			print("|", end="")
			for i in range((panjang-2)-len(isi)):
				if i == ((panjang-2)-len(isi))//2 :
					print(isi, end=" ")
				else:
					print(" ",end="")
			print("|")


#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program membuat garis bawah
def underLine(panjang): #int
	for i in range(panjang):
		print("=", end="")
	print("")


#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program membuat form
def form (nama,jenis): #str, str
	if jenis==int:
		return int(input(f'{nama} : '))
	else:
		return input(f'{nama} : ')

#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program membuat menu
def Menu(arr): #str semua, kalau kosong isi 0
	n = 1
	for i in (arr):
		print(f'[{n}] {i}')
		print("")
		n += 1

#nama/nim : Alfian Hanif Fitria Yustanto
#deskripsi : Program membuat tabel film
def tabelFilm(film, panjang): #film dalam bentuk array
	colPcts = [5,35,15,15,15,15]
	no = 0
	for i in film:
		print(i,end="")
		diff = int(colPcts[no]*panjang/100)-len(i)-1
		for j in range(diff):
			print(" ", end="")
		no += 1
	print("")
	for i in range(panjang):
		print("_",end="")
	print("")

#nama/nim : Yusuf Aji Nugraha / 16523008
#deskripsi : Program menampilkan visualisasi kursi kosong/terisi dari input array status kursi
def tampilkan_kursi(status_kursi, s):
  c = ['\033[36m'] * 62
  d = "\033[0m"
  s = (s-86)//2

  for kursi,i in zip([]+status_kursi,range(1,len(status_kursi)+1)):
    if kursi == False :
      c[i] = '\33[31m'
  print(f"""
  {" "*s}==================================================================================
  {" "*s}=                                                                                =
  {" "*s}=  ============================================================================  =
  {" "*s}=  =+++++++++++++++++++++++++++++++ Layar Lebar ++++++++++++++++++++++++++++++=  =
  {" "*s}=  ============================================================================  =
  {" "*s}=                                                                                =
  {" "*s}=  {c[1]}====== {c[2]}====== {c[3]}====== {c[4]}====== {c[5]}======        {c[6]}====== {c[7]}====== {c[8]}====== {c[9]}====== {c[10]}======  {d}=
  {" "*s}=  {c[1]}= 01 = {c[2]}= 02 = {c[3]}= 03 = {c[4]}= 04 = {c[5]}= 05 =        {c[6]}= 06 = {c[7]}= 07 = {c[8]}= 08 = {c[9]}= 09 = {c[10]}= 10 =  {d}=
  {" "*s}=  {c[1]}====== {c[2]}====== {c[3]}====== {c[4]}====== {c[5]}======        {c[6]}====== {c[7]}====== {c[8]}====== {c[9]}====== {c[10]}======  {d}=
  {" "*s}=  {c[11]}====== {c[12]}====== {c[13]}====== {c[14]}====== {c[15]}======        {c[16]}====== {c[17]}====== {c[18]}====== {c[19]}====== {c[20]}======  {d}=
  {" "*s}=  {c[11]}= 11 = {c[12]}= 12 = {c[13]}= 13 = {c[14]}= 14 = {c[15]}= 15 =        {c[16]}= 16 = {c[17]}= 17 = {c[18]}= 18 = {c[19]}= 19 = {c[20]}= 20 =  {d}=
  {" "*s}=  {c[11]}====== {c[12]}====== {c[13]}====== {c[14]}====== {c[15]}======        {c[16]}====== {c[17]}====== {c[18]}====== {c[19]}====== {c[20]}======  {d}=
  {" "*s}=  {c[21]}====== {c[22]}====== {c[23]}====== {c[24]}====== {c[25]}======        {c[26]}====== {c[27]}====== {c[28]}====== {c[29]}====== {c[30]}======  {d}=
  {" "*s}=  {c[21]}= 21 = {c[22]}= 22 = {c[23]}= 23 = {c[24]}= 24 = {c[25]}= 25 =        {c[26]}= 26 = {c[27]}= 27 = {c[28]}= 28 = {c[29]}= 29 = {c[30]}= 30 =  {d}=
  {" "*s}=  {c[21]}====== {c[22]}====== {c[23]}====== {c[24]}====== {c[25]}======        {c[26]}====== {c[27]}====== {c[28]}====== {c[29]}====== {c[30]}======  {d}=
  {" "*s}=  {c[31]}====== {c[32]}====== {c[33]}====== {c[34]}====== {c[35]}======        {c[36]}====== {c[37]}====== {c[38]}====== {c[39]}====== {c[40]}======  {d}=
  {" "*s}=  {c[31]}= 31 = {c[32]}= 32 = {c[33]}= 33 = {c[34]}= 34 = {c[35]}= 35 =        {c[36]}= 36 = {c[37]}= 37 = {c[38]}= 38 = {c[39]}= 39 = {c[40]}= 40 =  {d}=
  {" "*s}=  {c[31]}====== {c[32]}====== {c[33]}====== {c[34]}====== {c[35]}======        {c[36]}====== {c[37]}====== {c[38]}====== {c[39]}====== {c[40]}======  {d}=
  {" "*s}=  {c[41]}====== {c[42]}====== {c[43]}====== {c[44]}====== {c[45]}======        {c[46]}====== {c[47]}====== {c[48]}====== {c[49]}====== {c[50]}======  {d}=
  {" "*s}=  {c[41]}= 41 = {c[42]}= 42 = {c[43]}= 43 = {c[44]}= 44 = {c[45]}= 45 =        {c[46]}= 46 = {c[47]}= 47 = {c[48]}= 48 = {c[49]}= 49 = {c[50]}= 50 =  {d}=
  {" "*s}=  {c[41]}====== {c[42]}====== {c[43]}====== {c[44]}====== {c[45]}======        {c[46]}====== {c[47]}====== {c[48]}====== {c[49]}====== {c[50]}======  {d}=
  {" "*s}=  {c[51]}====== {c[52]}====== {c[53]}====== {c[54]}====== {c[55]}======        {c[56]}====== {c[57]}====== {c[58]}====== {c[59]}====== {c[60]}======  {d}=
  {" "*s}=  {c[51]}= 51 = {c[52]}= 52 = {c[53]}= 53 = {c[54]}= 54 = {c[55]}= 55 =        {c[56]}= 56 = {c[57]}= 57 = {c[58]}= 58 = {c[59]}= 59 = {c[60]}= 60 =  {d}=
  {" "*s}=  {c[51]}====== {c[52]}====== {c[53]}====== {c[54]}====== {c[55]}======        {c[56]}====== {c[57]}====== {c[58]}====== {c[59]}====== {c[60]}======  {d}=
  {" "*s}=                                                                                =
  {" "*s}==================================================================================
  """)
	
#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program menampilkan tabel keuangan
def tabelKeuangan(arr, panjang):
	colPcts = [10, 30, 30, 30]
	no = 0
	for i in arr:
		print(i,end="")
		diff = int(colPcts[no]*panjang/100)-len(i)-1
		for j in range(diff):
			print(" ", end="")
		no += 1
	print("")
	for i in range(panjang):
		print("_",end="")
	print("")

#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program menampilkan tabel penonton
def tabelPenonton(arr, panjang):
	colPcts = [10, 18, 18, 18, 18, 18]
	no = 0
	for i in arr:
		print(i,end="")
		diff = int(colPcts[no]*panjang/100)-len(i)-1
		for j in range(diff):
			print(" ", end="")
		no += 1
	print("")
	for i in range(panjang):
		print("_",end="")
	print("")
	


#FUNCTION MODUL ADMIN


#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program menambah film
def addFilm(id_film):
  global judulFilm
  global hargaFilm
  global jadwalFilm
  global durasiFilm
  global statusFilm

  judulFilm[id_film] = input("Judul : ")
  hargaFilm[id_film] = int(input("Harga : "))
  jadwalFilm[id_film] = input("Jadwal : ")
  durasiFilm[id_film] = int(input("Durasi : "))
  statusFilm[id_film] = True


#nama/nim : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program menghitung kursi terisi
def kursiTerisi(id_film):
  res = 0
  for i in range(60):
    if statusKursiFilm[id_film][i] == False:
      res += 1
  return res 


#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program menampilkan semua film
def showAllFilm(panjang):
  global judulFilm
  global hargaFilm
  global jadwalFilm
  global durasiFilm
  global statusFilm
  global statusKursiFilm 
  arr = ["NO" , "JUDUL" , "HARGA", "JADWAL" , "DURASI", "TERISI"]
  tabelFilm(arr, panjang)
  for i in range(1000): #range 1000 karena default jumlah ukuran array yang kita pake nilainya 1000
    if statusFilm[i] == True :
      kursi = kursiTerisi(i)
      arr = [str(i+1), judulFilm[i], str(hargaFilm[i]), jadwalFilm[i], str(durasiFilm[i]), str(kursi)]
      tabelFilm(arr, panjang)


#nama/nim : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program inisiasi data awal
def initFilm(id_film):
  global judulFilm
  global hargaFilm
  global jadwalFilm
  global durasiFilm
  global statusFilm
  initFilm = ["Mario", "Oppenheimer", "Gran Turismo", "Avatar 2", "John Wick",]
  initHarga = [30000, 45000, 45000, 35000, 45000]
  initJadwal = ["10:00" , "12:30", "14:30", "15:30", "18:30"]
  initDurasi = [90,180,120,180,120]
  for i in range(5):
    statusFilm[id_film + i] = True
    if statusFilm[id_film + i]:
      judulFilm[id_film + i] = initFilm[i]
      hargaFilm[id_film + i] = initHarga[i]
      jadwalFilm[id_film + i] = initJadwal[i]
      durasiFilm[id_film + i] = initDurasi[i]
  return 5

def initUser(id_user):
  global namaUser
  global filmUser 
  global kursiUser 
  global kodebayarOffline 
  global statusUser 
  global statusKursiFilm
  initNama = ["Suneo" , "Opet" , "Upin", "Saitama", "Sanji", "Naruto", "Luffy", "Zoro", "Sasuke", "Eren", "Nobita", "Doraemon", "Gojo"]
  for i in range(30):
      namaUser[id_user + i] = initNama[random.randrange(0,13,1)]
      filmUser[id_user + i] = random.randrange(0,5,1)
      kursiUser[id_user + i] = random.randrange(0,60,1)
      kodebayarOffline[id_user + i] = generateKodeBayarOffline(i)
      statusUser[id_user + i] = random.choice([True, False])
      statusKursiFilm[filmUser[id_user + i]][kursiUser[id_user + i]] = False
  return 30

# Nama/NIM : Christian Fernando Asterias Manurung/16523127
# Deskripsi : Program menghitung keuntungan total
def keuntunganTotal(id_film):
    global statusKursiFilm
    global hargaFilm
    res = 0
    for i in range(id_film):
         res += keuntunganFilm(i)
    return res

# Nama/NIM : Christian Fernando Asterias Manurung
# Deskripsi : Program menentukan keuntungan seharusnya
def keuntunganSeharusnya():
    global statusFilm
    nett = 0
    for i in range(1000):
       if statusFilm[i] == True:
          nett += hargaFilm[i]*60
    return nett

			

#FUNCTION MODUL GUEST


#nama : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program mengecek tiket penonton
def checkTiket(panjang):
    global kodebayarOffline
    global kodebayarOnline
    global statusUser
    valid = False
    kode = form("Kode Bayar", str )
    underLine(panjang)
    for i in range(1000):
        if kode == kodebayarOffline[i] or kode == kodebayarOnline[i]:
            nomor_tiket = i
            valid = True
    if valid:
        print("Tiket di temukan !")
        underLine(panjang)
        if statusUser[nomor_tiket] == True:
            showPenonton(nomor_tiket)
        else:
            print("Belum Bayar")
    else:
        print("Tiket Tidak Ditemukan !")
    

#nama : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program menampilkan tiket penononton
def showPenonton(id_user):
    global namaUser 
    global filmUser 
    global kursiUser 
    global jadwalFilm
    print(f"Nama    :   {namaUser[id_user]}")
    print(f"Film    :   {judulFilm[filmUser[id_user]]}")
    print(f'Jadwal  :   {jadwalFilm[filmUser[id_user]]}')
    print(f"Kursi   :   {kursiUser[id_user] }")


# Nama : Hanif Kalyana Aditya / 19623120
# Deskripsi : program simulasi pembayaran tiket
def bayarTiket(id_user):
  global hargaFilm
  global filmUser
  InputNominal = int(input("Masukkan nominal pembayaran Anda: "))
  if InputNominal == hargaFilm[filmUser[id_user]]:
    statusUser[id_user] = True
    return False
  else:
      return True

#nama : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program mengecek kode bayar
def checkKodeBayar(kodeBayar):
  global kodebayarOffline
  global kodebayarOnline
  valid = False
  for i in range(1000):
      if kodeBayar == kodebayarOffline[i] or kodeBayar == kodebayarOnline:
          nomor_tiket = i
          valid = True
  if valid:
      print("Kode Ditemukan ! ")
      return nomor_tiket
  else:
      print("Kode Salah ! ")
      return False
   

#Nama/NIM : Naufal Ridho Wicaksono / 16523022
#Deskripsi : Program membuat kode bayar online
def generateKodeBayarOnline(id_user) :
  global namaUser
  global filmUser
  global kodebayarOnline
  kodebayarOnline[id_user] = f'01{id_user}{filmUser[id_user]}'
  kode = kodebayarOnline[id_user]
  return kode


# Nama : Hanif Kalyana Aditya / 19623120
# Deskripsi : program buat input kode bayar oflline
def inputKodeBayarOffline():
  global kodebayarOffline
  global hargaFilm
  KodeBayar = (input("Masukkan kode bayar: "))
  for i in range(1000):
    if KodeBayar == kodebayarOffline[i]:
      print(f"kode bayar ditemukan ! tagihan mu sebesar {hargaFilm[filmUser[i]]}")
      return i
    elif KodeBayar != kodebayarOffline[i] and i == 999:
      print("kode bayar tidak ditemukan !")
      return -1

# Nama : Hanif Kalyana Aditya / 19623120
# Deskripsi : program buat input kode bayar oflline
def inputKodeBayarOnline():
  global kodebayarOnline
  global hargaFilm
  KodeBayar = (input("Masukkan kode bayar: "))
  for i in range(1000):
    if KodeBayar == kodebayarOnline[i]:
      print(f"kode bayar ditemukan ! Tagihan mu sebesar {hargaFilm[filmUser[i]]}")
      return i
    elif KodeBayar != kodebayarOnline[i] and i == 999:
      print("kode bayar tidak ditemukan !")
      return -1
    
#Nama/Nim : Yusuf Aji Nugraha
#Deskripsi : sub-program untuk mengganti status kursi yang user pilih menjadi "Terisi" (False)
def pilih_kursi(id_film):
  global statusKursiFilm
  no_kursi = int(input("Nomor Kursi       :    ")) - 1
  return no_kursi


#Nama/NIM : Naufal RIdho Wicaksono/16523022
#Deskripsi : Program membuat kode bayar offline
def generateKodeBayarOffline(id_user) :
  global filmUser
  global kodebayarOffline
  kodebayarOffline[id_user] = f'02{id_user}{filmUser[id_user]}'
  kode = kodebayarOffline[id_user]
  return kode

#nama : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program memasukkan film yang dipilih user ke dalam array
def addFilmUser(id_user,id_film):
   global filmUser
   filmUser[id_user] = id_film

#nama : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program memasukkan kursi user ke dalam array
def addKursiUser(id_user, nomor_kursi):
   global kursiUser
   kursiUser[id_user] = nomor_kursi + 1

#nama : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program memasukkan nama user ke dalam array
def addNamaUser(id_user):
   global namaUser
   namaUser[id_user] = input("Nama        :     ")

#nama : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program menampilkan list penonton
def listPenonton(panjang, id_user):
  global namaUser  
  global filmUser 
  global kursiUser 
  global statusUser
  global judulFilm
  global kodebayarOffline
  global kodebayarOnline
  num = 1
  arr = ["NO","NAMA","JUDUL FILM","NO KURSI", "STATUS" , "KODE BAYAR"]
  tabelPenonton(arr,panjang)
  for i in range(id_user):
    if kodebayarOnline[i] != "":
       kode = kodebayarOnline[i]
    else:
        kode = kodebayarOffline[i]
    if statusUser[i] == True:
       status = "sudah bayar"
    else:
       status = "belum bayar"
    arr = [str(num), namaUser[i],judulFilm[filmUser[i]],str(kursiUser[i]),status, kode]
    tabelPenonton(arr,panjang)
    num += 1


# Nama/NIM : Christian Fernando Asterias Manurung
# Deskripsi : Program menentukan keuntungan 1 film tertentu
def keuntunganFilm(id_film):
    global statusKursiFilm
    res = 0
    for i in range(60):
        if statusKursiFilm[id_film][i] == False :
            res +=1
    for j in range(1000):
        if judulFilm[filmUser[j]] == judulFilm[id_film] and statusUser[j] == False and kodebayarOffline[j] != "" :
          res -= 1
        elif judulFilm[filmUser[j]] == judulFilm[id_film] and statusUser[j] == False and kodebayarOnline[j] != "":
           res -= 1
    res = res * hargaFilm[id_film]
    return res

# Nama : Alfian Hanif Fitria Yustanto / 19623281
# Deskripsi : Program menampilkan keuntungan dalam bentuk tabel
def showKeuntungan(panjang):
  global judulFilm
  global hargaFilm
  global statusFilm
  no = 1
  for i in range(1000):
    if statusFilm[i] == True:
      arr = [str(no) , judulFilm[i], str(hargaFilm[i]), str(keuntunganFilm(i))]
      tabelKeuangan(arr,panjang)
      no += 1

#nama : Alfian Hanif Fitria Yustanto/19623281
#deskripsi : Program mengecek ketersediaan kursi
def cekKursi(film_user , kursi_user):
    global statusKursiFilm
    if statusKursiFilm[film_user][kursi_user] == False:
        return False
    else:
         statusKursiFilm[film_user][kursi_user] = False
         return True

     