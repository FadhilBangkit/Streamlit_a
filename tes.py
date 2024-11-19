import streamlit as st
import cv2
import numpy as np
import random
import gspread
import time
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials
from concurrent.futures import ThreadPoolExecutor
from camera_input_live import camera_input_live

# image = camera_input_live(debounce=500,show_controls=False)
# image_value = image.getvalue()

# image_decode = cv2.imdecode(np.frombuffer(image_value, np.uint8), cv2.IMREAD_COLOR)
# st.write('halo')
def Sukses_ujian():
    return st.markdown('''# Doa Ujian Lancar agar Dimudahkan

**Arabic:**  
> اَللَّهُمَّ لاَ سَهْلَ إِلَّا مَا جَعَلْتَهُ سَهْلاً وَأَنْتَ تَجْعَلُ الْحَزْنَ إِذَا شِئْتَ سَهْلاً  
**Latin:**  
Allahuma laa sahla illa maa ja’altahu sahlan wa anta taj’alul hazna idzaa syi’ta sahlan.  
**Meaning:**  
“Ya Allah, tidak ada kemudahan kecuali apa yang Engkau jadikan mudah, sedang yang susah bisa Engkau jadikan mudah, apabila Engkau menghendakinya.”

---

# Doa Ujian Lancar Saat Memasuki Ruang Ujian

**Arabic:**  
> اَللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ عِلْمٍ لَا يَنْفَعُ, وَمِنْ قَلْبٍ لَا يَخْشَعُ, وَمِنْ نَفْسٍ لَا تَشْبَعُ, وَمِنْ دَعْوَةٍ لَا يُسْتَجَابُ لَهَا  
**Latin:**  
Allahuma innii a’uudzu bika min ‘ilmin laa yanfa’u wa qolbin laa yakhsya’u wa du’aa-in laa yusma’u wa ‘amalin laa yurfa’u.  
**Meaning:**  
“Ya Allah, aku berlindung kepada-Mu dari ilmu yang tidak bermanfaat, hati yang tidak khusyu, doa yang tidak didengar, dan amal yang tidak diterima.”

---

# Doa Ujian Lancar Sebelum Mengikuti Ujian

**Arabic:**  
> سُبْحَانَكَ اللَّهُمَّ لَأَعِلْمَ لَنَا إِلَّا مَا عَلَّمْتَنَا وَ عَلَّمْنَا مَا يَنْفَعُنَا وَبَارِكْ لَنَا فِي مَا عَلَّمْتَنَا إِنَّكَ أَنْتَ الْعَلِيمُ الْحَكِيمُ.  
**Latin:**  
Subhaanakallaahumma laa ilma lanaa illaa maa ‘allamtanaa wa’allimnaa maa yanfa’unaa wa baarik lanaa fii maa ‘allamtanaa innaka antal ‘aliimul hakiimu.  
**Meaning:**  
“Maha Suci Engkau ya Allah, kami tidak akan memiliki ilmu kecuali Engkau mengajari kami, maka ajarilah kami ilmu yang bermanfaat bagi kami dan berkahilah kami dalam apa yang telah Engkau ajari untuk kami. Sesungguhnya Engkau Maha Tahu lagi Maha Bijaksana.”

---

# Doa Ujian Lancar agar Lulus

**Arabic:**  
> اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدِ الْفَاتِحِ لِمَا أُغْلِقَ وَالْخَاتِمِ وَالْخَاتِمِ ! لِمَا سَبَقَ نَاصِرِ الْحَقِّ بِالْحَقِّ وَالْهَادِ إِلَى صِرَاطِكَ الْمُسْتَقِيمِ وَعَلَى آلِهِ وَصَحْبِهِ حَقَّ قَدْرِهِ وَمِقْدَارِهِ الْعَظِيمِ  
**Latin:**  
Allaahumma shalli alaasayyidinaamuhammadinil faatihi limaa ughliqa wal khaatimi limaa sabaqa naashiril haqqi bil haqqi wal haadi ilaa shiraathikal mustaqiimi wa ‘alaa aalihi wa shahbihi haqqa qadrihi wamiqdaarihil ‘azhimi.  
**Meaning:**  
“Ya Allah limpahkanlah rahmat dan keagungan atas tuan kami, Nabi Muhammad Saw., yang menjadi pembuka bagi segala yang terkunci yang menjadi penutup bagi segala yang dahulu, yang memperjuangkan kebenaran dengan kebenaran dan yang menunjukan kepada-Mu yang lurus, dan juga atas keluarga dan para sahabatnya dengan hak kapasitas dan derajat yang agung.”

---

# Doa Ujian Lancar sesuai Imam An-Nawawi

**Arabic:**  
> رَبِّ يَسِّرْ وَأَعِنْ وَلَا تُعَسِّرْ  
**Latin:**  
Rabbi yassir wa a’in wa la tu’assir.  
**Meaning:**  
"Wahai Tuhanku, mudahkanlah, bantulah (aku), jangan kau persulit."

**Source:** Imam An-Nawawi, Raudhatut Thalibin.

---

# Doa Ujian Lancar sesuai Surah Al-Kahfi

**Arabic:**  
> اِذْ اَوَى الْفِتْيَةُ اِلَى الْكَهْفِ فَقَالُوْا رَبَّنَآ اٰتِنَا مِنْ لَدُنْكَ رَحْمَةً وَهَيِّئْ لَنَا مِنْ اَمْرِنَا رَشَدًا  
**Latin:**  
Idz awalfityatu ilalkahfi faqooluu rabbanaa aatinaa minladunka rahmatan wahayyi lanaa min amrina rasyadaa.  
**Meaning:**  
“Ya Tuhan kami, berikanlah rahmat kepada kami dari sisi-Mu, dan sempurnakanlah bagi kami petunjuk yang lurus dalam urusan kami.”

**Source:** Surah Al-Kahfi, Ayah 10.

---

# Doa Ujian Lancar sesuai Surah Thaha

**Arabic:**  
> قَالَ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي وَاحْلُلْ عُقْدَةً مِنْ لِسَانِي يَفْقَهُوا قَوْلِي  
**Latin:**  
Rabbisyah li sadri wa yassir li amri wahlul ‘uqdatam mil lisani yafqahu qauli.  
**Meaning:**  
“Ya Tuhanku, lapangkanlah dadaku, mudahkanlah urusanku, dan lepaskanlah kekakuan lidahku, agar mereka memahami perkataanku.”

**Source:** Surah Thaha, Ayah 25-28.
''')

