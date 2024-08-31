# Mengumpulkan Input
nama_lengkap = input("Masukkan nama lengkap Anda: ")
usia_tahun = int(input("Masukkan usia Anda dalam tahun: "))
tinggi_cm = float(input("Masukkan tinggi badan Anda dalam sentimeter: "))
status_menikah = input("Apakah Anda sudah menikah? (y/n): ").lower() == 'y'

# Memproses Data
usia_bulan = usia_tahun * 12
tinggi_meter = tinggi_cm / 100

# Menampilkan Output
print("\n--- Ringkasan Informasi ---")
print(f"Nama lengkap: {nama_lengkap}")
print(f"Usia: {usia_tahun} tahun atau {usia_bulan} bulan")
print(f"Tinggi badan: {tinggi_cm} cm atau {tinggi_meter:.2f} m")
print(f"Status pernikahan: {'Sudah menikah' if status_menikah else 'Belum menikah'}")

# Mengumpulkan Input
angka_pertama = float(input("Masukkan angka pertama: "))
angka_kedua = float(input("Masukkan angka kedua: "))

# Melakukan Operasi Aritmatika
penjumlahan = angka_pertama + angka_kedua
pengurangan = angka_pertama - angka_kedua
perkalian = angka_pertama * angka_kedua
pembagian = angka_pertama / angka_kedua if angka_kedua != 0 else "Tidak dapat membagi dengan nol"
pangkat = angka_pertama ** angka_kedua

# Menampilkan Hasil
print("\nHasil Operasi Aritmatika:")
print(f"Penjumlahan: {angka_pertama} + {angka_kedua} = {penjumlahan}")
print(f"Pengurangan: {angka_pertama} - {angka_kedua} = {pengurangan}")
print(f"Perkalian: {angka_pertama} * {angka_kedua} = {perkalian}")
print(f"Pembagian: {angka_pertama} / {angka_kedua} = {pembagian}")
print(f"Pangkat: {angka_pertama} ^ {angka_kedua} = {pangkat}")

# Mengumpulkan Input
nilai = float(input("Masukkan nilai awal: "))

# Menampilkan nilai awal
print(f"\nNilai awal: {nilai}")

# Tambahkan 2 ke nilai tersebut
nilai += 2
print(f"Setelah ditambah 2: {nilai}")

# Kurangi nilai tersebut dengan 3
nilai -= 3
print(f"Setelah dikurangi 3: {nilai}")

# Kalikan nilai tersebut dengan 10
nilai *= 10
print(f"Setelah dikalikan 10: {nilai}")

# Bagi nilai tersebut dengan 4
nilai /= 4
print(f"Setelah dibagi 4: {nilai}")

# Hitung pangkat nilai tersebut dengan 10
nilai **= 10
print(f"Setelah dipangkatkan 10: {nilai}")
