Link PWS: https://priyanggara-zuhaynanda-timtarkamshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat direktori utama dengan nama "TTS" sebagai tempat penyimpanan seluruh project. Setelah itu, saya membuat virtual environment di dalam direktori tersebut untuk mengisolasi dependensi project. Saya memastikan seluruh dependensi yang dibutuhkan, seperti Django, sudah terinstall di virtual environment ini.

Selanjutnya, saya membuat project Django dengan menjalankan perintah django-admin startproject tim_tarkam_shop. Setelah project berhasil dibuat, saya melakukan konfigurasi pada environment variable dan file-file utama seperti settings.py agar sesuai dengan kebutuhan project.

Untuk membuat aplikasi utama, saya menjalankan perintah python manage.py startapp main. Setelah aplikasi main berhasil dibuat, saya menambahkannya ke dalam daftar INSTALLED_APPS pada file settings.py agar Django dapat mengenali aplikasi tersebut.

Saya melakukan konfigurasi routing pada file urls.py di direktori project utama (tim_tarkam_shop). Pada file ini, saya mengimpor fungsi path dan include dari django.urls, lalu menambahkan baris path('', include('main.urls')) ke dalam urlpatterns. Hal ini bertujuan agar seluruh routing aplikasi main dapat diakses melalui project utama.

Pada file models.py di aplikasi main, saya membuat class Product yang merepresentasikan produk pada toko. Model ini memiliki atribut wajib seperti name, price, description, thumbnail, category, dan is_featured. Selain itu, saya juga menambahkan atribut tambahan seperti stock, brand, size, dan color untuk memperkaya informasi produk. Saya juga menambahkan beberapa fungsi pada model, seperti is_in_stock untuk mengecek ketersediaan stok dan short_description untuk menampilkan ringkasan deskripsi produk.

Saya membuat file baru bernama urls.py di dalam direktori aplikasi main. Pada file ini, saya mendefinisikan routing yang memetakan URL ke fungsi-fungsi yang ada di views.py. Dengan demikian, setiap permintaan ke aplikasi main dapat diarahkan ke fungsi yang sesuai.

Pada file views.py, saya membuat fungsi bernama show_main yang bertugas menampilkan nama aplikasi, nama saya, dan NPM saya. Fungsi ini akan mengembalikan data tersebut ke template HTML yang telah saya buat di folder templates/main.html. Setelah model selesai dibuat, saya menjalankan perintah python manage.py makemigrations dan python manage.py  migrate untuk membuat dan menerapkan skema database sesuai dengan model yang telah didefinisikan.

Di akhir, saya melakukan deployment melalui PWS dengan menkana tombol buat projek baru, dan melakukan penyesuaian pada bagian environs. Lalu saya menjalankan perintah yang terdapat pada informasi Project Command pada halaman PWS dan memasukkan username dan password yang sebelumnya telah saya catat.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
link canva bagan: https://www.canva.com/design/DAGygKjlvS8/PS5wNSaJ6r4Ttq-9ecjy7w/edit?utm_content=DAGygKjlvS8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

3. Jelaskan peran settings.py dalam proyek Django!
Dalam sebuah proyek Django, berkas settings.py berperan sebagai pusat konfigurasi yang mengatur hampir seluruh aspek perilaku aplikasi. Di dalamnya tersimpan pengaturan dasar seperti SECRET_KEY untuk keamanan, DEBUG untuk menentukan mode pengembangan atau produksi, serta ALLOWED_HOSTS untuk membatasi domain yang diizinkan untuk mengakses aplikasi. Berkas ini juga memuat daftar aplikasi yang digunakan (INSTALLED_APPS), middleware yang memproses request dan response, konfigurasi database (DATABASES), pengaturan template HTML, serta lokasi penyimpanan file statis dan media. Selain itu, settings.py mengatur bahasa (LANGUAGE_CODE), zona waktu (TIME_ZONE), dan opsi keamanan tambahan seperti penggunaan HTTPS atau pengaturan cookie. Setiap kali server Django dijalankan, framework akan membaca settings.py untuk menentukan bagaimana request diproses, data diambil dari database, dan hasil akhirnya dirender menjadi HTML sebelum dikirim kembali ke browser pengguna. Jadi, settings.py memiliki peran yang sangat signifikan dalanm proyek Django.

4. Bagaimana cara kerja migrasi database di Django?
Cara kerja migrasi database di Django adalah dengan menyesuaikan perubahan yang dibuat pada model agar langsung tercermin di dalam struktur database. Jadi, ketika developer menambah, mengubah, atau menghapus bagian dari model, Django bisa otomatis membuat catatan perubahan tersebut melalui perintah makemigrations. Selanjutnya, perintah migrate akan menerapkan perubahan itu ke database, misalnya dengan membuat tabel baru, menambahkan kolom, atau mengganti jenis data, sambil tetap menyimpan riwayat migrasi di tabel khusus. Dengan cara ini, developer tidak perlu repot menulis kode SQL sendiri, karena Django sudah mengatur agar struktur database selalu sesuai dengan model yang didefinisikan.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dipakai sebagai langkah awal untuk belajar membuat aplikasi berbasis web karena sudah menyediakan banyak hal penting yang dibutuhkan tanpa harus menambah banyak komponen lain. Framework ini memberikan panduan yang jelas dalam menyusun proyek, lengkap dengan dokumentasi yang mudah diikuti. Di dalamnya juga sudah ada konsep dasar pengembangan web, seperti cara mengatur jalannya aplikasi, menghubungkannya dengan database, hingga menampilkan hasil ke pengguna. Dengan begitu, pemula bisa lebih cepat memahami bagaimana sebuah aplikasi web bekerja dari awal sampai akhir.

Selain itu, Django membiasakan penggunanya untuk menulis kode dengan rapi dan teratur, sehingga sejak awal belajar sudah terbentuk pola kerja yang baik. Fitur keamanan yang tersedia juga membantu mahasiswa memahami betapa pentingnya menjaga aplikasi tetap aman dari berbagai ancaman. Berkat kemudahan, kelengkapan, dan kualitas standarnya, Django bisa jadi wadah belajar yang ideal sebelum mencoba framework lain yang lebih ringan atau lebih khusus.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tidak ada, sampai saat ini asdos-asdosnya sangat baik dalam menanggapi pertanyaan yang saya berikan.
