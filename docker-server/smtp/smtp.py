import smtplib


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

smtpObj.login('yurov.mikhail@gmail.com', 'password')

smtpObj.sendmail("yurov.mikhail@gmail.com" "endimey@gmail.com", "Пора баиньки!")

