from datetime import datetime

# Rincian coffeeshop
def rincian_coffeshop():
    print("=" * 38)
    print("            Coffe Mercie")
    print("           Jl. Mangkunegara")
    print("            083814329508")

# Menu
menu = {
    "1": {"nama": "Americano", "harga": 20000},
    "2": {"nama": "Cappuccino", "harga": 20000},
    "3": {"nama": "Caffe Latte", "harga": 25000},
    "4": {"nama": "Mochaccino", "harga": 27000},
    "5": {"nama": "Vanilla Latte", "harga": 25000},
    "6": {"nama": "Matchalatte", "harga": 25000},
    "7": {"nama": "Red Velvet", "harga": 25000},
    "8": {"nama": "Cookies", "harga": 7000},
    "9": {"nama": "Croissant", "harga": 15000},
    "10": {"nama": "Muffin Chocolate", "harga": 10000},
    "11": {"nama": "Cheesecake", "harga": 10000}
}

def tampilkan_menu():
    print("=" * 38)
    print("   Selamat Datang di Coffe Mercie")
    print("Daftar Menu:")
    for i, item in menu.items():
        print(f"{i}. {item['nama']:<22} ({item['harga']} IDR)")
    print("=" * 38)

def proses_pemesanan():
    pesanan = {}
    total_harga = 0
    print("\nMasukkan kode makanan yang dipesan (pisahkan dengan spasi):")
    kode_pesanan = input().split()

    # Hitung total harga pesanan
    for kode in kode_pesanan:
        if kode in menu:
            if kode in pesanan:
                pesanan[kode] += 1
            else:
                pesanan[kode] = 1
            total_harga += menu[kode]["harga"]
        else:
            print(f"Maaf, kode {kode} tidak tersedia.")

    # Diskon 20% jika total harga lebih dari 100rb
    diskon = 0
    if total_harga > 100000:
        diskon = 0.2 * total_harga

    # Ulang proses pembayaran jika uang kurang
    while True:
        uang_pelanggan = float(input("Masukkan uang: "))
        if uang_pelanggan < total_harga:
            print("Uang yang anda masukkan kurang.")
            continue
        else:
            # Tampilkan struk
            rincian_coffeshop()
            print("")
            print(datetime.now().strftime("Waktu: %d/%m/%Y %H:%M:%S"))
            print("=" * 38)
            print("Menu yang dipesan:")
            for kode, jumlah in pesanan.items():
                print(f"{menu[kode]['nama']:20}: {jumlah:2}")
            print("-" * 38)
            print("Total       : Rp. ", total_harga)
            if total_harga >= 100000:
                print("Diskon      : 20%", "(", diskon, ")")
                print("Bayar       : Rp. ", uang_pelanggan)
                print("Kembalian   : Rp. ", uang_pelanggan - (total_harga - diskon))
            else:
                print("Bayar       : Rp. ", uang_pelanggan)
                print("Kembalian   : Rp. ", uang_pelanggan - total_harga)
            print("=" * 38)
            print("")
            print("     ~~Terimakasih Sudah Memesan~~")
            print("")
            print("=" * 38)
            return True

# Jalankan program
while True:
    tampilkan_menu()
    if proses_pemesanan():
        break