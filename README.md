# 2024-dj5ecom-francis-new
Membuat aplikasi ecommerce menggunakan Django versi 5.0.3
Github:https://github.com/gurnitha/2024-dj5ecom-francis-new
Local:E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new
Udemy:https://www.udemy.com/course/apprendre-django-a-par-la-creation-dun-site-e-commerce/learn/lecture/



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


#### 2. Membuat dan mengaplikasikan model Category

        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0003_category.py
            - Create model Category

        E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new\src(main -> origin)
        (francis-new) λ python manage.py migrate shop 0003
        Operations to perform:
          Target specific migration: 0003_category, from shop
        Running migrations:
          Applying shop.0003_category... OK

        E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new\src(main -> origin)
        (francis-new) λ python manage.py sqlmigrate shop 0003
        --
        -- Create model Category
        --
        CREATE TABLE `shop_category` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `name` varchar(60) NOT NULL, 
                `description` varchar(120) NOT NULL, 
                `slug` varchar(255) NOT NULL, 
                `image` varchar(100) NOT NULL, 
                `is_mega` bool NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `created_at` datetime(6) NOT NULL
        );
        CREATE INDEX `shop_category_slug_4508178e` ON `shop_category` (`slug`);

        mysql> DESC shop_category;
        +-------------+--------------+------+-----+---------+----------------+
        | Field       | Type         | Null | Key | Default | Extra          |
        +-------------+--------------+------+-----+---------+----------------+
        | id          | bigint       | NO   | PRI | NULL    | auto_increment |
        | name        | varchar(60)  | NO   |     | NULL    |                |
        | description | varchar(120) | NO   |     | NULL    |                |
        | slug        | varchar(255) | NO   | MUL | NULL    |                |
        | image       | varchar(100) | NO   |     | NULL    |                |
        | is_mega     | tinyint(1)   | NO   |     | NULL    |                |
        | updated_at  | datetime(6)  | NO   |     | NULL    |                |
        | created_at  | datetime(6)  | NO   |     | NULL    |                |
        +-------------+--------------+------+-----+---------+----------------+
        8 rows in set (0.00 sec)

        modified:   README.md
        modified:   app/shop/admin.py


#### 3. Mendaftarkan model Category pada shop/admin.py dan menginput categories

        modified:   README.md
        modified:   app/shop/admin.py
        new file:   media/categories/2024/07/04/1.webp


#### 4. Mendefinisikan tampilan Category objects pada admin panel

        modified:   README.md
        modified:   app/shop/admin.py
        new file:   media/categories/2024/07/04/3.webp
        new file:   media/categories/2024/07/04/5.webp


#### 5. Membuat model Image

        modified:   README.md
        new file:   app/shop/models/Image.py


#### 7. Membuat dan mengaplikasikan model Image

        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0004_image.py
            - Create model Image

        (francis-new) λ python manage.py migrate shop 0004
        Operations to perform:
          Target specific migration: 0004_image, from shop
        Running migrations:
          Applying shop.0004_image... OK

        (francis-new) λ python manage.py sqlmigrate shop 0004
        --
        -- Create model Image
        --
        CREATE TABLE `shop_image` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `image` varchar(100) NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `created_at` datetime(6) NOT NULL
        );

        mysql> DESC shop_image;
        +------------+--------------+------+-----+---------+----------------+
        | Field      | Type         | Null | Key | Default | Extra          |
        +------------+--------------+------+-----+---------+----------------+
        | id         | bigint       | NO   | PRI | NULL    | auto_increment |
        | image      | varchar(100) | NO   |     | NULL    |                |
        | updated_at | datetime(6)  | NO   |     | NULL    |                |
        | created_at | datetime(6)  | NO   |     | NULL    |                |
        +------------+--------------+------+-----+---------+----------------+
        4 rows in set (0.00 sec)


#### 8. Mendaftarkan dan mendefinisikan model Image pada shop/admin.py

        modified:   README.md
        modified:   app/shop/admin.py


#### 9. Membuat model Product

        modified:   README.md
        new file:   app/shop/models/Product.py


#### 10. Menambahkan hubungan ManyToMany antara model Category dengan model Product

        modified:   README.md
        modified:   app/shop/models/Product.py


#### 11. Menambahkan hubungan ManyToMany antara model Product dengan model Image

        modified:   README.md
        modified:   app/shop/models/Image.py


