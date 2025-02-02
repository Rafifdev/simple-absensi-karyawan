# Import modul datetime untuk mencatat waktu
import datetime

# Dictionary untuk menyimpan data karyawan
data_karyawan = {
     "Dummy": {
        "posisi": "Manager",
        "jam_masuk": "08:00",
        "jam_keluar": "17:00",
    },
}

# Fungsi untuk menampilkan cara penggunaan program
def cara_penggunaan():
    while True:
        print("\n========== Cara Menggunakan Program ==========\n")
        print("1. Pilih menu yang tersedia.")
        print("2. Tambah data karyawan sebelum mencatat jam kerja.")
        print("3. Catat jam masuk dan keluar sesuai kehadiran.")
        print("4. Lihat laporan jam kerja karyawan.")
        print("5. Pilih 'Keluar' untuk mengakhiri program.")
        print("\n===============================================")
        
        lanjut = input("Ketik 'next' untuk melanjutkan: ").strip().lower()
        print("")
        if lanjut == "next":
            break
        else:
            print("\nInput salah, silakan coba lagi😕.\n")

# Fungsi untuk menambahkan data karyawan
def tambah_karyawan():
    while True :
        print("\n=============== Tambah Karyawan ===============\n")
        nama = input("Masukkan Nama: ")
        posisi = input("Masukkan posisi: ")
        data_karyawan[nama] = {"posisi": posisi, "jam_masuk": None, "jam_keluar": None}
        validasi = input("\nMau masukan data lagi? (y/n) : ")
        if validasi == "y" :
            print("\nKaryawan berhasil ditambahkan✅")
        elif validasi == "n" :
            break

# Fungsi untuk mencatat jam masuk karyawan
def catat_masuk():
  while True :
    print("\n=============== Catat Jam Masuk ===============\n")
    nama = input("Masukkan Nama: ")
    
    # Memeriksa apakah karyawan ada dalam data
    if nama in data_karyawan:
        
        # Mengambil jam masuk
        data_karyawan[nama]["jam_masuk"] = datetime.datetime.now().strftime("%H:%M")
        print(f"\nJam masuk {nama} tercatat pada {data_karyawan[nama]['jam_masuk']}📝")
        break
    else:
        print("Karyawan tidak ditemukan😕\n")
        validasi = input("Mau keluar (y/n) ?")
        if validasi == "y":
          break

# Fungsi untuk mencatat jam keluar karyawan
def catat_keluar():
  while True:
    print("\n=============== Catat Jam Keluar ===============\n")
    nama = input("Masukkan Nama: ")
    
    # Memeriksa apakah karyawan ada dalam data
    if nama in data_karyawan:
        
        # Mengambil jam keluar
        data_karyawan[nama]["jam_keluar"] = datetime.datetime.now().strftime("%H:%M")
        
        print(f"\nJam keluar {nama} tercatat pada {data_karyawan[nama]['jam_keluar']}📝")
        break
    else:
        print("Karyawan tidak ditemukan😕\n")
        validasi = input("Mau keluar (y/n) ?")
        if validasi == "y":
          break

# Fungsi untuk menampilkan semua data karyawan
def tampilkan_data():
    print("\n================ Data Karyawan ================\n")
    
    # Cari data di  data_karyawan
    for nama, data in data_karyawan.items():
        print(f"- Nama: {nama}, posisi: {data['posisi']}, Jam Masuk: {data['jam_masuk']}, Jam Keluar: {data['jam_keluar']}")

# Fungsi untuk mengedit data karyawan
def edit_data():
    print("\n=============== Menu Edit Data ===============\n")
    nama = input("Masukkan Nama Karyawan yang ingin diedit: ")

    # Memeriksa apakah karyawan ada dalam data
    if nama in data_karyawan:

      while True:
        print("\n=============== Menu Edit Data ===============\n")
        print("1. Edit Posisi Karyawan")
        print("2. Edit Jam Masuk Karyawan")
        print("3. Edit Jam Keluar Karyawan")
        print("4. Kembali Ke Menu Utama")
        print("\n==============================================\n")
        validasi = input("Pilih menu : ")

        # Mengambil data dari dictionary 
        posisi = data_karyawan[nama].get("posisi", "")
        jam_masuk = data_karyawan[nama].get("jam_masuk", "")
        jam_keluar = data_karyawan[nama].get("jam_keluar", "")

        # Validasi pilihan
        if validasi == "1":
          posisi = input("\nMasukkan posisi baru: ")
        elif validasi == "2":
          jam_masuk = input("\nMasukkan Jam Masuk baru (HH:MM): ")
        elif validasi == "3":
          jam_keluar = input("\nMasukkan Jam Keluar baru (HH:MM): ")
        elif validasi == "4":
          break

        # Memperbarui data
        if posisi: data_karyawan[nama]["posisi"] = posisi
        if jam_masuk: data_karyawan[nama]["jam_masuk"] = jam_masuk
        if jam_keluar: data_karyawan[nama]["jam_keluar"] = jam_keluar
        
        print("\nData karyawan berhasil diperbarui✅")
    else:
        print("\nKaryawan tidak ditemukan😕")

# Fungsi untuk menghapus data karyawan
def hapus_data():
    print("\n=============== Menu Hapus Data ===============\n")
    nama = input("Masukkan Nama Karyawan yang ingin dihapus: ")
    
    # Memeriksa apakah karyawan ada dalam data
    if nama in data_karyawan:
        del data_karyawan[nama]
        print("\nData karyawan berhasil dihapus🗑️")
    else:
        print("\nKaryawan tidak ditemukan❌\n")

# Looping program
while True:
    print("\n========== APLIKASI ABSENSI KARYAWAN ==========\n")
    print("Silahkan Pilih Sesuai Kebutuhan Anda :")
    print("1. Cara menggunakan program")
    print("2. Tambah data karyawan")
    print("3. Catat jam masuk karyawan")
    print("4. Catat jam keluar karyawan")
    print("5. Edit data karyawan")
    print("6. Hapus data karyawan")
    print("7. Tampilkan data karyawan")
    print("8. Keluar")
    print("\n===============================================")

    pilihan = input("\nPilih menu: ")
    
    # Perkondisian untuk pilihan menu
    if pilihan == "1":
        cara_penggunaan()
    elif pilihan == "2":
        tambah_karyawan()
    elif pilihan == "3":
        catat_masuk()
    elif pilihan == "4":
        catat_keluar()
    elif pilihan == "5":
        edit_data()
    elif pilihan == "6":
        hapus_data()
    elif pilihan == "7":
        tampilkan_data()
    elif pilihan == "8":
        print("\n- Terima kasih! Program selesai😎\n")
        break
    else:
        print("\nPilihan tidak valid, silakan coba lagi😕")