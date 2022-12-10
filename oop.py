class Mahasiswa:
    #-- deklarasi nama proverti:
  def __init__(self):
    self.datamahasiswa = {
        'nama': [],
        'kelas': [],
        'uts':[],
        'uas':[],
        'nilai akhir':[]
    }

# methode untuk menampilkan data
def tampilkan(self):
    print("berikut adalah datanya")
    print(tabulate(self.datamahasiswa, headers=[
        'nama','kelas','uts','uas','nilai akhir'], tablefmt="fancy_grid"))
    
#methode menambahkan data
def tambah(self, nama):
    nama = int(input("masukan nama : "))
    kelas = int(input("masukan kelas : "))
    uts = int(input("masukan nilai uts : "))
    uas = int(input("masukan nilai uas : "))
    nilai_akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 /100)
    # menambahkan data
    self.datamahasiswa['nama'].append(nama)
    self.datamahasiswa['kelas'].append(kelas)
    self.datamahasiswa['uts'].append(uts)
    self.datamahasiswa['uas'].append(uas)
    self.datamahasiswa['nilai akhir'].append(nilai_akhir)
    print('data berhasil di tambahkan.')

#methode hapus data
def hapus(self, nama):
    if nama in self.datamahasiswa['nama']:
        namaIndex = self.datamahasiswa['nama'].index(nama)
        def self.datamahasiswa['nama'][namaIndex]
        def self.datamahasiswa['kelas'][namaIndex]
        def self.datamahasiswa['uts'][namaIndex]
        def self.datamahasiswa['uas'][namaIndex]
        def self.datamahasiswa['nilai akhir'][namaIndex]
        print("data berhasil dihapus")
    else:
        print("data tidak ditemukan")

    
    
    