#### 12. Membuat dan mengaplikasikan migrasi pada model Product

        (francis-new) λ python manage.py makemigrations shop
        It is impossible to add a non-nullable field 'product' to image without specifying a default. This is because the database needs something to populate existing rows.
        Please select a fix:
         1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
         2) Quit and manually define a default value in models.py.
        Select an option: 1
        Please enter the default value as valid Python.
        The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
        Type 'exit' to exit this prompt
        >>> 1
        Migrations for 'shop':
          app\shop\migrations\0005_product_image_product.py
            - Create model Product
            - Add field product to image

        (francis-new) λ python manage.py migrate shop 0005
        Operations to perform:
          Target specific migration: 0005_product_image_product, from shop
        Running migrations:
          Applying shop.0005_product_image_product... OK

        (francis-new) λ python manage.py sqlmigrate shop 0005
        --
        -- Create model Product
        --
        CREATE TABLE `shop_product` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(60) NOT NULL, `slug` varchar(255) NOT NULL, `description` varchar(120) NOT NULL, `more_description` longtext NULL, `additional_infos` longtext NULL, `stock` integer NOT NULL, `sold_price` double precision NOT NULL, `regular_price` double precision NOT NULL, `brand` varchar(60) NULL, `is_available` bool NOT NULL, `is_best_seller` bool NOT NULL, `is_new_arrival` bool NOT NULL, `is_featured` bool NOT NULL, `is_special_offer` bool NOT NULL, `updated_at` datetime(6) NOT NULL, `created_at` datetime(6) NOT NULL);
        CREATE TABLE `shop_product_categories` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `product_id` bigint NOT NULL, `category_id` bigint NOT NULL);
        --
        -- Add field product to image
        --
        ALTER TABLE `shop_image` ADD COLUMN `product_id` bigint DEFAULT 1 NOT NULL , ADD CONSTRAINT `shop_image_product_id_1cb0873d_fk_shop_product_id` FOREIGN KEY (`product_id`) REFERENCES `shop_product`(`id`);
        ALTER TABLE `shop_image` ALTER COLUMN `product_id` DROP DEFAULT;
        CREATE INDEX `shop_product_slug_30bd2d5d` ON `shop_product` (`slug`);
        ALTER TABLE `shop_product_categories` ADD CONSTRAINT `shop_product_categories_product_id_category_id_edca6f84_uniq` UNIQUE (`product_id`, `category_id`);
        ALTER TABLE `shop_product_categories` ADD CONSTRAINT `shop_product_categories_product_id_59c38762_fk_shop_product_id` FOREIGN KEY (`product_id`) REFERENCES `shop_product` (`id`);
        ALTER TABLE `shop_product_categories` ADD CONSTRAINT `shop_product_categories_category_id_7b004fe8_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`);

        mysql> DESC shop_image;
        +------------+--------------+------+-----+---------+----------------+
        | Field      | Type         | Null | Key | Default | Extra          |
        +------------+--------------+------+-----+---------+----------------+
        | id         | bigint       | NO   | PRI | NULL    | auto_increment |
        | image      | varchar(100) | NO   |     | NULL    |                |
        | updated_at | datetime(6)  | NO   |     | NULL    |                |
        | created_at | datetime(6)  | NO   |     | NULL    |                |
        | product_id | bigint       | NO   | MUL | NULL    |                |
        +------------+--------------+------+-----+---------+----------------+
        5 rows in set (0.00 sec)

        mysql> DESC shop_product_categories;
        +-------------+--------+------+-----+---------+----------------+
        | Field       | Type   | Null | Key | Default | Extra          |
        +-------------+--------+------+-----+---------+----------------+
        | id          | bigint | NO   | PRI | NULL    | auto_increment |
        | product_id  | bigint | NO   | MUL | NULL    |                |
        | category_id | bigint | NO   | MUL | NULL    |                |
        +-------------+--------+------+-----+---------+----------------+
        3 rows in set (0.00 sec)

        mysql> DESC shop_product;
        +------------------+--------------+------+-----+---------+----------------+
        | Field            | Type         | Null | Key | Default | Extra          |
        +------------------+--------------+------+-----+---------+----------------+
        | id               | bigint       | NO   | PRI | NULL    | auto_increment |
        | name             | varchar(60)  | NO   |     | NULL    |                |
        | slug             | varchar(255) | NO   | MUL | NULL    |                |
        | description      | varchar(120) | NO   |     | NULL    |                |
        | more_description | longtext     | YES  |     | NULL    |                |
        | additional_infos | longtext     | YES  |     | NULL    |                |
        | stock            | int          | NO   |     | NULL    |                |
        | sold_price       | double       | NO   |     | NULL    |                |
        | regular_price    | double       | NO   |     | NULL    |                |
        | brand            | varchar(60)  | YES  |     | NULL    |                |
        | is_available     | tinyint(1)   | NO   |     | NULL    |                |
        | is_best_seller   | tinyint(1)   | NO   |     | NULL    |                |
        | is_new_arrival   | tinyint(1)   | NO   |     | NULL    |                |
        | is_featured      | tinyint(1)   | NO   |     | NULL    |                |
        | is_special_offer | tinyint(1)   | NO   |     | NULL    |                |
        | updated_at       | datetime(6)  | NO   |     | NULL    |                |
        | created_at       | datetime(6)  | NO   |     | NULL    |                |
        +------------------+--------------+------+-----+---------+----------------+
        17 rows in set (0.00 sec)

        modified:   README.md
        new file:   app/shop/migrations/0005_product_image_product.py
        modified:   app/shop/models/__init__.py


