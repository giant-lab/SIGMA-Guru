[app]

# Nama aplikasi
title = SiGMA Guru

# Nama paket (reverse-DNS)
package.name = sigmaguru

# Domain paket
package.domain = com.giantlab

# Direktori sumber
source.dir = .

# Ekstensi file yang disertakan
source.include_exts = py,png,jpg,jpeg,kv,ttf,csv

# Pola penyertaan (untuk aset gambar)
source.include_patterns = images/*

# Direktori aset
source.include_dirs = images

# Tambahkan aset Android
android.add_assets = images

# File yang tidak dikompres
android.no_compress = *.png,*.jpg,*.jpeg

# Versi aplikasi
version = 1.0

# Persyaratan
requirements = 
    python3,
    kivy==2.3.0,
    kivymd==1.2.0,
    pandas,
    numpy,
    android

# Konfigurasi jam Kivy
osx.kivy_clock = interrupt
linux.kivy_clock = interrupt
win.kivy_clock = interrupt

# Konfigurasi Android
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b

# Izin
android.permissions = 
    INTERNET,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE

# Konfigurasi Android 10+ (Scoped Storage)
android.enable_android_storage = True
android.manifest_application_arguments = android:requestLegacyExternalStorage="true"
android.manifest_features = 
    <uses-feature android:name="android.hardware.touchscreen" android:required="false"/>

# Konfigurasi iOS (opsional, bisa diabaikan jika hanya Android)
ios.kivy_ios_dir = ../kivy-ios
ios.appname = SiGuru

# Orientasi
orientation = portrait

# Layar penuh
fullscreen = 0

# Level log
log_level = 2
