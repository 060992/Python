# import library
import time
import datetime

# input nama user
nama = input("hallo.. nama saya mr.kompie, nama anda siapa?")

#tampilkan nama user
print("oh.. nama anda "+ nama + " nama yang bagus sekali")

#kasih jeda 3 detik
time.sleep(3)

#input tahun lahir
thnLahir = int(input("BTW.. "+ nama + " kamu lahir tahun berapa?"))

#kasih jeda 3 detik
time.sleep(3)

# hitung usia user
skrg = datetime.datetime.now()
usia = skrg.year - thnLahir

#tampilkan usia
print("hmmm..", nama, "kamu sudah", usia, "tahun yaa")

#kasih jeda 3 detik
time.sleep(3)

#tampilkan pesan sesuai range usia
if usia > 50:
    print("anda sudah cukup tua ya?")
    print("jaga kesehatan yaa")
elif usia > 20:
    print("ternyata anda masih cukup muda belia")
    print("jangan sia siakan masa mudamu ya")
elif usia > 17:
    print("hihihi.. ternyata anda masih abg")
    print("mulai berpikirlah secara dewasa ya!!")
else:
    print("oalah.. anda masih anak anak toh?")
    print("jangan suka merengek minta jajan yaa!!")

#kasih jeda 3 detik
time.sleep(3)

#say goodbye
print("Ok.. see you later " + nama + "..senang berkenalan dengan mu")