#### 13. Mendaftarkan dan mendefinisikan model Product pada shop/admin.py

        modified:   README.md
        modified:   app/shop/admin.py


#### 14. Insert products

        modified:   README.md
        new file:   media/categories/2024/07/04/2.webp
        new file:   media/categories/2024/07/04/4.webp
        new file:   media/products/2024/07/04/1.webp
        new file:   media/products/2024/07/04/10.webp
        new file:   media/products/2024/07/04/11.webp
        new file:   media/products/2024/07/04/12.webp
        new file:   media/products/2024/07/04/13.webp
        new file:   media/products/2024/07/04/14.webp
        new file:   media/products/2024/07/04/14_3OOdjZs.webp
        new file:   media/products/2024/07/04/15.webp
        new file:   media/products/2024/07/04/15_JgoUOl4.webp
        new file:   media/products/2024/07/04/16.webp
        new file:   media/products/2024/07/04/17.webp
        new file:   media/products/2024/07/04/2.webp
        new file:   media/products/2024/07/04/20.webp
        new file:   media/products/2024/07/04/21.webp
        new file:   media/products/2024/07/04/22.webp
        new file:   media/products/2024/07/04/23.webp
        new file:   media/products/2024/07/04/24.webp
        new file:   media/products/2024/07/04/25.webp
        new file:   media/products/2024/07/04/26.webp
        new file:   media/products/2024/07/04/27.webp
        new file:   media/products/2024/07/04/28.webp
        new file:   media/products/2024/07/04/3.webp
        new file:   media/products/2024/07/04/30.webp
        new file:   media/products/2024/07/04/31.webp
        new file:   media/products/2024/07/04/32.webp
        new file:   media/products/2024/07/04/32_yvJcKFu.webp
        new file:   media/products/2024/07/04/33.webp
        new file:   media/products/2024/07/04/34.webp
        new file:   media/products/2024/07/04/5.webp
        new file:   media/products/2024/07/04/6.webp
        new file:   media/products/2024/07/04/7.webp
        new file:   media/products/2024/07/04/8.webp
        new file:   media/products/2024/07/04/9.webp


#### 15. Load dan display products

        modified:   README.md
        modified:   app/shop/views/shop_view.py
        modified:   templates/shop/index.html


#### 16. Membuat partials template untuk product

        modified:   README.md
        new file:   templates/partials/product.html
        modified:   templates/shop/index.html



## 10. PENGELOLAAN INFORMASI SITUS


#### 1. Membuat model Setting

        modified:   README.md
        new file:   app/shop/models/Setting.py


