# yaml_to_xml

## Как установить зависимотсти

Установить необходимые пакеты
```shell
pip install -r requirements.txt
```

Затем загрузить пакеты из pypy.flexline.ru
```shell
pip install -r requirements-fl.txt --extra-index-url=http://pypi.flexline.ru/simple --trusted-host=pypi.flexline.ru
```

## Как запустить

Для для начала необходимо создать файл standard.yaml по пути yaml в проекте:
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
