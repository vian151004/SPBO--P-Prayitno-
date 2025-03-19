# Kelas untuk merepresentasikan atribut dan metode HP
class HP:
    def __init__(self, merk, model, tahun, harga):
        # Atribut yang dimiliki oleh objek HP
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.harga = harga

    # Fungsi tanpa return value, hanya mencetak informasi
    def tampilkan_info(self):
        print(f"HP {self.merk}, {self.model}, tahun {self.tahun}, harga: Rp {self.harga}")
        print("-" * 40)  # Garis batas

    # Fungsi dengan satu parameter
    def diskon(self, persen_diskon):
        # Menghitung harga setelah diskon
        diskon_harga = self.harga * (persen_diskon / 100)
        harga_setelah_diskon = self.harga - diskon_harga
        print(f"Harga setelah diskon {persen_diskon}%: Rp {harga_setelah_diskon}")
        print("-" * 40)  # Garis batas

    # Fungsi dengan return value, menghitung usia HP berdasarkan tahun
    def hitung_usia(self, tahun_sekarang):
        usia = tahun_sekarang - self.tahun
        return usia

    # Fungsi dengan beberapa parameter
    def perbarui_harga(self, harga_baru, tahun_baru):
        self.harga = harga_baru
        self.tahun = tahun_baru
        print(f"Harga dan tahun HP {self.merk} {self.model} diperbarui menjadi Rp {self.harga} dan tahun {self.tahun}")
        print("-" * 40)  
