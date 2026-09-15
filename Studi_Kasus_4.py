produk = {
    "nama": "Kopi Susu Gula Aren",
    "harga": 18000,
    "stok": 50
}


while True:
    print("\n=== MENU PENGELOLAAN DATA PRODUK ===")
    print("1. Tampilkan Data")
    print("2. Tambah Kategori")
    print("3. Ubah Harga")
    print("4. Hapus Kategori")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    
    if pilihan == "1":
        print("\nData Produk:")
        print(produk)

   
    elif pilihan == "2":
        if "kategori" in produk:
            print("\nKategori sudah ada.")
        else:
            kategori = input("Masukkan kategori produk: ")
            produk["kategori"] = kategori
            print("\nSetelah Add:")
            print(produk)

    
    elif pilihan == "3":
        harga_baru = input("Masukkan harga baru: ")
        if harga_baru.isdigit():
            produk.update({"harga": int(harga_baru)})
            print("\nSetelah Update:")
            print(produk)
        else:
            print("\nInput harga harus berupa angka.")


    elif pilihan == "4":
        if "kategori" in produk:
            produk.pop("kategori")
            print("\nSetelah Delete:")
            print(produk)
        else:
            print("\nData kategori tidak ditemukan.")


    elif pilihan == "5":
        print("\nProgram selesai. Sampai jumpa!")
        break

    else:
        print("\nPilihan tidak valid, coba lagi ya.")