import streamlit as st

col1, col2, col3 = st.columns([1,7,1])
with col2:
    st.image("logo.png")

options_merchan = {
    "Tumbler Choco Luxe": {"Harga": 120000, "gambar": "tumbler.PNG"},
    "Mug Velvet": {"Harga": 90000, "gambar": "mug.PNG"},  
    "Tote bag Chocoa Carry": {"Harga": 75000, "gambar": "totebag.PNG"},
    "Kaos Choco Vibe": {"Harga": 150000, "gambar": "baju.PNG"},
    "Apron Choco Craft": {"Harga": 130000, "gambar": "apron.PNG"},
    "Notebook Mocha Note": {"Harga": 85000, "gambar": "notebook.PNG"},
    "Paket Chocoa Starter": {"Harga": 180000, "gambar": "tumbler1.PNG"},
    "Paket Barista Set": {"Harga": 200000, "gambar": "barista.PNG"},
    "Paket Choco Lifestle": {"Harga": 320000, "gambar": "baju1.PNG"}
}

st.title("Merchandise")
index = 0
for row in range(3):
    cols = st.columns(3) 
    for col in range(3):
        if index < len(options_merchan):  
            option, details = list(options_merchan.items())[index]
            with cols[col]: 
                st.image(details["gambar"], caption=option)

                if st.button(f"Tambah {option} 1"):
                    def open_link(url):
                        st.markdown(f'<a href="{url}" target="_blank">Klik di sini untuk membuka link</a>', unsafe_allow_html=True)
                    if st.button("Buka Link"):
                        open_link("https://wa.me/6282331257397?text=Permisi+kak,+saya+ingin+memesan+produk+pel+peras+magic") 
            index += 1

