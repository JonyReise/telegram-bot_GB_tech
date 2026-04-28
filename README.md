# 🤖 Telegram Bot (aiogram 3.x)

Шаблон Telegram бота с командами, Reply и Inline меню. Готов к деплою на Render.

---

## 📁 Структура проекта

```
tgbot/
├── bot.py            # Основной файл бота
├── requirements.txt  # Зависимости
├── render.yaml       # Конфиг для Render
└── README.md
```

---

## 🚀 Быстрый старт (локально)

### 1. Создай бота в Telegram
- Открой [@BotFather](https://t.me/BotFather)
- Отправь `/newbot` и следуй инструкциям
- Скопируй полученный `BOT_TOKEN`

### 2. Установи зависимости

```bash
pip install -r requirements.txt
```

### 3. Задай токен

**Linux/Mac:**
```bash
export BOT_TOKEN="твой_токен_здесь"
```

**Windows (PowerShell):**
```powershell
$env:BOT_TOKEN = "твой_токен_здесь"
```

### 4. Запусти бота

```bash
python bot.py
```

---

## ☁️ Деплой на Render

### Шаг 1 — Залей код на GitHub
```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/ВАШ_НИК/ВАШ_РЕП.git
git push -u origin main
```

### Шаг 2 — Создай сервис на Render
1. Зайди на [render.com](https://render.com) и зарегистрируйся
2. Нажми **New → Blueprint** (если используешь render.yaml) **или New → Background Worker**
3. Подключи свой GitHub репозиторий
4. Render автоматически определит настройки из `render.yaml`

### Шаг 3 — Добавь переменную окружения
В разделе **Environment** добавь:
| Key | Value |
|-----|-------|
| `BOT_TOKEN` | `твой_токен_от_BotFather` |

### Шаг 4 — Deploy!
Нажми **Create Worker** — Render установит зависимости и запустит бота.

> ⚠️ **Важно:** Используй тип сервиса **Worker** (не Web Service), так как бот работает через long polling, а не HTTP.

---

## ✨ Функциональность

| Команда / Кнопка | Описание |
|-----------------|----------|
| `/start` | Приветствие + Reply-клавиатура |
| `/menu` или 📋 Меню | Inline-меню с разделами |
| `/help` | Список команд |
| `/about` | Информация о боте |
| ⚙️ Настройки | Раздел настроек |
| 📞 Контакты | Контактная информация |

---

## 🛠️ Как расширить бота

Добавь новый обработчик в `bot.py`:

```python
@dp.message(Command("mycommand"))
async def my_handler(message: Message):
    await message.answer("Привет из нового обработчика!")
```

Добавь команду в `set_commands()`:

```python
BotCommand(command="mycommand", description="Моя команда"),
```

---

## 📦 Зависимости

- `aiogram==3.7.0` — асинхронный фреймворк для Telegram Bot API
