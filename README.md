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


#### 1. Merubah struktur proyek

        modified:   README.md



## 4. URLS, VIEWS, TEMPLATES


#### 1. Membuat HALLO WORLD menggunakan HttpResponse: views dan urls

        modified:   README.md
        modified:   app/shop/urls.py
        deleted:    app/shop/views.py
        new file:   app/shop/views/__init__.py
        new file:   app/shop/views/shop_view.py
        modified:   config/urls.py

        :)


#### 2. Membuat laman home: urls, views, templates

        modified:   README.md
        new file:   app/shop/templates/shop/index.html
        modified:   app/shop/views/shop_view.py


#### 3. Mengaktifkan django templates

        modified:   README.md
        modified:   config/settings.py
        renamed:    app/shop/templates/shop/index.html -> templates/shop/index.html



## 5. TEMPLATING DAN STATIK FILE


#### 1. Mengisi HTML template pada laman home

        modified:   README.md
        modified:   templates/shop/index.html


#### 2. Membuat path dan loading statik file 

        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py
        modified:   templates/shop/index.html

        Note: 
        static file diabaikan oleh git(tidak disimpan dalam repositori)


#### 3. Membuat template inheritance dan partials

        modified:   README.md
        new file:   templates/base.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/header.html
        modified:   templates/shop/index.html



## 6. DATABASE


#### 1. Membuat mysql database

        λ mysql -u root
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 8
        Server version: 8.0.30 MySQL Community Server - GPL

        Copyright (c) 2000, 2022, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql> CREATE DATABASE 2024_dj5ecom_francis_new;
        Query OK, 1 row affected (0.14 sec)