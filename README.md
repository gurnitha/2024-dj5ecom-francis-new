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


#### 2. Menginstal mysql driver

        (francis-new) λ pip install mysqlclient


#### 3. Menghubungkan proyek dengan database

        modified:   README.md
        modified:   config/settings.py


#### 4. Melindungi sensitif file

        new file:   .env-example
        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py



## 7. AKTIVASI


#### 1. Mengaktifkan default app bawaan django

        (francis-new) λ python manage.py makemigrations
        No changes detected

        (francis-new) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK

        mysql> USE 2024_dj5ecom_francis_new;
        Database changed

        mysql> SHOW tables;
        +------------------------------------+
        | Tables_in_2024_dj5ecom_francis_new |
        +------------------------------------+
        | auth_group                         |
        | auth_group_permissions             |
        | auth_permission                    |
        | auth_user                          |
        | auth_user_groups                   |
        | auth_user_user_permissions         |
        | django_admin_log                   |
        | django_content_type                |
        | django_migrations                  |
        | django_session                     |
        +------------------------------------+
        10 rows in set (0.00 sec)

        mysql> DESC auth_user;
        +--------------+--------------+------+-----+---------+----------------+
        | Field        | Type         | Null | Key | Default | Extra          |
        +--------------+--------------+------+-----+---------+----------------+
        | id           | int          | NO   | PRI | NULL    | auto_increment |
        | password     | varchar(128) | NO   |     | NULL    |                |
        | last_login   | datetime(6)  | YES  |     | NULL    |                |
        | is_superuser | tinyint(1)   | NO   |     | NULL    |                |
        | username     | varchar(150) | NO   | UNI | NULL    |                |
        | first_name   | varchar(150) | NO   |     | NULL    |                |
        | last_name    | varchar(150) | NO   |     | NULL    |                |
        | email        | varchar(254) | NO   |     | NULL    |                |
        | is_staff     | tinyint(1)   | NO   |     | NULL    |                |
        | is_active    | tinyint(1)   | NO   |     | NULL    |                |
        | date_joined  | datetime(6)  | NO   |     | NULL    |                |
        +--------------+--------------+------+-----+---------+----------------+
        11 rows in set (0.00 sec)


#### 2. Membuat superuser

        (francis-new) λ python manage.py createsuperuser
        Username (leave blank to use 'ing'): superuser
        Email address: superuser@mail.com
        Password:
        Password (again):
        The password is too similar to the email address.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.



## 8. MODELS: SLIDERS DAN NEW COLLECTIONS


#### 1. Membuat model Slider

        modified:   README.md
        new file:   app/shop/models/Slider.py
        new file:   app/shop/models/__init__.py

        Note:

        Model dibuat sebagai modul.


#### 2. Membuat dan mengaplikasikan model Slider

        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0001_initial.py
            - Create model Slider

        (francis-new) λ python manage.py migrate shop 0001
        Operations to perform:
          Target specific migration: 0001_initial, from shop
        Running migrations:
          Applying shop.0001_initial... OK

        (francis-new) λ python manage.py sqlmigrate shop 0001
        --
        -- Create model Slider
        --
        CREATE TABLE `shop_slider` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `title` varchar(60) NOT NULL, 
                `description` varchar(120) NOT NULL, 
                `button_text` varchar(60) NOT NULL, 
                `button_link` varchar(255) NOT NULL, 
                `image` varchar(100) NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `created_at` datetime(6) NOT NULL
        );

        modified:   README.md
        new file:   app/shop/__models/Slider.py
        new file:   app/shop/__models/__init__.py
        new file:   app/shop/migrations/0001_initial.py
        deleted:    app/shop/models.py
        modified:   app/shop/models/Slider.py
        modified:   app/shop/models/__init__.py

        Note:

        Masalah:

        1. Dengan cara biasa migrasi gagal.

        Solusi:

        1. Buka file models/__init__.py dan isi code ini

        # app/shop/models/__init__.py

        # Impor Model from models 
        from app.shop.models.Slider import Slider

        :)


#### 3. Mendaftarkan model Slider pada shop/admin.py

        modified:   README.md
        modified:   app/shop/admin.py


#### 4. Login sebagai superuser untuk memeriksa hasil migrasi

        http://127.0.0.1:9000/admin/

        Note:

        Gunakan kredensial superuser untuk login.


#### 5. Membuat path untuk media file dan menginput sliders

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   media/sliders/2024/07/04/banner1.png
        new file:   media/sliders/2024/07/04/banner2.png
        new file:   media/sliders/2024/07/04/banner3.png
        new file:   media/sliders/2024/07/04/banner7.png

        Note:

        Slider masih ditampilkan sebagai slider object pada tabel.
        Sebiknya object diganti dengan title slider.


#### 6. Mendefinisikan tampilan Slider objects pada admin panel

        modified:   README.md
        modified:   app/shop/admin.py


#### 7. Load dan display sliders

        modified:   app/shop/views/shop_view.py
        new file:   templates/partials/slider.html
        modified:   templates/shop/index.html

        :)


#### 8. Membuat model Collection

        modified:   README.md
        new file:   app/shop/models/Collection.py
        modified:   app/shop/models/Slider.py

        Note:

        Model Slider hanya menambahkan lokasi file.


#### 9. Membuat dan mengaplikasikan model Collection

        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0002_collection.py
            - Create model Collection

        (francis-new) λ python manage.py migrate shop 0002
        Operations to perform:
          Target specific migration: 0002_collection, from shop
        Running migrations:
          Applying shop.0002_collection... OK

        (francis-new) λ python manage.py sqlmigrate shop 0002
        --
        -- Create model Collection
        --
        CREATE TABLE `shop_collection` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `title` varchar(60) NOT NULL, 
                `description` varchar(120) NOT NULL, 
                `button_text` varchar(60) NOT NULL, 
                `button_link` varchar(255) NOT NULL, 
                `image` varchar(100) NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `created_at` datetime(6) NOT NULL
        );

        mysql> DESC shop_collection;
        +-------------+--------------+------+-----+---------+----------------+
        | Field       | Type         | Null | Key | Default | Extra          |
        +-------------+--------------+------+-----+---------+----------------+
        | id          | bigint       | NO   | PRI | NULL    | auto_increment |
        | title       | varchar(60)  | NO   |     | NULL    |                |
        | description | varchar(120) | NO   |     | NULL    |                |
        | button_text | varchar(60)  | NO   |     | NULL    |                |
        | button_link | varchar(255) | NO   |     | NULL    |                |
        | image       | varchar(100) | NO   |     | NULL    |                |
        | updated_at  | datetime(6)  | NO   |     | NULL    |                |
        | created_at  | datetime(6)  | NO   |     | NULL    |                |
        +-------------+--------------+------+-----+---------+----------------+
        8 rows in set (0.01 sec)

        modified:   README.md
        new file:   app/shop/migrations/0002_collection.py
        modified:   app/shop/models/__init__.py


#### 10. Mendaftarkan model Collection pada shop/admin.py dan menginput collections

        modified:   README.md
        modified:   app/shop/admin.py
        new file:   media/sliders/2024/07/04/1.png
        new file:   media/sliders/2024/07/04/2.png


#### 11. Mendefinisikan tampilan Collection objects pada admin panel

        modified:   README.md
        modified:   app/shop/admin.py


#### 12. Load dan display Collections

        modified:   README.md
        modified:   app/shop/views/shop_view.py
        modified:   templates/shop/index.html

        :)



## 9. MODELS: EXCLUSIVE PRODUCTS


#### 1. Membuat model Category

        modified:   README.md
        new file:   app/shop/models/Category.py