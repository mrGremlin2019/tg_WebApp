# Telegram WebApp

## Структура проекта
```
tg_WebApp/
├── bot/                 # Telegram-бот (Aiogram)
├── scripts/             # Скрипт для запуска бота
├── src/
│   ├── backend/         # Бэкенд (FastAPI)
│   ├── database/        # База данных (PostgreSQL + Tortoise ORM)
│   ├── frontend/        # Фронтенд (Vue 3, Pinia, TypeScript)
├── .env                 # Файл переменных окружения (не загружен в Git)
├── .gitignore           # Список файлов, игнорируемых Git
├── requirements.txt     # Список зависимостей для Python
├── package.json         # Список зависимостей для Node.js
├── tsconfig.json        # Конфигурация TypeScript
├── webpack.config.js    # Конфигурация Webpack
```

## Установка и запуск проекта

### 1. Установка зависимостей

Установка зависимостей:
```bash
pip install -r requirements.txt
```



### 2. Настройка базы данных PostgreSQL
Если PostgreSQL ещё не установлен, установите его. Затем создайте базу данных:
```bash
sudo -u postgres psql
```

### 3. Запуск бота
Запуск Telegram-бота:
```bash
python scripts/run_bot.py
```

### 4. Запуск бэкенда
Запуск FastAPI сервер с помощью Uvicorn:
```bash
cd src/backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Запуск фронтенда
Перейдите в папку `frontend` и запустите фронт с помощью npm:
```bash
cd src/frontend
npm start
```

### 6. Использование ngrok для внешнего доступа  
Если нужно протестировать веб-приложение или API из внешней сети, можно использовать `ngrok`:

1. Установите `ngrok`:
   ```bash
   npm install -g ngrok
   ```
2. Запустите `ngrok` для проброса локального сервера:
   ```bash
   ngrok http 8000
   ```
