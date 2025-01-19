import tkinter as tk
from random import shuffle

def karistir_ve_goster():
    my_key = entry.get()  
    defchar_list = [".", "!", ".", "!"]
    char_list = list(my_key) 
    mix_list = char_list + defchar_list 
    shuffle(mix_list)  
    global result  
    result = "".join(mix_list) 
    result_label.config(text=f"Güçlü Şifre: {result}") 

def sifreyi_kopyala():
    if result:  
        window.clipboard_clear()  
        window.clipboard_append(result)  
        window.update()  
        result_label.config(text="Şifre kopyalandı!")

window = tk.Tk()
window.title("Şifre Güçlendirici")
window.geometry("400x200")

entry_label = tk.Label(window, text="Şifre girin:", font=("Arial", 12))
entry_label.pack(pady=5)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)

button = tk.Button(window, text="Güçlü Yeni Şifre Oluştur", font=("Arial", 12), command=karistir_ve_goster)
button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

copy_button = tk.Button(window, text="Şifreyi Kopyala", font=("Arial", 12), command=sifreyi_kopyala)
copy_button.pack(pady=10)

result = ""  # Global değişkeni başlangıç değeriyle tanımlıyoruz
window.mainloop()
