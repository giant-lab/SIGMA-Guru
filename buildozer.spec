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
    kivymd==1.1.1,
    pandas,
    openpyxl,
    plyer,  # Diperbaiki dari 'flyer' ke 'plyer'
    android,
    libiconv  # Diperlukan untuk kompatibilitas Android

# Konfigurasi jam Kivy
osx.kivy_clock = interrupt
linux.kivy_clock = interrupt
win.kivy_clock = interrupt

[buildozer]
p4a.branch = stable
log_level = 2  # Level log lebih detail

# Konfigurasi Android
android.arch = arm64-v8a  # Diperbaiki dari 'archs' ke 'arch'
android.api = 33
android.minapi = 21
android.ndk = 25b

# Izin
android.permissions = 
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE

# Konfigurasi Android 10+ (Scoped Storage)
android.enable_android_storage = True
android.manifest_application_arguments = android:requestLegacyExternalStorage="true"
android.manifest_features = 
    <uses-feature android:name="android.hardware.touchscreen" android:required="false"/>

# Konfigurasi tambahan untuk optimasi
android.allow_backup = False
android.enable_androidx = True
android.ndk_api = 23

# Orientasi
orientation = portrait

# Layar penung
fullscreen = 0

# Presplash (opsional)
#presplash.filename = %(source.dir)s/images/splash.png

# Icon (opsional)
#icon.filename = %(source.dir)s/images/icon.png

# Batasi jumlah arsitektur untuk mempercepat build
android.arch = arm64-v8a
