# Z-TECH
- project/urls.py -> app/urls.py -> views.py -> models.py -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py : 입력 사이트
- 개발 순서 : models.py, views.py, urls.py, templates

1. startproject ZTech
   1. python -m pip install django~=3.2
   2. django-admin startproject ZTech .
   3. python manage.py runserver
2. startapp tech
   1. python manage.py startapp tech
   2. add 'tech', to INSTALLED_APPS in settings.py
3. tech/models Tech
   1. python manage.py makemigrations tech
      1. models -> DB로 옮기기 위한 py
   2. python manage.py migrate
      1. DB 테이블 만들기