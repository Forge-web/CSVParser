# Parser CSV file
---

## установка зависимостей

- для **uv**

```shell
    uv add -r requirements.txt
```

- для **poetry**

```shell
    poetry add $(cat requirements.txt)
```

- для **pip**

```shell
    pip install -r 'requirements.txt'
```

---

## запуск

- для указания файла **--file test.csv**

- фильтрация по одному из столбцов **--where 'column{>, <, =}value'**

- для агрегации **--aggregate 'column={avg, min, max}'**
Принимает только числовые столбцы

```shell
    uv run main.py --file test.csv --where 'price>500'

    # test csv file: 
    # name,brand,price,rating
    # iphone 15 pro,apple,999,4.9
    # iphone 16 pro,apple,1999,4.9
    # galaxy s23 ultra,samsung,1199,4.8
    # redmi note 12,xiaomi,199,4.6
    # poco x5 pro,xiaomi,299,4.4

    #output:
    # +------------------+---------+---------+----------+
    # | name             | brand   |   price |   rating |
    # +==================+=========+=========+==========+
    # | iphone 15 pro    | apple   |     999 |      4.9 |
    # +------------------+---------+---------+----------+
    # | iphone 16 pro    | apple   |    1999 |      4.9 |
    # +------------------+---------+---------+----------+
    # | galaxy s23 ultra | samsung |    1199 |      4.8 |
    # +------------------+---------+---------+----------+
```

```shell
    uv run main.py --file test.csv --where 'price>500' --aggregate 'price=avg'
    
    #output
    # +-------+
    # |   avg |
    # +=======+
    # |  1399 |
    # +-------+
```

- **--aggregate** можно использовать и без **--where**

```shell
    uv run main.py --file test.csv --aggregate 'price=avg'

    #output
    # +-------+
    # |   avg |
    # +=======+
    # |   939 |
    # +-------+
```

---

## Тесты

- для запуска тестирования

```shell
    uv run pytest
    # or
    pytest
```
