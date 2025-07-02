import streamlit as st
from manajer_kontak import ManajerKontak
from model import Kontak

manajer = ManajerKontak()

st.set_page_config(
    page_title="📇 Manajemen Kontak",
    page_icon=":card_index:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("📇 Aplikasi Manajemen Kontak")

menu = st.sidebar.radio(
    "📌 Navigasi Menu",
    ["➕ Tambah Kontak", "📋 Lihat Kontak", "🔍 Cari Kontak", "✏️ Edit Kontak"],
    key="menu"
)

st.sidebar.info("Contoh Projek OOP Sederhana\nPython x Streamlit")
st.markdown("---")

if menu == "➕ Tambah Kontak":
    st.subheader("Tambah Kontak Baru")
    col1, col2 = st.columns([2, 2])
    with col1:
        nama = st.text_input("👤 Nama Lengkap")
    with col2:
        telepon = st.text_input("📞 Nomor Telepon")
    email = st.text_input("📧 Email (Opsional)")

    if st.button("💾 Simpan Kontak"):
        if nama.strip() and telepon.strip():
            k = Kontak(nama.strip(), telepon.strip(), email.strip())
            manajer.tambah_kontak(k)
            st.success(f"✅ Kontak *{nama}* berhasil disimpan!")
        else:
            st.warning("⚠️ Nama & Telepon wajib diisi!")

elif menu == "📋 Lihat Kontak":
    st.subheader("📋 Daftar Kontak")
    df = manajer.get_kontak_df()
    if df.empty:
        st.info("Belum ada kontak.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.write("## 🔴 Hapus Kontak")
        id_hapus = st.number_input("Masukkan ID Kontak:", min_value=1, step=1)
        if st.button("🗑️ Hapus Kontak"):
            manajer.hapus_kontak(id_hapus)
            st.success(f"Kontak dengan ID {id_hapus} berhasil dihapus.")
            st.rerun()

elif menu == "🔍 Cari Kontak":
    st.subheader("🔍 Cari Kontak")
    keyword = st.text_input("Masukkan kata kunci nama kontak:")
    if keyword.strip():
        df_hasil = manajer.cari_kontak_df(keyword.strip())
        if df_hasil.empty:
            st.warning("Tidak ada kontak yang cocok.")
        else:
            st.dataframe(df_hasil, use_container_width=True, hide_index=True)
    else:
        st.info("Masukkan minimal 1 huruf.")

elif menu == "✏️ Edit Kontak":
    st.subheader("✏️ Edit Kontak")
    id_kontak = st.number_input("Masukkan ID Kontak:", min_value=1, step=1)

    if st.button("🔍 Cari Kontak Berdasarkan ID"):
        kontak = manajer.get_kontak_by_id(id_kontak)
        if kontak:
            st.success(f"Ditemukan: {kontak.nama}")

            nama_baru = st.text_input("Nama Baru", kontak.nama, key=f"nama_edit_{id_kontak}")
            telepon_baru = st.text_input("Telepon Baru", kontak.telepon, key=f"telepon_edit_{id_kontak}")
            email_baru = st.text_input("Email Baru", kontak.email or "", key=f"email_edit_{id_kontak}")

            if st.button("💾 Simpan Perubahan"):
                kontak.nama = nama_baru.strip() or kontak.nama
                kontak.telepon = telepon_baru.strip() or kontak.telepon
                kontak.email = email_baru.strip()

                manajer.edit_kontak(kontak)
                st.success(f"Kontak ID {kontak.id} berhasil diperbarui.")
                st.session_state["menu"] = "📋 Lihat Kontak"
                st.rerun()
        else:
            st.error("Kontak tidak ditemukan.")
