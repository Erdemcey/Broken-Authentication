# 0000'dan 9999'a kadar tüm kombinasyonları hazırlar
with open("mfa_wordlist.txt", "w") as f:
    for i in range(1000,10000):
        # zfill(4) komutu sayıyı 4 haneye tamamlar (örn: 7 -> 0007)
        f.write(str(i).zfill(4) + "\n")

print("MFA listesi 'mfa_wordlist.txt' adıyla başarıyla oluşturuldu!")