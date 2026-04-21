# Учебный проект в рамках курса "Автоматизация тестирования с помощью Selenium и Python"

## Проект содержит набор тестовых сценарием на языке Python с применением инструментария selenium

### Описание

Проект содержит тестовые сценарии для проверки работы сайта интернет-магазина,
размещенного по адресу http://selenium1py.pythonanywhere.com/

* Для запуска тестовых сценариев необходимо установить (инструкция для ОС Windows):

	* Python ([скачать](https://www.python.org/downloads/windows/) )
	* драйвер для браузера (ChromeDriver - [скачать](https://sites.google.com/chromium.org/driver/downloads))

* Создать виртуальное окружение для python:
```
mkdir environments
cd environments
python -m venv selenium_env
```

* Получить локальную копию репозитория https://github.com/yurg824-gif/selenium-final
```
mkdir selenium-final
git clone https://github.com/yurg824-gif/selenium-final

```

* Активировать виртуальное окружение:
```
selenium_env\Scripts\activate.bat
```
* Настроить виртуальное окружение, установив
необходимы пакеты, в том числе selenium и pytest
```
pip install -r selenium-final\requirements.txt
```

* Запуск тестов для ревью:

```
cd selenium-final
pytest -v --tb=line -m need_review
```

