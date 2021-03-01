# yaml_to_xml

## Как установить зависимотсти

Установить необходимые пакеты
```shell
pip install -r requirements.txt
```

## Как запустить

Для для начала необходимо создать файл standard.yaml в папке yaml в проекте:
```yaml
Файл:
  А1: "2121212121"
  Б1: '22.05.2001'
  B1: '3232'
  Г1: '080'
  Документ:
    - A2: '1124549845'
      Б2:
        A3: '57540534543'
        Б3: '575325725432'
        В3: '12289188534243'
        Г3:
          А4: '01'
          Б4: '493849343984'
          В4: '483949394838'
          Г4: '21.02.2011'
```

## Алгоритм работы
На основе standard.yaml будет сформирован xml файл

Запустить main.py
```python
# Введите путь yaml схемы
path_yaml = 'yaml/standard.yaml'
# Введите пути, по которому будет сформирован xml файл
path_xml = 'xml/new.xml'
xml_str = yaml_to_xml(path_yaml)
make_file(path_xml, xml_str)
print(f'Создан xml файл по пути {path_xml}')
```

После того как будет создан xml файл, средствами Pycharm сгенерируйте xsd файл (схему для валидации)
![image](https://user-images.githubusercontent.com/38376206/109461768-b4ea1700-7a73-11eb-9e2c-8da9e87477d5.png)
После того как будет создана схема, появляется возможность запустить процесс валидации с помощью функции (main.py)
```python
# Валидация
validate('xml/new.xsd', 'xml/new.xml')
```
![image](https://user-images.githubusercontent.com/38376206/109462200-2fb33200-7a74-11eb-8971-cf8adb42f0e4.png)
