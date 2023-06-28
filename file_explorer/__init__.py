# Файл __init__.py пакета file_explorer

# Импортируем модули и функции из файлов пакета
from .file_operations import getFolders, saveToJson
from .explorer_object import tojson

# Экспортируем функции для использования извне
__all__ = [
    'getFolders',
    'saveToJson',
]
