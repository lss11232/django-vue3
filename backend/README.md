cd apps
python ../manage.py startapp user

#创建表
python manage.py makemigrations
python manage.py migrate

# 启动
python manage.py runserver

# 初始化数据
python manage.py  init



# rbac 数据库
python manage.py makemigrations rbac
python manage.py migrate  rbac

python manage.py runserver 0.0.0.0:8888