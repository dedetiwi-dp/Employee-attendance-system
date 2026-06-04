# ==============================
# MINI SYSTEM KASIR SUPERMARKET
# ==============================

produk = {
    "1": {"nama": "Indomie Goreng", "harga": 3500},
    "2": {"nama": "Aqua 600ml", "harga": 4000},
    "3": {"nama": "Teh Botol", "harga": 5000},
    "4": {"nama": "Roti Coklat", "harga": 7500},
    "5": {"nama": "Beras 5Kg", "harga": 68000}
}

keranjang = []
total = 0

while True:

    print("\n===== KASIR SUPERMARKET =====")
    print("1. Lihat Produk")
    print("2. Tambah Barang")
    print("3. Lihat Keranjang")
    print("4. Checkout")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    # ======================
    # LIHAT PRODUK
    # ======================
    if pilihan == "1":

        print("\n===== DAFTAR PRODUK =====")

        for kode, item in produk.items():
            print(f"{kode}. {item['nama']} - Rp{item['harga']}")

    # ======================
    # TAMBAH BARANG
    # ======================
    elif pilihan == "2":

        kode = input("Masukkan kode produk: ")

        if kode in produk:

            jumlah = int(input("Jumlah beli: "))

            nama_produk = produk[kode]["nama"]
            harga_produk = produk[kode]["harga"]

            subtotal = harga_produk * jumlah
            total += subtotal

            keranjang.append({
                "nama": nama_produk,
                "harga": harga_produk,
                "jumlah": jumlah,
                "subtotal": subtotal
            })

            print(f"\n{nama_produk} berhasil ditambahkan!")

        else:
            print("Kode produk tidak ditemukan!")

    # ======================
    # LIHAT KERANJANG
    # ======================
    elif pilihan == "3":

        print("\n===== KERANJANG =====")

        if len(keranjang) == 0:
            print("Keranjang masih kosong!")

        else:
            for item in keranjang:
                print(
                    f"{item['nama']} | "
                    f"{item['jumlah']} x Rp{item['harga']} "
                    f"= Rp{item['subtotal']}"
                )

            print(f"\nTOTAL: Rp{total}")
    # ======================
    # CHECKOUT
    # ======================
    elif pilihan == "4":

        print("\n===== CHECKOUT =====")

        if len(keranjang) == 0:
            print("Keranjang kosong!")

        else:

            print("\n")
            print("=" * 35)
            print("     INDOMINI MARKET 😎🔥")
            print("=" * 35)

            for item in keranjang:
                print(
                    f"{item['nama']}"
                )

                print(
                    f"{item['jumlah']} x Rp{item['harga']} "
                    f"= Rp{item['subtotal']}"
                )

                print("-" * 35)

            print(f"TOTAL BELANJA : Rp{total}")

            bayar = int(input("Uang Pembayaran : Rp"))

            if bayar < total:
                print("Uang tidak cukup!")

            else:

                kembalian = bayar - total

                print(f"Kembalian      : Rp{kembalian}")

                print("=" * 35)
                print(" Terima Kasih Sudah Belanja ")
                print("=" * 35)

                break

    # ======================
    # KELUAR
    # ======================
    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid!")