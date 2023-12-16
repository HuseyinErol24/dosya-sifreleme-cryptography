# Dosya Şifreleme ve Çözme

Bu Python programı, dosyaları şifrelemek ve çözmek için kullanılır. [cryptography](https://cryptography.io/en/latest/) kütüphanesini kullanır.

## Kurulum

1. Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) Python'u indirip yükleyin.
2. Terminal veya komut istemcisine aşağıdaki komutu girerek `cryptography` kütüphanesini yükleyin:

    ```bash
    pip install cryptography
    ```

## Kullanım

1. `dosya_şifrele.py` dosyasını çalıştırın.
2. Program size bir seçenek sunacaktır: Dosya şifreleme veya dosya çözme.
3. İlgili seçeneği seçtikten sonra, program sizden dosya uzantısını (örneğin, "c:/acer/merhaba.txt") alacak ve işlemi gerçekleştirecektir.

Not: Eğer program ilk kez çalıştırılıyorsa, bir anahtar dosyası ("şifre_kaydet.txt") oluşturulur. Bu dosya şifreleme ve çözme işlemlerinde kullanılır.şifreleme işlemini yaptıktan sonra dosyanın şifresini çözmek için bu anahtarı kullanacaksınız bu dosyadaki şifreyi saklayınız 

## HÜSEYİN EROL