Link PWS:

Pertama, saya membuat direktori utama dengan nama "TTS" sebagai tempat penyimpanan seluruh project. Setelah itu, saya membuat virtual environment di dalam direktori tersebut untuk mengisolasi dependensi project. Saya memastikan seluruh dependensi yang dibutuhkan, seperti Django, sudah terinstall di virtual environment ini.

Selanjutnya, saya membuat project Django dengan menjalankan perintah django-admin startproject tim_tarkam_shop. Setelah project berhasil dibuat, saya melakukan konfigurasi pada environment variable dan file-file utama seperti settings.py agar sesuai dengan kebutuhan project.

Untuk membuat aplikasi utama, saya menjalankan perintah python manage.py startapp main. Setelah aplikasi main berhasil dibuat, saya menambahkannya ke dalam daftar INSTALLED_APPS pada file settings.py agar Django dapat mengenali aplikasi tersebut.

Saya melakukan konfigurasi routing pada file urls.py di direktori project utama (tim_tarkam_shop). Pada file ini, saya mengimpor fungsi path dan include dari django.urls, lalu menambahkan baris path('', include('main.urls')) ke dalam urlpatterns. Hal ini bertujuan agar seluruh routing aplikasi main dapat diakses melalui project utama.

Pada file models.py di aplikasi main, saya membuat class Product yang merepresentasikan produk pada toko. Model ini memiliki atribut wajib seperti name, price, description, thumbnail, category, dan is_featured. Selain itu, saya juga menambahkan atribut tambahan seperti stock, brand, size, dan color untuk memperkaya informasi produk. Saya juga menambahkan beberapa fungsi pada model, seperti is_in_stock untuk mengecek ketersediaan stok dan short_description untuk menampilkan ringkasan deskripsi produk.

Saya membuat file baru bernama urls.py di dalam direktori aplikasi main. Pada file ini, saya mendefinisikan routing yang memetakan URL ke fungsi-fungsi yang ada di views.py. Dengan demikian, setiap permintaan ke aplikasi main dapat diarahkan ke fungsi yang sesuai.

Pada file views.py, saya membuat fungsi bernama show_main yang bertugas menampilkan nama aplikasi, nama saya, dan NPM saya. Fungsi ini akan mengembalikan data tersebut ke template HTML yang telah saya buat di folder templates/main.html. Setelah model selesai dibuat, saya menjalankan perintah python manage.py makemigrations dan python manage.py  migrate untuk membuat dan menerapkan skema database sesuai dengan model yang telah didefinisikan.

Di akhir, saya melakukan deployment melalui PWS dengan menkana tombol buat projek baru, dan melakukan penyesuaian pada bagian environs. Lalu saya menjalankan perintah yang terdapat pada informasi Project Command pada halaman PWS dan memasukkan username dan password yang sebelumnya telah saya catat.