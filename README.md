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

Для начала необходимо задать реквизиты доступа к API lanbilling. Для этого необходимо заполнить следующие переменные:
```bash
DBI_SOAP = {
    "login": os.getenv("DBI_SOAP_LOGIN", "fix-dbt-time"),
    "pass": os.getenv("DBI_SOAP_PASSWORD", "CBhOlvoKXEkU3BFaXBBwjUAm"),
    "service": os.getenv("DBI_SOAP_SERVICE",
                         "http://dbt20.flexline.ru:34012"),
    "wsdl": os.getenv("DBI_SOAP_WSDL",
                      "http://dbt20.flexline.ru/admin/soap/api3.wsdl")
}
```

## Алгоритм работы
