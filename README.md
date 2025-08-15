# mcp_server_for_kaiten
MCP‑сервер для Kaiten

---
## Основные возможности
- Управление пространствами (CRUD)
- Управление досками (CRUD, удаление с параметром force)
- Управление картами (CRUD)
- Асинхронные запросы с httpx
- Обработка ошибок с логированием
- Совместимость с MCP Inspector

---
## Описание MCP-инструментов
- `boards_list(space_id)` — список досок в пространстве  
- `boards_get(id)` — получение доски по ID  
- `boards_create(space_id, data)` — создание доски  
- `boards_update(board_id, space_id, data)` — обновление доски  
- `boards_delete(board_id, space_id)` — удаление доски с принудительным `force`  
- `cards_list()` — список карт  
- `cards_get(id)` — получение карты по ID  
- `cards_create(data)` — создание карты  
- `cards_update(id, data)` — обновление карты  
- `cards_delete(id)` — удаление карты  
- `spaces_list()` — список пространств  
- `spaces_get(id)` — получение пространства по ID  
- `spaces_create(data)` — создание пространства  
- `spaces_update(id, data)` — обновление пространства  
- `spaces_delete(id)` — удаление пространства  

---
## Быстрый старт
1. Установите зависимости (`pip install -r requirements.txt`)  
2. Добавьте в файл _.env_ DOMAIN и TOKEN, как указано в примере в файле _.env.example_
3. Запустите сервер командой `uv run src/main.py`
4. Используйте MCP-инструменты для вызовов API
5. Логи ошибок и операций пишутся в файл _log.log_