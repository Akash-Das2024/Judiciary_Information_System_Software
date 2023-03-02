# JISS

-   a web-based application using Django aim to provide the members of the attorney's office manage court cases.
-   the application helps the registrar create, delete, and manage court cases and updates after each hearing.
-   Judges and Lawyers can search for old court cases for any of their references.

### Users:

-   Registers
-   Judges
-   Lawyers

### Install Django:

```
pip install django
```

### Usage:

-   run

```
python manage.py runserver <port(opt)>
```

-   migrate

```
python manage.py makemigrations
python manage.py migrate
```

### Django Basic Commands to look for:

-   Development server:

```
python manage.py runserver
```

-   Database management:

```
python manage.pydbshell
python manage.py inspectdb
python manage.py loaddata
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

-   Content management:

```
python manage.py createcachetable
python manage.py flush
python manage.py sendtestemail
python manage.py startapp
python manage.py startproject
```

-   Test management:

```
python manage.py test
python manage.py testserver
python manage.py Utility
```
