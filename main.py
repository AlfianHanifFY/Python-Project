# JUDUL : Main Program
# DESKRIPSI : Program Utama Sistem Bioskop

#Penanggung Jawab :
# KELOMPOK 11
# Alfian Hanif FY (19623281)


#KAMUS
#start = Boolean
#id_user = int
#id_film = int
#main_route = int
#sub_route = int
#panjang = int

#ALGORITMA

import subProgram as sp                           #import subprogram
from subProgram import judulFilm,statusKursiFilm  #import beberapa array
import os                                         #import untuk mengaktifkan cls
start = True
id_user = 0
id_film = 0
main_route = 0
sub_route = 0
panjang = 100


#inisiasi awal program untuk menampilkan data awal
id_film += sp.initFilm(id_film)
id_user += sp.initUser(id_user)

while(start):
    #menu awal pilih user / admin
    while(main_route== 0):
        sp.Header("SELAMAT DATANG", panjang)
        arr_menu = ["Admin", "Guest", "Pengaturan", "Keluar"]
        sp.Menu(arr_menu)
        sp.underLine(panjang)
        main_route = int(input(""))
        os.system("cls")


    #program admin
    while(main_route == 1):
        sp.Header("ADMIN", panjang)
        arr_menu = ["Konfirmasi Pembayaran", "Cek Tiket", "Cek Penonton", "Cek Film", "Tambah Film", "Keuangan","Kembali"]
        sp.Menu(arr_menu)
        sp.underLine(panjang)
        sub_route = int(input(""))
        os.system("cls")

        #program konfirmasi pembayaran sub rute 1
        while(sub_route == 1):                           
            sp.Header("PEMBAYARAN", panjang)
            valid = True
            nomor_bayar = sp.inputKodeBayarOffline()
            if nomor_bayar>= 0:
                sp.underLine(panjang)
                while valid:
                  valid = sp.bayarTiket(nomor_bayar)
                  if not valid:
                      print("Pembayaran Berhasil")
                  else:
                      print("Pembayaran Gagal , nominal uang salah !")
                  sp.underLine(panjang)
            print("")
            kembali = input("kembali (ya/tidak) : ")
            if(kembali=="ya"):
                sub_route = 0
            os.system("cls")


        #program cek tiket sub rute 2
        while(sub_route == 2):
            sp.Header("CEK TIKET", panjang)
            sp.checkTiket(panjang)
            print("")
            kembali = input("kembali (ya/tidak) : ")
            sp.underLine(panjang)
            if(kembali=="ya"):
                sub_route = 0
            os.system("cls")



        #program cek penonton sub rute 3
        while (sub_route == 3):
            sp.Header("CEK PENONTON", panjang)
            sp.listPenonton(panjang , id_user)
            print("")
            kembali = input("kembali (ya/tidak) : ")
            if(kembali=="ya"):
                sub_route = 0
            os.system("cls")



        #program cek film sub rute 4
        while(sub_route == 4):
            sp.Header("CEK FILM", panjang)
            sp.showAllFilm(panjang)
            sp.underLine(panjang)
            print("")
            kembali = input("kembali (ya/tidak) : ")
            if(kembali == "ya"):
                sub_route = 0
                print("sukses")
            os.system("cls")


        #program tambah film sub rute 5
        while(sub_route == 5) :
            sp.Header("TAMBAH FILM", panjang)
            sp.addFilm(id_film)
            id_film += 1
            sp.underLine(panjang)
            print("")
            kembali = input("kembali (ya/tidak) : ")
            if(kembali=="ya"):
                sub_route = 0
            os.system("cls")


        #program keuangan sub rute 6
        while(sub_route == 6):
          sp.Header("KEUANGAN",panjang)
          arr = ["NO" , "JUDUL" , "HARGA" , "PENDAPATAN"]
          sp.tabelKeuangan(arr, panjang)
          sp.showKeuntungan(panjang)
          print("")
          sp.underLine(panjang)
          arr = [" ", "TOTAL", " " , str(sp.keuntunganTotal(id_film))]
          sp.tabelKeuangan(arr, panjang)
          arr = [" ", "TARGET", " " , str(sp.keuntunganSeharusnya())]
          sp.tabelKeuangan(arr,panjang)
          if sp.keuntunganSeharusnya() > 0:
            arr = [" ", "TERCAPAI", " " , str(sp.keuntunganTotal(id_film)/sp.keuntunganSeharusnya() * 100) + "%"]
            sp.tabelKeuangan(arr,panjang)
          sp.underLine(panjang)
          print("")
          kembali = input("kembali (ya/tidak) : ")
          if(kembali=="ya"):
            sub_route = 0
          os.system("cls")


        #program Logout kembali ke halaman utama sub rute 7
        while(sub_route == 7):
            main_route = 0
            sub_route = 0



    #program Guest
    while(main_route == 2):
        sp.Header("GUEST", panjang)
        arr_menu = ["Pesan Tiket", "Bayar Online", "Cek Tiket", "Kembali"]
        sp.Menu(arr_menu)
        sp.underLine(panjang)
        sub_route = int(input(""))
        os.system("cls")

        #program pesan tiket sub rute 1
        while(sub_route == 1):
            sp.Header("PESAN TIKET", panjang)
            sp.showAllFilm(panjang)
            sp.underLine(panjang)
            film_user = int(input("Masukkan nomor film : ")) - 1
            sp.addFilmUser(id_user,film_user)
            os.system("cls")

            sp.Header(f'{judulFilm[film_user]}', panjang)
            sp.tampilkan_kursi(statusKursiFilm[film_user], panjang)
            sp.underLine(panjang)
            sp.addNamaUser(id_user)
            kursiUser = sp.pilih_kursi(film_user)
            if sp.cekKursi(film_user, kursiUser):    
              sp.addKursiUser(id_user,kursiUser)
              os.system("cls")

              sp.Header("METODE BAYAR",panjang)
              arr_menu = ["Online", "Offline"]
              sp.Menu(arr_menu)
              sp.underLine(panjang)
              metod = int(input(""))
              if metod == 1:
                  print(f"Kode Bayar Online Anda : {sp.generateKodeBayarOnline(id_user)}")

              elif metod == 2:
                  print(f"Kode Bayar Offline Anda : {sp.generateKodeBayarOffline(id_user)}")
              id_user += 1
            else:
                print("Kursi sudah terisi !")
            print("")
            kembali = input("kembali (ya/tidak) : ")
            if(kembali=="ya"):
                sub_route = 0
            os.system("cls")



        #program bayar online sub rute 2
        while(sub_route == 2):                          
            sp.Header("PEMBAYARAN", panjang)
            valid = True
            nomor_bayar = sp.inputKodeBayarOnline()
            if nomor_bayar>= 0:
                while valid:
                  valid = sp.bayarTiket(nomor_bayar)
                  sp.underLine(panjang)
                  if not valid:
                      print("Pembayaran Berhasil")
                  else:
                      print("Pembayaran Gagal , nominal uang salah !")
                  sp.underLine(panjang)
            print("")
            kembali = input("kembali (ya/tidak) : ")
            if(kembali=="ya"):
                sub_route = 0
            os.system("cls")


        #program cek tiket sub rute 3
        while(sub_route == 3):
            sp.Header("CEK TIKET", panjang)
            sp.checkTiket(panjang)
            kembali = input("kembali (ya/tidak) : ")
            print("")
            if(kembali=="ya"):
                sub_route = 0
            os.system("cls")


        #program logout sub rute 4
        while(sub_route == 4):
            main_route = 0
            sub_route = 0



    #program pengaturan
    while(main_route == 3):
        sp.Header("PENGATURAN", panjang)
        arr_menu = ["Ukuran", "Inisiasi User" , "Inisiasi Film" , "Tentang Kami","Kembali"]
        sp.Menu(arr_menu)
        sp.underLine(panjang)
        sub_route = int(input(""))
        os.system("cls")
        
        #menu ukuran sub rute 1
        while(sub_route==1):
          sp.Header("UKURAN" , panjang)
          panjang = int(input("Ukuran Header : "))
          os.system("cls")
          sp.Header("PENGATURAN", panjang)
          print("")
          simpan = input("Simpan pengaturan (ya/tidak) : ")
          os.system("cls")
          if(simpan=="ya"):
              sub_route = 0
        
        #menu inisiasi User sub rute 2
        while(sub_route==2):
          sp.Header("INISIASI USER" , panjang)
          id_user += sp.initUser(id_user)
          print("Inisiasi Berhasil !")
          sp.underLine(panjang)
          kembali = input("kembali (ya/tidak) : ")
          print("")
          if(kembali=="ya"):
              sub_route = 0
          os.system("cls")


        #menu inisiasi film sub rute 3
        while(sub_route==3):
          sp.Header("INISIASI FILM" , panjang)
          id_film += sp.initFilm(id_film)
          print("Inisiasi Berhasil !")
          sp.underLine(panjang)
          kembali = input("kembali (ya/tidak) : ")
          print("")
          if(kembali=="ya"):
              sub_route = 0
          os.system("cls")

        #menu Tentang kami sub rute 4
        while(sub_route==4):
          sp.Header("Tentang Kami" , panjang)
          print("TUGAS BESAR PENGENALAN KOMPUTASI")
          sp.underLine(panjang)
          print("")
          print("KELOMPOK 11")
          print("")
          print("Alfian Hanif Fitria Yustanto - 19623281")
          print("Yusuf Aji Nugraha - 16523008")
          print("Hanif Kalyana Aditya")
          print("Naufal Ridho Wicaksono - 16523022")
          print("Christian Fernando Asterias Manurung - 16523127")
          sp.underLine(panjang)
          print("")
          kembali = input("kembali (ya/tidak) : ")
          if(kembali=="ya"):
              sub_route = 0
          os.system("cls")

        while(sub_route==5):
            main_route = 0
            sub_route = 0
            


    #keluar dari program
    while (main_route == 4):
        start = False