Cred_list = [
    "Cred/Cred.json",
    "Cred/Cred_Aghil.json",
    "Cred/Cred_Bangkit.json",
    "Cred/Cred_Fadhil119.json",
    "Cred/Cred_Fadhil14039.json",
    "Cred/Cred_FadhilULM.json",
    "Cred/Cred_M.json"
]



# if image:
#     st.image(image)
face_ref = cv2.CascadeClassifier('tes.xml')

def face_detection(cv2_img):
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    faces = face_ref.detectMultiScale2(cv2_img, scaleFactor=1.1)
    return faces

def Box(cv2_img):
    rects, _ = face_detection(cv2_img)
    # print(rects)
    for x, y, w, h in rects:
        radius = np.int32((h/2)*0.2)
        x =np.int32((2*x + w)*0.5)
        y =np.int32((2*y + h)/2)

        cv2_img_rect = cv2.circle(cv2_img, (x, y), radius, color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), thickness=-5)
        
        return cv2_img_rect

def background_deteksi_wajah(Gambar):
    if Gambar is not None:
        cv2_img = Box(Gambar)
        if cv2_img is not None:
            st.session_state.Wajah =True
            
            return True, cv2_img
        else:
            st.session_state.Wajah = False
            print('False')
            return False, None
    else:
        st.session_state.Wajah = False
        return False, None

def form_page():
    with st.form(key='My_form'):
        Nama = st.text_input('Masukkan Nama Lengkap anda')
        NIM = st.text_input('Masukkan NIM anda')
        Angkatan = st.text_input('Masukkan Angkatan anda')
        Digit_terakhir_nim = st.text_input('Masukkan digit Terakhir NIM anda')
        st.info('Masukkan Kode anda sesuai di colab')
        Kode = st.text_input('Masukkan kode anda')
        submit_button = st.form_submit_button('Submit')
        if submit_button:
            kirim_ke_sps_form(Nama, NIM, Angkatan, Digit_terakhir_nim, Kode)
            st.info('Data Sudah disubmit')
            with st.spinner('Tunggu Sebentar'):
                time.sleep(5)
            st.session_state.Nama = Nama
            st.session_state.Mengisi_form = True
            st.rerun()