#### 2. Membuat dan mengaplikasikan migrasi untuk model Setting

        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0006_setting.py
            - Create model Setting

        E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new\src(main -> origin)
        (francis-new) λ python manage.py migrate shop 0006
        Operations to perform:
          Target specific migration: 0006_setting, from shop
        Running migrations:
          Applying shop.0006_setting... OK

        E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new\src(main -> origin)
        (francis-new) λ python manage.py sqlmigrate shop 0006
        --
        -- Create model Setting
        --
        CREATE TABLE `shop_setting` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `name` varchar(60) NOT NULL, 
                `description` varchar(255) NOT NULL, 
                `currency` varchar(4) NOT NULL, 
                `taxe_rate` double precision NOT NULL, 
                `logo` varchar(100) NOT NULL, 
                `street` varchar(60) NOT NULL, 
                `city` varchar(255) NOT NULL, 
                `code_postal` varchar(60) NOT NULL, 
                `state` varchar(255) NOT NULL, 
                `phone` varchar(100) NOT NULL, 
                `email` varchar(254) NOT NULL, 
                `copyright` varchar(255) NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `created_at` datetime(6) NOT NULL
        );

        mysql> DESC shop_setting;
        +-------------+--------------+------+-----+---------+----------------+
        | Field       | Type         | Null | Key | Default | Extra          |
        +-------------+--------------+------+-----+---------+----------------+
        | id          | bigint       | NO   | PRI | NULL    | auto_increment |
        | name        | varchar(60)  | NO   |     | NULL    |                |
        | description | varchar(255) | NO   |     | NULL    |                |
        | currency    | varchar(4)   | NO   |     | NULL    |                |
        | taxe_rate   | double       | NO   |     | NULL    |                |
        | logo        | varchar(100) | NO   |     | NULL    |                |
        | street      | varchar(60)  | NO   |     | NULL    |                |
        | city        | varchar(255) | NO   |     | NULL    |                |
        | code_postal | varchar(60)  | NO   |     | NULL    |                |
        | state       | varchar(255) | NO   |     | NULL    |                |
        | phone       | varchar(100) | NO   |     | NULL    |                |
        | email       | varchar(254) | NO   |     | NULL    |                |
        | copyright   | varchar(255) | NO   |     | NULL    |                |
        | updated_at  | datetime(6)  | NO   |     | NULL    |                |
        | created_at  | datetime(6)  | NO   |     | NULL    |                |
        +-------------+--------------+------+-----+---------+----------------+
        15 rows in set (0.01 sec)

        modified:   README.md
        new file:   app/shop/migrations/0006_setting.py
        modified:   app/shop/models/__init__.py


#### 3. Mendaftarkan model Setting pada shop/admin.py

        modified:   README.md
        modified:   app/shop/admin.py


#### 4. Membuat context_processors.py dan insert info site

        modified:   README.md
        new file:   app/shop/context_processors.py
        modified:   config/settings.py
        new file:   media/settings/logo-38.PNG


#### 5. Load dan display info site

        modified:   README.md
        modified:   app/shop/context_processors.py
        modified:   templates/partials/footer.html
        modified:   templates/partials/header.html


#### 6. Membuat model Social

        modified:   README.md
        new file:   app/shop/models/Social.py


#### 7. Membuat dan mengaplikasikan migrasi untuk model Social

        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0007_social.py
            - Create model Social

        (francis-new) λ python manage.py migrate shop 0007
        Operations to perform:
          Target specific migration: 0007_social, from shop
        Running migrations:
          Applying shop.0007_social... OK

        (francis-new) λ python manage.py sqlmigrate shop 0007
        --
        -- Create model Social
        --
        CREATE TABLE `shop_social` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `name` varchar(60) NOT NULL, 
                `icon` varchar(120) NOT NULL, 
                `link` varchar(255) NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `created_at` datetime(6) NOT NULL
        );

        mysql> DESC shop_social;
        +------------+--------------+------+-----+---------+----------------+
        | Field      | Type         | Null | Key | Default | Extra          |
        +------------+--------------+------+-----+---------+----------------+
        | id         | bigint       | NO   | PRI | NULL    | auto_increment |
        | name       | varchar(60)  | NO   |     | NULL    |                |
        | icon       | varchar(120) | NO   |     | NULL    |                |
        | link       | varchar(255) | NO   |     | NULL    |                |
        | updated_at | datetime(6)  | NO   |     | NULL    |                |
        | created_at | datetime(6)  | NO   |     | NULL    |                |
        +------------+--------------+------+-----+---------+----------------+
        6 rows in set (0.00 sec)

        modified:   README.md
        new file:   app/shop/migrations/0007_social.py
        modified:   app/shop/models/__init__.py


#### 8. Mendaftarkan model Social pada shop/admin.py, load dan diplay Social

        modified:   README.md
        modified:   app/shop/admin.py
        modified:   app/shop/context_processors.py
        modified:   templates/partials/footer.html



## 11. PENGELOLAAN LAMAN SITUS


#### 1. Membuat model Page

        modified:   README.md
        new file:   app/shop/models/Page.py


