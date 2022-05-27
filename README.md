# taro_bot
Бот предназначен для людей в развлекательных целях, которым могут пользоваться люди отдельно и в групповых чатах. 
С целью развлечения, путем просмотра рандомных предсказаний.

<p align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/greenderix/taro_bot">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/greenderix/taro_bot">
  <a href="https://github.com/Greenderix/taro_bot/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/greenderix/taro_bot"></a>
</p>

## УСТАНОВКА
Для написания кода использовалась библиотека [telebot](https://core.telegram.org/bots/api).

Для установки всех зависимостей просто пропишите ```python -m pip install -r requirements.txt```

## БЫСТРЫЙ СТАРТ
В файлах [settings.py](https://github.com/Greenderix/taro_bot/blob/master/settings.py) хранится основная информация о вашем боте, а именно ``token``.

В переменную ``token`` необходимо создать и записать токен телеграм бота, в которой у Вас будет находиться бот. Для этого нужно открыть [BotFather](https://t.me/BotFather), после чего написать ему, создать нового бота,
после чего скопировать получившийся токен, который имеет 
следующий формат: ``9999999999:AAE_VQGYPKiizP9ADvGjIefM6ctMa_yGyXM``. 
Получив токен, мы вставляем его уже в программу.

## ЭКСКУРСИЯ
В боте построена небольшая база данных информации о карточках таро, цветах.
Она дает возможность полноценно пользоваться функционалом бота.

Почти весь текст (реакции на команды и т.д.) хранится в файле [tarobot.py](https://github.com/Greenderix/taro_bot/blob/master/tarobot.py)
Вся информация о картах и цвете хранится в файле [infobase](https://github.com/Greenderix/taro_bot/blob/master/infobase.py)


Для удобства навигации во время пользования ботом - реализованы команды [клавиатуры](https://github.com/Greenderix/taro_bot/blob/master/tarobot.py), чтобы пользователи не прописывали постоянно команды.

<p align="center"><a href="https://vk.com/evgenygrinderix" target="_blank"><img src="https://i.imgur.com/IDtdq56.gif"></a></p>


## КОМАНДЫ ПОЛЬЗОВАТЕЛЕЙ

+ **🔮 Аркан дня** - команда для просмотра рандомного предсказания аркана дня.
+ **🎱 Число дня** - команда для просмотра рандомного числа дня.
+ **🧿 Цвет дня** - команда для просмотра рандомного цвета дня.
+ **Другое...** - временная команда, для проверки информации о новвоведениях.
+ **/start** - вызов пользователем меню.



