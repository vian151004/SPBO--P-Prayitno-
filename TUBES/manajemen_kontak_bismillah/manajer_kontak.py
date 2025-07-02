from model import Kontak
import database

class ManajerKontak:
    def tambah_kontak(self, kontak: Kontak):
        sql = "INSERT INTO kontak (nama, telepon, email) VALUES (?, ?, ?)"
        params = (kontak.nama, kontak.telepon, kontak.email)
        kontak.id = database.execute(sql, params)
        return kontak.id

    def get_kontak_df(self):
        sql = "SELECT id, nama, telepon, email FROM kontak ORDER BY nama ASC"
        return database.fetch_df(sql)

    def hapus_kontak(self, id_kontak):
        sql = "DELETE FROM kontak WHERE id = ?"
        return database.execute(sql, (id_kontak,))

    def cari_kontak_df(self, keyword):
        sql = "SELECT id, nama, telepon, email FROM kontak WHERE nama LIKE ? ORDER BY nama ASC"
        return database.fetch_df(sql, (f"%{keyword}%",))

    def get_kontak_by_id(self, id_kontak):
        sql = "SELECT * FROM kontak WHERE id = ?"
        rows = database.fetch(sql, (id_kontak,))
        if rows:
            row = rows[0]
            return Kontak(*row[1:], id_kontak=row[0])
        return None

    def edit_kontak(self, kontak: Kontak):
        sql = "UPDATE kontak SET nama = ?, telepon = ?, email = ? WHERE id = ?"
        params = (kontak.nama, kontak.telepon, kontak.email, kontak.id)
        database.execute(sql, params)
        return True