#### 2. Membuat dan mengaplikasikan migrasi untuk model Page

        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0008_page.py
            - Create model Page

        (francis-new) λ python manage.py migrate shop 0008
        Operations to perform:
          Target specific migration: 0008_page, from shop
        Running migrations:
          Applying shop.0008_page... OK

        (francis-new) λ python manage.py sqlmigrate shop 0008
        --
        -- Create model Page
        --
        CREATE TABLE `shop_page` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `name` varchar(255) NOT NULL, 
                `slug` varchar(50) NOT NULL, 
                `content` longtext NOT NULL, 
                `is_head` bool NOT NULL, 
                `is_foot` bool NOT NULL, 
                `is_checkout` bool NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `created_at` datetime(6) NOT NULL
        );
        CREATE INDEX `shop_page_slug_76a841a4` ON `shop_page` (`slug`);

        mysql> DESC shop_page;
        +-------------+--------------+------+-----+---------+----------------+
        | Field       | Type         | Null | Key | Default | Extra          |
        +-------------+--------------+------+-----+---------+----------------+
        | id          | bigint       | NO   | PRI | NULL    | auto_increment |
        | name        | varchar(255) | NO   |     | NULL    |                |
        | slug        | varchar(50)  | NO   | MUL | NULL    |                |
        | content     | longtext     | NO   |     | NULL    |                |
        | is_head     | tinyint(1)   | NO   |     | NULL    |                |
        | is_foot     | tinyint(1)   | NO   |     | NULL    |                |
        | is_checkout | tinyint(1)   | NO   |     | NULL    |                |
        | updated_at  | datetime(6)  | NO   |     | NULL    |                |
        | created_at  | datetime(6)  | NO   |     | NULL    |                |
        +-------------+--------------+------+-----+---------+----------------+
        9 rows in set (0.01 sec)

        modified:   README.md
        new file:   app/shop/migrations/0008_page.py
        modified:   app/shop/models/__init__.py

        NOTE: No migrations to apply.

        Aktivitas:

        1. Menghapus file migrasi
        2. Menghapus tabel

        Hasil:

        1. Tabel terhapus
        2. Membuat model baru (Page)
        3. Menjalankan migrasi dengan hasil: No migrations to apply.

        Solusi:

        (francis-new) λ python manage.py makemigrations --empty shop
        Migrations for 'shop':
          app\shop\migrations\0008_auto_20240705_0905.py

        E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new\src(main -> origin)
        (francis-new) λ python manage.py migrate shop 0008
        Operations to perform:
          Target specific migration: 0008_auto_20240705_0905, from shop
        Running migrations:
          Applying shop.0008_auto_20240705_0905... OK

        E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new\src(main -> origin)
        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0009_page.py
            - Create model Page

        E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new\src(main -> origin)
        (francis-new) λ python manage.py migrate shop 0008
        Operations to perform:
          Target specific migration: 0008_auto_20240705_0905, from shop
        Running migrations:
          No migrations to apply.

        E:\_WORKSPACE\2024\ex_desktop\2024-DEVSPACE\2024-dj5ecom-francis-new\src(main -> origin)
        (francis-new) λ python manage.py migrate shop 0009
        Operations to perform:
          Target specific migration: 0009_page, from shop
        Running migrations:
          Applying shop.0009_page... OK

        modified:   README.md
        modified:   app/shop/admin.py
        new file:   app/shop/migrations/0008_auto_20240705_0905.py
        new file:   app/shop/migrations/0009_page.py
        modified:   app/shop/models/__init__.py


#### 3. Mendaftarkan dan mendefinisikan model Page pada shop/admin.py 

        modified:   README.md
        modified:   app/shop/admin.py


#### 4. Membuat laman: About, Contact, Legal, Partner, Services

        modified:   README.m

        Note:

        Semua laman itu dibuat melalui admin panel.


#### 5. Menambahkan logik untuk model Page pada context_processors

        modified:   README.md
        modified:   app/shop/context_processors.py


#### 6. Load dan display object Page pada menu pages

        modified:   README.md
        modified:   templates/partials/header.html

        :)


#### 7. Menampilkan halaman part 1: basics 

        modified:   README.md
        modified:   app/shop/urls.py
        modified:   app/shop/views/shop_view.py
        modified:   templates/partials/header.html
        new file:   templates/shop/page.html

        Note: Berhasil menampilkan halaman 

        :)


#### 7. Menampilkan halaman part 2: styling 

        new file:   templates/partials/top_page.html
        modified:   templates/shop/page.html


#### 8. Menginstal django-ckeditor

        (francis-new) λ pip install django-ckeditor==6.7.0

        modified:   .gitignore
        modified:   README.md
        modified:   app/shop/admin.py
        modified:   config/settings.py

        NOTE:

        1. Menginstal django-ckeditor
        2. Memodifikasi konten menggunakan ckeditor

        :)


