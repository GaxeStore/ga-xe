import streamlit as st
import webbrowser

st.markdown("""
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '2957774121062477');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=2957774121062477&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
""", unsafe_allow_html=True)

# Menampilkan logo
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("logo.png")

# Data produk
options_merchan = {
    "Rak Dapur Pengering Piring": {"page": 30000, "gambar": "rakm.png"},
    "Rak Organizer Susun": {"page": 90000, "gambar": "rakp.png"},
    "Toples Penyimpanan": {"page": 75000, "gambar": "toples.png"},
    "Sikat Electric": {"page": 150000, "gambar": "sikat.png"},
    "Super Senter LED": {"page": 130000, "gambar": "senter.png"},
    "Toothpick Otomatis": {"page": 85000, "gambar": "tootp.png"},
    "Alat Pel Peras": {"page": 180000, "gambar": "pelperas.png"},
    "Alat Pel Semprot": {"page": 200000, "gambar": "pelsemprot.png"},
    "Vacuum Cleaner": {"page": 320000, "gambar": "vcm.png"}
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
                    webbrowser.open("https://wa.me/6282331257397?text=Permisi+kak,+saya+ingin+memesan+{selected_product}")
                    # Menampilkan link setelah tombol ditekan
                    #st.markdown(f'<a href="https://wa.me/6282331257397?text=Permisi+kak,+saya+ingin+memesan+{option}" target="_blank">Klik di sini</a>', unsafe_allow_html=True)
            index += 1

col1, col2, col3 = st.columns([1, 10, 1])
with col2:
    st.markdown("<h3 style='text-align: center;'>Note:</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Mohon untuk melakukan video unboxing dan pengecekan barang</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Komplain tanpa video unboxing dan foto bukti tidak akan di terima.</p>", unsafe_allow_html=True)
