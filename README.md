# P1_Komnum_D2
Richard Ryan              5025211141
Sandhika Surya Ardyanto   5025211022

Penugasan praktikum pertama ini adalah membuat program yang bisa menghasilkan akar dari suatu persamaan menggunakan metode bolzano serta menggambarkan grafik fungsinya
Metode bolzano ini sendiri merupakan metode akolade dimana dengan mengambil 2 nilai yang nilai fungsinya berbeda tanda maka dengan mencari terus nilai tengah mereka dan sedikit dilakukan operasi semacam binary search akan didapatkan akar yang diinginkan

Misalkan diambil nilai L dan R dengan nilai tengahnya M
Apabila f(M) * f(L) > 0 maka nilai L berubah menjadi M
Sebaliknya apabila f(M) * f(L) < 0 maka nilai R yang berubah menjadi nilai M

Metode bolzano dilakukan terus hingga akhirnya memenuhi salah satu syarat berikut
1) Nilai f(M) = 0 atau sangat mendekati 0 (disini saya menggunakan batas kesalahan 1e-9)
   Maka M bisa dianggap merupakan akar persamaan
2) Selisih nilai L dan R = 0 atau sangat mendekati 0 (disini saya menggunakan batas kesalahan 1e-9)
   Maka tidak terdapat akar persamaan diantara L dan R awal, atau nilai f(L) dan f(R) keduanya positif / keduanya negatif
   
Setelah berhasil menkoding metode bolzanonya, kami kemudian menggunakan salah satu module di python bernama matplotlib yang bisa digunakan untuk menggambar grafik yang diinginkan
Disini kami menggambar hingga 3 garis
1) grafik fungsi f(x)
2) garis y=0
3) garis x=M (jika M merupakan akar persamaan)
Garis y=0 dan x=M digunakan untuk membantu pengecekan kebenaran akar (jika ada nilainya bisa dipastikan, jika tidak ada maka nilai f(L) dan f(R) bisa terlihat)
