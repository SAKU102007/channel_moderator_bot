# Telegram Bot: Channel Moderator

Проект для модерации и управления контентом в Telegram-каналах с использованием библиотеки **aiogram**.

В проекте реализована админ-панель, система ролей, пошаговое создание и редактирование постов через машину состояний (FSM), а также антиспам-система.

> [!IMPORTANT]
> Проект разработан с использованием **Python 3.10** и библиотеки **aiogram 2.25.1**.
>
> **Python 3.13 и новее не поддерживаются**, так как `aiogram 2.25.1` несовместим с этими версиями Python.

---

## 📌 Возможности

Бот поддерживает следующие функции:

- доступ ко всему функционалу через единую команду `/start`;
- пошаговое создание, редактирование и удаление постов через FSM;
- предпросмотр и публикация готовых постов в подключенный канал;
- система ролей:
  - **Администратор**: имеет полный доступ, включая назначение и удаление ролей пользователей.
  - **Контент-менеджер**: имеет доступ к созданию, редактированию и публикации постов;
- работа с базой данных PostgreSQL для надежного хранения данных и профилей;
- защита от спама с помощью встроенного middleware (троттлинг).

---

## 🛠 Используемые технологии

- Python 3.10
- aiogram 2.25.1
- asyncpg
- python-dotenv
- PostgreSQL

---

# Структура проекта

```text
channel_moderator_bot/
│
├── main.py                                         # Основной файл запуска бота
├── .env                                            # Файл с настройками (создается самостоятельно)
│
├── config/                                         # Настройки и загрузка переменных окружения
│   └── bot_config.py
├── db_handler/                                     # Работа с БД PostgreSQL (посты, роли пользователей)
│   ├── change_post
│   │   ├── change_post.py
│   │   └── get_post_name.py
│   ├── create_post
│   │   ├── check_user_name.py
│   │   └── create_post.py
│   ├── delete_post
│   │   └── delete_post.py
│   ├── get_post
│   │   └── get_post.py
│   └── user_role
│       ├── check_user_role.py
│       ├── create_admin.py
│       ├── create_content_manager.py
│       └── delete_user_role.py
├── handlers/                                       # Обработчики (админ-панель, FSM для создания постов)
│   ├── admin_panel
│   │   ├── change_post
│   │   │   ├── get_post.py
│   │   │   └── states_change_post
│   │   │       ├── post_description.py
│   │   │       ├── post_id.py
│   │   │       ├── post_image.py
│   │   │       ├── post_name.py
│   │   │       └── post_tag.py
│   │   ├── check_post
│   │   │   ├── check_post.py
│   │   │   └── states_check_post
│   │   │       └── post_id.py
│   │   ├── create_post
│   │   │   ├── create_post.py
│   │   │   └── states_post
│   │   │       ├── post_description.py
│   │   │       ├── post_image.py
│   │   │       ├── post_name.py
│   │   │       └── post_tag.py
│   │   ├── create_user_role
│   │   │   ├── admin
│   │   │   │   └── admin.py
│   │   │   ├── content_manager
│   │   │   │   └── content_manager.py
│   │   │   └── create_user_role.py
│   │   ├── delete_post
│   │   │   ├── delete_post.py
│   │   │   └── states_delete_post
│   │   │       └── post_id.py
│   │   ├── delete_user_role
│   │   │   └── delete_user_role.py
│   │   ├── main_menu.py
│   │   └── publish_post
│   │       ├── publish_post.py
│   │       └── states_publish_post
│   │           └── post_id.py
│   └── start
│       └── start.py
 keyboards/                                         # Файлы для создания Reply и Inline клавиатур
│   ├── admin_panel_keyboard_back_to_main_menu.py
│   ├── admin_panel_keyboard_main_menu.py
│   ├── admin_panel_keyboard_take_user_role.py
│   └── content_manager_keyboard_main_menu.py
└── middlewares/                                    # Middleware (в т.ч. система троттлинга)
│   └── trottling
│       ├── rate_limit
│       │   └── rate_limit.py
│       └── trottling.py
└── pip_requirements.txt                            # Список зависимостей
```

---

## 📄 Описание основных модулей

| Модуль / Папка | Назначение |
|------|------------|
| **`main.py`** | **Основной файл** – точка входа. Запускайте именно его для работы бота. |
| `config/` | Загрузка конфигурации из `.env` (токен бота, реквизиты базы данных). |
| `db_handler/` | Скрипты взаимодействия с PostgreSQL (создание, удаление постов, проверка прав и управление ролями `admin` / `content_manager`). |
| `handlers/admin_panel/` | Основная логика: главное меню, FSM-сценарии создания, проверки, редактирования, удаления и публикации постов в канал, управление правами доступа. |
| `handlers/start/` | Обработка базовой команды `/start` и маршрутизация пользователя в зависимости от его роли. |
| `keyboards/` | Модули генерации Reply и Inline клавиатур для навигации. |
| `middlewares/trottling/` | Защита от спама (rate limit), ограничивающая частоту запросов от одного пользователя. |