#### 9. Menampilkan halaman pada footer

        modified:   README.md
        modified:   templates/partials/footer.html

        NOTE:

        Laman baru: About, Contact, Legal, Partner, Services
        berhsil dibuat dan dinamis.

        :)



## 12. PENGELOLAAN MEGA MENU


#### 1. Memodifikasi (re-sizing) Category objects display pada admim panel

        modified:   README.md
        modified:   app/shop/admin.py


#### 2. Display products by category in the header part 1: membuat context_processors

        modified:   README.md
        modified:   app/shop/context_processors.py


#### 3. Display products by category in the header part 2: testing mega_categories pada header

        modified:   README.md
        modified:   templates/partials/header.html


#### 4. Display products by category in the header part 3: show product item pada header

        modified:   README.md
        modified:   templates/partials/header.html


#### 5. Menampilkan koleksi mega menu part 1: membuat model NavCollection

        modified:   README.md
        new file:   app/shop/models/NavCollection.py


#### 6. Menampilkan koleksi mega menu part 2: membuat dan mengaplikasikan migrasi

        (francis-new) λ python manage.py makemigrations shop
        Migrations for 'shop':
          app\shop\migrations\0010_navcollection.py
            - Create model NavCollection

        (francis-new) λ python manage.py migrate shop 0010
        Operations to perform:
          Target specific migration: 0010_navcollection, from shop
        Running migrations:
          Applying shop.0010_navcollection... OK

        (francis-new) λ python manage.py sqlmigrate shop 0010
        --
        -- Create model NavCollection
        --
        CREATE TABLE `shop_navcollection` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `title` varchar(60) NOT NULL, 
                `description` varchar(120) NOT NULL, 
                `button_text` varchar(60) NOT NULL, 
                `button_link` varchar(255) NOT NULL, 
                `image` varchar(100) NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `created_at` datetime(6) NOT NULL
        );

        mysql> DESC shop_navcollection;
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
        8 rows in set (0.00 sec)

        modified:   README.md
        new file:   app/shop/migrations/0010_navcollection.py


#### 7. Mendaftarkan dan mendefinisikan model NavColletion pada shop/admin.py 

        modified:   README.md
        modified:   app/shop/admin.py
        modified:   app/shop/models/NavCollection.py
        modified:   app/shop/models/__init__.py (lupa mendaftarkan model NavCollection di sini)        new file:   media/new_collections/2024/07/05/coll_1.png
        new file:   media/new_collections/2024/07/05/coll_1_SaSAKTO.png
        new file:   media/new_collections/2024/07/05/coll_1_Y30elgj.png
        new file:   media/new_collections/2024/07/05/coll_2.png
        new file:   media/new_collections/2024/07/05/coll_3.png
        new file:   media/new_collections/2024/07/05/coll_4.png
        modified:   app/shop/admin.py


#### 8. Membuat context_processors untuk NavCollection

        modified:   README.md
        modified:   app/shop/context_processors.py


#### 9. Menampilkan mega collections banner pada header

        modified:   README.md
        modified:   templates/partials/header.html

        :)


#### 10. Menampilkan field deskripsi pada mega collections banner pada header

        modified:   README.md
        modified:   app/shop/context_processors.py



## 13. PENGELOLAAN PRODUK


#### 1. Format harga dengan filter khusus

        modified:   README.md
        new file:   app/shop/templatetags/price_filter.py
        modified:   templates/partials/product.html


#### 2. Format harga prosentase pengurangan

        modified:   README.md
        # Mendefinisikan simbul harga dan prosentase diskon
        modified:   app/shop/templatetags/price_filter.py
        # Mengaplikasikan hal di atas
        modified:   templates/partials/product.html


#### 3. Menampilkan halaman single product

        modified:   README.md
        # modifikasi dan buat path baru
        modified:   app/shop/urls.py
        # membuat fungsing single_product
        modified:   app/shop/views/shop_view.py
        # menambahkan link
        modified:   templates/partials/product.html
        # template
        new file:   templates/shop/single_product.html


#### 4. Mengisi HTML tempate pada laman single_product

        modified:   README.md
        modified:   templates/shop/single_product.html


#### 5. Menampilkan halaman single product

        modified:   README.md
        modified:   templates/shop/single_product.html

        Note:

        1. Tampilan belum sempurna.
        2. Galeri gambar kecil belum dinamis.

        Next: 

        Menampilkan galeri gambar kecil