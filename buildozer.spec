[app]
# Nama aplikasi yang akan ditampilkan di perangkat
title = SiGMA Guru

# Nama paket aplikasi (format reverse-DNS, contoh: com.nama_perusahaan.nama_aplikasi)
package.name = com.giantlab.sigmaguru

# Nama domain paket
package.domain = com.giantlab

# Direktori utama kode sumber aplikasi (biasanya direktori saat buildozer dijalankan)
source.dir = .

# Daftar ekstensi file yang akan disertakan dalam APK
# Pastikan semua aset seperti gambar, font, dll., dengan ekstensi ini akan masuk
source.include_exts = py,png,jpg,jpeg,kv,ttf,csv

# Pola untuk menyertakan file dan direktori secara rekursif
# 'images/*' akan menyertakan semua file di dalam direktori 'images'
source.include_patterns = images/*

# Direktori yang akan dicari untuk aset. Jika ada direktori 'images' di root proyek, ini akan meng-handle-nya.
source.include_dirs = images

# Tambahkan direktori 'images' sebagai aset Android. Ini penting agar aset terakses di perangkat.
android.add_assets = images

# Nonaktifkan kompresi untuk jenis file tertentu (opsional, dapat meningkatkan waktu loading untuk aset besar)
# Gunakan daftar koma tanpa spasi jika lebih dari satu
android.no_compress = *.png,*.jpg,*.jpeg

# Versi aplikasi (numerik, misal: 10 untuk 1.0, 11 untuk 1.1)
version = 1.0

# Daftar modul Python yang dibutuhkan aplikasi Anda.
# Kivy dan Python3 sudah disertakan secara otomatis oleh Buildozer,
# namun mencantumkannya di sini akan memastikan versi yang spesifik jika diperlukan.
requirements = 
    python3,
    kivy==2.3.0,
    kivymd==1.2.0,
    pandas,
    numpy,
    android

# Konfigurasi Kivy Clock (opsional, jika Anda perlu mengatur metode clock Kivy)
# 'interrupt' adalah pilihan yang baik untuk performa.
osx.kivy_clock = interrupt
linux.kivy_clock = interrupt
win.kivy_clock = interrupt

# Konfigurasi spesifik Android
# Arsitektur target (arm64-v8a adalah yang paling umum untuk perangkat modern)
android.archs = arm64-v8a

# API Level target Android (misal: 33 untuk Android 13)
android.api = 33

# API Level minimum yang didukung aplikasi
android.minapi = 21

# Versi NDK (Android Native Development Kit). Buildozer akan mengunduhnya jika tidak ada.
android.ndk = 25b

# Jalur ke p4a (Python for Android) dan SDK/NDK jika Anda mengelolanya secara manual.
# Biasanya, ini bisa dikosongkan karena Buildozer akan mengunduh dan mengelolanya.
android.p4a_dir = 
android.sdk = 
android.ndk_path = 
android.sdk_path = 

# Izin Android yang dibutuhkan aplikasi Anda.
# Tambahkan izin lain yang relevan seperti CAMERA, ACCESS_FINE_LOCATION, dll.
android.permissions = 
    INTERNET,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE

# Konfigurasi khusus untuk Android 10+ (Scoped Storage)
# 'android.enable_android_storage = True' diperlukan untuk akses penyimpanan yang benar pada API 29+.
# '<application android:requestLegacyExternalStorage="true"/>' mengaktifkan mode warisan penyimpanan
# untuk kompatibilitas mundur, tetapi tidak disarankan untuk aplikasi baru di Android 11+.
android.enable_android_storage = True
android.add_manifest_attr = 
    <uses-feature android:name="android.hardware.touchscreen" android:required="false"/>
    <application android:requestLegacyExternalStorage="true"/>

# Konfigurasi iOS (opsional, kosongkan jika hanya menargetkan Android)
ios.kivy_ios_dir = ../kivy-ios
ios.appname = SiGuru

# Aturan pemaketan aplikasi
# Orientasi layar aplikasi ('portrait', 'landscape', 'all')
orientation = portrait

# Mode layar penuh (0 untuk tidak layar penuh, 1 untuk layar penuh)
fullscreen = 0

# Tingkat log Buildozer (0=debug, 1=info, 2=warning, 3=error, 4=critical)
log_level = 2

# Perintah atau skrip yang akan dijalankan setelah proses build utama selesai (opsional)
# post.pymodules_install = pandas, numpy
