# api_yamdb


### Описание: 
  REST API для проекта YaMDb. С этим интерфейсом могут взаимодействовать мобильные приложения, боты или другие сторонние ресурсы.  
  Проект YaMDb собирает отзывы и оценки пользователей на различные произведения. К отзывам можно оставлять комментарии. 


### Технологии в проекте:
  Python 3.9, Django 2.2.16, Django REST Framework (DRF).
  

### Последовательность команд при запуске:

#### Клонировать репозиторий и перейти в него в командной строке
git clone git@github.com:reztsovdimitrii/api_yamdb.git 
cd api_yamdb

#### Cоздать и активировать виртуальное окружение, обновить pip
python -m venv venv  
source venv/Scripts/./activate  
python -m pip install --upgrade pip  

#### Установить зависимости из файла requirements.txt
pip install -r requirements.txt

#### Выполнить миграции
python manage.py migrate

#### Запустить проект
python manage.py runserver

### Авторы:
    Дмитрий Резцов (Github - reztsovdimitrii)
    Лычагин Андрей (Github - Linnaip)
	Семёнов Сергей (Github - bluesprogrammer-Python)
