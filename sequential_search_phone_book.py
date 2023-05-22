def sequential_search_phone_book(name, phone_book):
    for contact_name, phone_number in phone_book.items():
        if contact_name == name:
            return phone_number
        
    return None

# Daftar buku nomor telepon
phone_book = {
    "John Doe": "081234567890",
    "Jane Smith": "089876543210",
    "Michael Johnson": "087811223344",
    "Emily Davis": "082122232425"
}

# Nama untuk mencari nomor telepon
name = "Jane Smith"

# Mencari nomor telepon
phone_number = sequential_search_phone_book(name, phone_book)

# Menampilkan nomor telepon Jane Smith
if phone_number:
    print("Nomor Telepon", name, "adalah", phone_number)
else:
    print("Nomor Telepon", name, "Tidak ditemukan.")