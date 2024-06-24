import os
import smtplib

my_login = os.environ['LOGIN_YANDEX']

my_pass = os.environ['PASS_YANDEX']

sender_name = "Илья"
recipient_name = "Ира"
website = "https://dvmn.org/referrals/dEEadLN2iikhrftQd9BeakG2ox1jOcXDPHgit4dT/"
senders_email = "Konchanos@yandex.ru"
recipients_email = "ilia.snyatkov@yandex.ru"
the_title = "Приглашение!"
type_of_letter =  'text/plain; charset="UTF-8";'

letter = (f"""From: {senders_email}

To: {recipients_email}

Subject: {the_title}

Content-Type: {type_of_letter}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

     %website% — это новая версия онлайн-курса по программированию. 
     Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

     Как будет проходить ваше обучение на %website%? 

     → Попрактикуешься на реальных кейсах. 
     Задачи от тимлидов со стажем от 10 лет в программировании.
     → Будешь учиться без стресса и бессонных ночей. 
     Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
     → Подготовишь крепкое резюме.
     Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

     Регистрируйся → %website%  
     На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""")
letter = letter.replace("%website%", website).replace("%my_name%", sender_name).replace(" %friend_name%", recipient_name)
letter = letter.encode("UTF-8")


server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
server.login(my_login, my_pass)
server.sendmail("Konchanos@yandex.ru", "ilia.snyatkov@yandex.ru", letter)
server.quit()

