from PIL import Image

# Kullanilacak Gorseller
frame1 = Image.open("frame1.jpg")
frame2 = Image.open("frame2.jpg")
frame3 = Image.open("frame3.jpg")

# Gorselleri Gife Donusturme
frame1.save(
    "animation.gif",#Cikti Dosyasi
    save_all = True, #Tum Kareleri Kaydet
    append_images = [frame2, frame3],
    duration = 200, #Her karenin gosterim suresi
    loop = 0, #Dongu sayisi
)