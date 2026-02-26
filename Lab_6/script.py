print("isimler islemi basladi--------------------------------------------------------------------")

for i in range(150):
    if i % 3 :
        print("carlos")
    else:
        print("wiener")


print("\n\n\n\n\n\n\n\nsifreler islemi basladi--------------------------------------------------------------------")


with open("/home/erdem/GitHub/Broken Authentication/Lab_6/password.txt", "r") as f:
    line=f.readlines()


i=0

for l in line:
    if i % 3 :
        print(l.strip('\n'))
    else:
        print("peter")
        print(l.strip('\n'))
        i+=1
    i+=1

print("islemler tamamlandi")
