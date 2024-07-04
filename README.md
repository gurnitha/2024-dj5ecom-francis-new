# 2024-dj5ecom-francis-new
Membuat aplikasi ecommerce menggunakan Django versi 5.0.3



## 1. SETUP


#### 1. Membuat lingkungan virtual dan menginstal django

        λ python -m venv venv312503 --promp francis-new
        λ venv312503\Scripts\activate.bat
        (francis-new) λ pip install django==5.0.3
        (francis-new) λ python.exe -m pip install --upgrade pip



## 2. PROYEK DAN APLIKASI


#### 1. Membuat proyek

        (francis-new) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. Menjalankan developmen server

        (francis-new) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        July 04, 2024 - 07:53:33
        Django version 5.0.3, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        Note:

        Saat kali pertama menjalankan developmen server, maka django
        akan menghasilkan secara default db.sqlite3.


#### 3. Membuat aplikasi shop

        (francis-new) λ mkdir app\shop
        (francis-new) λ django-admin startapp shop app\shop

        modified:   README.md
        new file:   app/shop/__init__.py
        new file:   app/shop/admin.py
        new file:   app/shop/apps.py
        new file:   app/shop/migrations/__init__.py
        new file:   app/shop/models.py
        new file:   app/shop/tests.py
        new file:   app/shop/views.py


#### 4. Mendaftarkan aplikasi shop pada app/shop/admin.py

        modified:   README.md
        modified:   app/shop/apps.py
        modified:   config/settings.py



## 3. STRUKTUR PROYEK
