# Cash Flow Tracker

## Запуск приложения

Для запуска приложения Вам необходимо установить [Python 3.11 или позднее](https://www.python.org/downloads/) и [Git](https://git-scm.com/downloads).

#### Склонируйте репозиторий приложения

```bash
git clone https://github.com/soderrs/cash_flow_tracker.git
```

#### Создайте и активируйте виртуальное окружение

```bash
cd cash_flow_tracker
python3 -m venv .venv

# Linux/Mac OS
source .venv/bin/activate

# Windows
.venv/Scripts/activate.bat
```

#### Установите необходимые зависимости

```bash
pip install -r requirements/prod.txt
```

#### Задайте необходимые переменные окружения, либо воспользуйтесь шаблоном

```bash
cp .env.example .env
```

#### Примените миграции для БД и загрузите стандартные данные

```bash
python3 manage.py migrate
python3 manage.py loaddata fixtures/core/setup.json
```

#### Для доступа в админку Django нужно создать нового пользователя

```bash
python3 manage.py createsuperuser
# Введите необходимые данные для создания пользователя
# ...
```

#### Запуск проекта

```bash
python3 manage.py runserver
```

#### Перейдите по адресу <http://127.0.0.1:8000/admin> (или по адресу своего хоста)