---

# Требования

Необходимо установить:

- Python **3.10**
- pip
- PostgreSQL (сервер базы данных)

Проверить можно командами:

```bash
python3.10 --version
python3.10 -m pip --version
```

Ожидаемый результат:

```text
Python 3.10.x
pip <version> from <path> (python 3.10)
```

Если у вас установлена версия Python **3.13** или новее, необходимо установить **Python 3.10**, поскольку библиотека **aiogram 2.25.1** не поддерживает более новые версии Python.

---

# Установка проекта

### 1. Клонировать репозиторий

```bash
git clone https://github.com/SAKU102007/channel_moderator_bot.git
```
или распакуйте архив проекта.

После этого перейти в папку проекта.

```bash
cd channel_moderator_bot
```

---

### 2. Создать виртуальное окружение (рекомендуется)

**Windows**

```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3.10 -m venv venv
source venv/bin/activate
```

---

### 3. Установить зависимости

Все необходимые библиотеки перечислены в файле `pip_requirements.txt`.

Установить их можно командой

```bash
pip install -r pip_requirements.txt
```

---

# Настройка Telegram API и канала

## Этап 1. Создание бота

### Шаг 1
Открыть Telegram и найти бота **@BotFather**. Это официальный бот Telegram для создания других ботов.

### Шаг 2
Отправить команду:
```
/newbot
```

### Шаг 3
Придумать имя будущего бота (например, `Channel Moderator Bot`).

### Шаг 4
Придумать username. Он обязательно должен заканчиваться на `bot` (например, `my_channel_mod_bot`).

### Шаг 5
После успешного создания BotFather отправит сообщение с токеном:
```
Use this token to access the HTTP API:
123456789:AAHXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
Скопируйте этот токен.

---

## Этап 2. Настройка Telegram-канала

### Шаг 1
Создайте новый публичный или частный канал в Telegram, куда будут публиковаться посты.

### Шаг 2
Перейдите в настройки канала -> **Администраторы** -> **Добавить администратора**.

### Шаг 3
Найдите вашего бота по username (`@my_channel_mod_bot`) и добавьте его в список администраторов канала.

### Шаг 4
Выдайте боту необходимые права. Для корректной работы требуются права на **Отправление сообщений** (Post Messages) и **Редактирование сообщений** (Edit Messages).

---

## Этап 3. Получение ID пользователя и канала

Для корректной работы бота и настройки файла `.env` вам понадобятся ваш личный ID (чтобы стать первым администратором) и ID вашего канала.

### Шаг 1
Откройте Telegram и найдите бота **@GetsMyIDBot** (или перейдите по ссылке).

### Шаг 2
Нажмите **Start** (или отправьте команду `/start`). Бот ответит сообщением, в котором будет указан ваш личный ID:
```text
Your user ID: 1234567890
Current chat ID: 1234567890
```
Скопируйте значение **Your user ID** — это ваш личный `ADMIN` ID.

### Шаг 3
Перейдите в ваш Telegram-канал, который вы создали на предыдущем этапе.
Отправьте любое тестовое сообщение в этот канал.

### Шаг 4
Перешлите это тестовое сообщение из вашего канала в диалог с ботом **@GetsMyIDBot**.

### Шаг 5
Бот пришлет ответное сообщение с информацией о пересланном сообщении:
```text
Your user ID: 1234567890
Current chat ID: 1234567890

Forwarded from chat: -1001234567890
```
Скопируйте значение **Forwarded from chat** (включая знак минуса) — это `CHAT_ID` вашего канала.

---

# Создание файла .env

В папке сonfig создайте файл .env

```
touch config/.env
open -e config/.env
```

В этот файл необходимо прописать токен вашего бота и данные для подключения к базе данных PostgreSQL.

Пример содержимого файла (в строках с комментариями вам надо заменить значения переменных на ранее созданные):

```env
# Настройки Telegram Бота
API_TOKEN='123456789:AAHXXXXXXXXXXXXXXXXXXXXXXXXXXXX'     # Токен от **@BotFather**
ADMIN='12345678'     # Значение от **@GetsMyIDBot**
CHAT_ID='-12345678'     # Значение от **@GetsMyIDBot**

# Настройки подключения к PostgreSQL
HOST=localhost
USER=postgres
PASSWORD=12345678     # Пароль, который вы ввели в pgAdmin 4
DATABASE=bot_db
```

---

# Запуск проекта

После выполнения всех предыдущих шагов запустите

```bash
python main.py
```

Если всё настроено правильно, бот начнет работать и успешно подключится к PostgreSQL.

---

# Команды бота

| Команда | Описание |
|----------|----------|
| `/start` | Запуск бота. Открывает админ-панель или меню контент-менеджера в зависимости от прав доступа пользователя. |

Всё остальное взаимодействие (создание постов, выдача ролей, публикация) реализовано через удобные Inline и Reply клавиатуры внутри бота.
