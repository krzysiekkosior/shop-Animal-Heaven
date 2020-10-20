# Shop: Animal Heaven

Project contains online shop with items dedicated to animals.
Products can be searched directly from list of them or by search engine. 
Additionaly products are divided into categories and brands.

Page views are divided into two basic views: for Customer and for Admin. 
Additionally there is third view (for SuperUser) 
that is the same as Admin View, but can also allows to add Admins manually.

# Instructions:
1. Download project to your computer
2. Set the virtual enviroment and install required packages from *requirements.txt*
3. Create PostgreSQL database according to *DATABASES* in *shop.settings*
4. In directory with project use command:
    `python manage.py migrate`
5. To fulfil database with data use command: `python manage.py insert_data`
6. To create admin use command `python manage.py create_admin`
7. Run project, create account and buy something for your pet :)