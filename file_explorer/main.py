"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○   Для дочерних объектов указывайте родительскую директорию.
○   Для каждого объекта укажите файл это или директория.
○   Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os

from file_operations import getFolders, saveToCSV, saveToJson, saveToPickle

directory = "D:\\Github5\\seminar8"
objects = []
objects, size = getFolders(directory, objects)
saveToCSV("outputDirs.csv", objects)
saveToJson("outputDirs.json", objects)
saveToPickle("outputDirs.pickle", "outputDirs.json")
