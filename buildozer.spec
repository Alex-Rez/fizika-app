[app]
title = Физика: Теплообмен
package.name = fizika_teploobmen
package.domain = org.tvoynik
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
version.code = 1
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0

# Требования
requirements = python3,flet

# Разрешения
android.permissions = INTERNET

# Стабильные версии (НЕ preview!)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.sdk = 33
android.accept_all_licenses = True

[buildozer]
log_level = 2
warn_on_root = 1
