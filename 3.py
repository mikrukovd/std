import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

website = os.getenv('WEBSITE')
friend_name = os.getenv('FRIEND_NAME')
my_name = os.getenv('MY_NAME')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
email_from = os.getenv('EMAIL_FROM')
email_to = os.getenv('EMAIL_TO')

letter = """From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(website=website,friend_name=friend_name,my_name=my_name, email_from = email_from,email_to=email_to)

letter = letter.encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.com:465')
server.login(login, password)
server.sendmail(email_from, email_to, letter)

server.quit()