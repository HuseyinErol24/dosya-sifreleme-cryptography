from cryptography.fernet import Fernet

class Şifrele():
    def __init__(self):
        self.dosya_path = input("Dosya uzantısını giriniz: ")  # Örneğin, "c:/acer/merhaba.txt"
        
        try:
            with open("şifre_kaydet.txt", "rb") as file:
                self.şifre = file.read()
        except FileNotFoundError:
            self.şifre = Fernet.generate_key()
            with open("şifre_kaydet.txt", "wb") as dosya:
                dosya.write(self.şifre)

        self.data = self.veri_okuma()

    def veri_okuma(self):
        with open(self.dosya_path, "rb") as file:
            return file.read()

    def encrypt(self):
        sifreleme_method = Fernet(self.şifre)
        şifrelenen_data = sifreleme_method.encrypt(self.data)
        with open(self.dosya_path, "wb") as file:
            file.write(şifrelenen_data)

    def decrypt(self):
        sifreleme_method = Fernet(self.şifre)
        with open(self.dosya_path, "rb") as file:
            cozulecek_veri = file.read()
            
        cozulmus_veri = sifreleme_method.decrypt(cozulecek_veri)
        with open(self.dosya_path, "wb") as file:
            file.write(cozulmus_veri)

secim = input("Yapmak istediğiniz işlemi seçin: 1 (Şifreleme) / 2 (Çözme) ")
sifreleci = Şifrele()

if secim == "1":
    sifreleci.encrypt()
    print("Dosya başarıyla şifrelendi.")
elif secim == "2":
    sifreleci.decrypt()
    print("Dosya başarıyla çözüldü.")
else:
    print("Geçersiz seçim! Lütfen sadece 1 veya 2 girin.")