def tampilkan_warning(hasil_deteksi):
    if hasil_deteksi:
        st.warning('Wajah Anda terlihat')
    else:
        st.error('Wajah anda tidak erlihat')

def tampilkan_gambar(hasil_deteksi, gambar_terdeteksi, gambar_tidak_terdeteksi):
    if hasil_deteksi:
        st.image(gambar_terdeteksi, caption='Semangat Ujiannya Ganteng/Cantik')
    else:
        st.image(gambar_tidak_terdeteksi, caption='Semangat Ujiannya Ganteng/Cantik')
            

def mulai_sps():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    Cred_pilihan = random.choice(Cred_list)
    creds = Credentials.from_service_account_file('Cred_Aghil_2.json', scopes=scopes)
    client = gspread.authorize(creds)
    sheet_id = "1F1xTqTI603vxn7-WY7Kg4XN0L62BF43AX5a6RSAA_2Y"
    workbook = client.open_by_key(sheet_id)
    return workbook

def kirim_ke_sps_form(Nama, NIM, Angkatan, Digit_terakhir_nim, Kode):
    workbook = mulai_sps()
    worksheet_name = 'Kondisi_wajah'
    try:
        worksheet = workbook.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = workbook.add_worksheet(title=worksheet_name, rows="1000", cols="1000")
    worksheet.append_row([Nama, NIM, Angkatan, Digit_terakhir_nim, Kode])

def kirim_ke_sps_kondisi_wajah(Kondisi_wajah, Nama):
    workbook = mulai_sps()
    worksheet_name = 'Kondisi_wajah'
    try:
        worksheet = workbook.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = workbook.add_worksheet(title=worksheet_name, rows="1000", cols="1000")
    Kolom_Nama = worksheet.col_values(1)
    if Nama in Kolom_Nama:
        index_baris = Kolom_Nama.index(Nama) + 1
        worksheet.update_cell(index_baris, 6, Kondisi_wajah)

def Mulai_deteksi_wajah(gambar):
    deteksi_wajah = ThreadPoolExecutor(1)
    lakukan_deteksi_wajah = deteksi_wajah.submit(background_deteksi_wajah, gambar)
    hasil_deteksi_wajah = lakukan_deteksi_wajah.result()
    return hasil_deteksi_wajah



def main():
    if 'Mengisi_form' not in st.session_state:
        st.title('Selamat Mengerjakan Ujian')
        st.session_state.Wajah = False
        st.session_state.Nama = None
        st.session_state.Mengisi_form = True
    
    if not st.session_state.Mengisi_form:
        form_page()
    
    print(st.session_state.Mengisi_form)

    if st.session_state['Mengisi_form']:
        gambar = camera_input_live(debounce=4000, show_controls=False)
        if gambar:
            gambar_value = gambar.getvalue()
            gambar_decode = cv2.imdecode(np.frombuffer(gambar_value, np.uint8), cv2.IMREAD_COLOR)
            gambar_handphone = cv2.resize(gambar_decode, (360, 640), interpolation=cv2.INTER_LINEAR)
            st.session_state.Wajah, gambar_terdeteksi = Mulai_deteksi_wajah(gambar_handphone)
            st.title('Halo Badut🤡!')
            tampilkan_warning(st.session_state.Wajah)
            tampilkan_gambar(st.session_state.Wajah, gambar_terdeteksi, gambar_handphone)
            st.header('Kumpulan doa dapat Nilai Baik')
            Sukses_ujian()
            





if __name__ == '__main__':
    main()


# deteksi_wajah = ThreadPoolExecutor(1)
# x =deteksi_wajah.submit(background_deteksi_wajah, image_decode).result()

# if x[0]:
#     st.session_state.Wajah =True
#     st.info('Ada Wajah')
#     tampil = st.image(x[1])
# else:
#     st.session_state.Wajah =False
#     st.error('Tidak Ada Wajah')
#     tampil = st.image(image)




