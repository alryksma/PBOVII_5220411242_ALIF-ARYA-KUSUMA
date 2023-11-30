class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Ll:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def tambah_node(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

class Perpustakaan:
    def __init__(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek

    def lokasiPenyimpanan(self):
        return "Lokasi penyimpanan belum ditentukan"

    def info(self):
        return f"Judul: {self.judul}, Subjek: {self.subjek}"

class DVD(Perpustakaan):
    def __init__(self, judul, subjek, aktor, genre):
        super().__init__(judul, subjek)
        self.aktor = aktor
        self.genre = genre

    def tampilkan_info(self):
        return f"{super().info()}, Aktor: {self.aktor}, Genre: {self.genre}"

class Majalah(Perpustakaan):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue

    def tampilkan_info(self):
        return f"{super().info()}, Volume: {self.volume}, Issue: {self.issue}"

class Buku(Perpustakaan):
    def __init__(self, judul, subjek, isbn, pengarang, jmlhal, ukuran):
        super().__init__(judul, subjek)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal
        self.ukuran = ukuran

    def tampilkan_info(self):
        return f"{super().info()}, ISBN: {self.isbn}, Pengarang: {self.pengarang}, Jumlah Halaman: {self.jmlhal}, Ukuran: {self.ukuran}"

class Pengarang(Buku):
    def __init__(self, judul, subjek, isbn, pengarang, jmlhal, ukuran, nama):
        super().__init__(judul, subjek, isbn, pengarang, jmlhal, ukuran)
        self.nama = nama
        self.daftar_pengarang = Ll(self)

    def info(self):
        return f"{super().tampilkan_info()}, Nama Pengarang: {self.nama}"

    def cari_pengarang(self, pengarang):
        current_node = self.daftar_pengarang.head
        while current_node:
            if current_node.data.pengarang.lower() == pengarang.lower():
                return current_node.data
            current_node = current_node.next
        return None


class Katalog(Perpustakaan):
    def __init__(self, judul, subjek):
        super().__init__(judul, subjek)
        self.daftar_buku = Ll(self)

    def tambah_buku(self, buku):
        self.daftar_buku.tambah_node(buku)

    def cari_buku(self, judul):
        current_node = self.daftar_buku.head
        while current_node:
            if current_node.data.judul.lower() == judul.lower():
                return current_node.data
            current_node = current_node.next
        return None

    def tampilkan_buku(self):
        current_node = self.daftar_buku.head
        while current_node:
            if isinstance(current_node.data, Buku):  # Menambahkan kondisi untuk jenis buku
                print(current_node.data.tampilkan_info())
            else:
                print(current_node.data.info())
            current_node = current_node.next

# Contoh penggunaan
katalog = Katalog("Katalog Umum", "Umum")
buku1 = Buku("Dosa Besar Suharto", "Non-fiksi", "123456789", "Aldi", 200, "A5")
buku2 = Buku("Kisah Asmara Zaki dan Sindi", "Fiksi", "987654321", "Aldi", 150, "B5")
dvd1 = DVD("Judul DVD", "DVD", "Aktor DVD", "Genre DVD")
majalah1 = Majalah("Judul Majalah", "Majalah", "Volume Majalah", "Issue Majalah")

katalog.tambah_buku(buku1)
katalog.tambah_buku(buku2)
katalog.tambah_buku(dvd1)
katalog.tambah_buku(majalah1)

# Mencari buku
nyari = input("apa buku yang mau anda cari: ")
print("buku :")
hasil_pencarian = katalog.cari_buku(nyari)
if hasil_pencarian:
    print("Buku ditemukan:", hasil_pencarian.tampilkan_info())
else:
    print("Buku tidak ditemukan.")

print("="*100)
# Menampilkan semua buku dalam katalog
katalog.tampilkan_buku()
