import streamlit as st

# Menampilkan logo
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("logo.png")

# Data produk
options_merchan = {
    "Rak Dapur Pengering Piring": {"Harga": 120000, "gambar": "rakm.webp"},
    "Rak Organizer Susun": {"Harga": 90000, "gambar": "rakp.webp"},
    "Toples Penyimpanan": {"Harga": 75000, "gambar": "toples.webp"},
    "Sikat Electric": {"Harga": 150000, "gambar": "sikat.webp"},
    "Super Senter LED": {"Harga": 130000, "gambar": "senter.webp"},
    "Toothpick Otomatis": {"Harga": 85000, "gambar": "tootp.webp"},
    "Alat Pel Peras": {"Harga": 180000, "gambar": "pelperas.webp"},
    "Alat Pel Semprot": {"Harga": 200000, "gambar": "pelsemprot.webp"},
    "Vacuum Cleaner": {"Harga": 320000, "gambar": "vcm.webp"}
}

index = 0

# Menampilkan produk dalam kolom
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        if index < len(options_merchan):
            option, details = list(options_merchan.items())[index]
            with cols[col]:
                st.image(details["gambar"], caption=option)
                if st.button(f"Pesan {option} via Whatsapp"):
                    # Menampilkan link setelah tombol ditekan
                    st.markdown(f'<a href="https://wa.me/6282331257397?text=Permisi+kak,+saya+ingin+memesan+{option}" target="_blank">Klik di sini</a>', unsafe_allow_html=True)
            index += 1

