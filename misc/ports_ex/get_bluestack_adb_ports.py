import json
import re
import misc.ports_ex.config as config



def get_instanses_data():
    """
    Получения данных активных инстансов
    """

    # Загрузка данных из JSON файла
    with open(config.MimMetaData_dir, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Инициализация словаря
    instance_dict = {}

    # Обработка данных из JSON
    for item in data['Organization']:
        instance_name = item['InstanceName']
        name = item['Name']
        instance_dict[instance_name] = {
            'InstanceName': instance_name,
            'Name': name,
            'port': 'Unknown'  # Инициализируем с значением 'Unknown'
        }

    # Чтение конфигурационного файла
    with open(config.bluestacks_conf_dir, 'r', encoding='utf-8') as conf_file:
        conf_content = conf_file.read()

    # Регулярное выражение для поиска строк с портами
    pattern = re.compile(r'bst\.instance\.(\w+)\.status\.adb_port="(\d+)"')

    # Поиск всех совпадений в конфигурационном файле
    matches = pattern.findall(conf_content)

    # Обновление словаря instance_dict с портами
    for match in matches:
        instance_name, port = match
        if instance_name in instance_dict:
            instance_dict[instance_name]['port'] = port

    keys_to_remove = ['Pie64', '', 'Pie64_70', 'Pie64_71' ]
    for key in keys_to_remove:
        if key in instance_dict:
            del instance_dict[key]

            # Вывод результата
    # Разделение словаря на два
    dict_1143 = {k: v for k, v in instance_dict.items() if v['Name'].startswith('1143_')}
    dict_1220 = {k: v for k, v in instance_dict.items() if v['Name'].startswith('1220_')}

    # Сохранение первого словаря в JSON файл
    with open('1143_instance_data.json', 'w', encoding='utf-8') as file_1143:
        json.dump(dict_1143, file_1143, ensure_ascii=False, indent=4)

    # Сохранение второго словаря в JSON файл
    with open('1220_instance_data.json', 'w', encoding='utf-8') as file_1220:
        json.dump(dict_1220, file_1220, ensure_ascii=False, indent=4)

    print("Словари успешно сохранены в файлы 1143_instance_data.json и 1220_instance_data.json")



if __name__ == '__main__':
    get_instanses_data()







