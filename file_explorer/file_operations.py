import os
import csv
import json
import pickle

import explorer_object


def getFolders(baseDir, objects):
    # установим лимит, чтобы выполнением не требовало много времени/ресурсов
    # если выббранная папка содержит слишком много элементов
    total_size = 0
    if len(objects) > 100:
        return objects
    for dirpath, dirnames, filenames in os.walk(baseDir):
        pDir = str(baseDir)
        pDir = pDir.split('\\')
        pDir = pDir[len(pDir) - 1]

        for filename in filenames:

            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
            o = explorer_object.ExplorerObject(str(filename), pDir, "F", os.path.getsize(filepath), "")
            if o not in objects:
                objects.append(o)

        for dirname in dirnames:
            # dirpath2 требуется, дабы предовратить изменение итерируемого dirpath
            dirpath2 = os.path.join(dirpath, dirname)
            objects, size = getFolders(dirpath2, objects)
            total_size += size
            o = ExplorerObject(str(dirname), pDir, "D", size, "")
            if (o not in objects):
                objects.append(o)

    return objects, total_size


def saveToCSV(output, objects):
    with open(output, 'w', newline='') as file:
        writer = csv.writer(file)
        # Записываем заголовки столбцов
        writer.writerow(['Name', 'Parent', 'Type', 'Size'])
        for o in objects:
            writer.writerow([o.name, o.parent, o.oType, o.size])


def saveToJson(output, objects):
    records = []
    for o in objects:
        # print(o.toJSON())
        # print(o.toJSON().replace("\\n", "\n"))
        records.append(o.tojson())
    # print(records)
    with open(output, 'w') as file:
        file.writelines("[\n")

        # for o in objects:
        file.writelines(",\r".join(records))
        file.writelines("\n]")
        # json.dump(records, file, indent=4)


def saveToPickle(output, jsonpath):
    data = None
    with open(jsonpath, 'r') as jf:
        data = json.load(jf)
    with open(output, 'wb') as pf:
        pickle.dump(data, pf)
