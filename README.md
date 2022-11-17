# telegram_bot_anonim_feedback
Telegram бот для анонимной обратной связи

## Запуск бота
- установить Python 3.10.8 с [официального сайта](https://www.python.org/)
- установить Aiogram с помощью команды:
```
pip install -U aiogram
```
- изменить файл `config.py`
  - подставить в `TOKEN` свое значение Bot API, которое нужно получить у бота @BotFather
  - подставить в `ID` свой Telegram User ID, который можно узнать у бота @getmyid_bot
- запустить самого бота 
```
python bot.py
```
 
## Запуск бота на Heroku
После того как подставили свои значения и проверили работоспособность бота проделываем следующие действия:
- скачиваем и устанавливаем [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)
- запускаем консоль и переходим в папку с рабочим ботом
- входим в Heroku с помощью команды:
```
heroku login
```
- нажимаем любую клавишу и авторизуемся через браузер
- запускаем по порядку команды
```
git init
git add .
git commit -m "Release Bot v.1.0"
heroku create telegram_bot_anonim_feedback
git remove -v
git push heroku master
heroku ps:scale worker=1
```
