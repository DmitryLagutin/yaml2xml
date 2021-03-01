from helper import *
from pprint import pprint
import yaml

# Введите путь yaml схемы
path_yaml = 'yaml/standard.yaml'
# Введите пути, по которому будет сформирован xml файл
path_xml = 'xml/new.xml'
xml_str = yaml_to_xml(path_yaml)
make_file(path_xml, xml_str)
print(f'Создан xml файл по пути {path_xml}')


# # Валидация
# validate('xml/new.xsd', 'xml/new.xml')
