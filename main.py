#~~~ Pratham-code ~~~
import os
from email.message import EmailMessage
import ssl
import smtplib
import time

#~~~ PASSWORD ~~
password = 'muuyaircfwqhifgm'

#~~~ MAIL IDS ~~~
send = 'tastpro28@gmail.com'
receiver1 = ('patelpratham281@gmail.com')
receiver2 = ('patelpratham964@gmail.com')
receiver3 = ('heetvp28@gmail.com')
receiver4 = ('patelpratham964@gmail.com', 'heetvp28@gmail.com')

#~~~ CODE ~~~
contest = ssl.create_default_context()


#~~~ CODE FOR SEND ~~~
def msend1():
  #1 mailcode
  subject1 ="mail bot π"
  body1 = """
        all mails send by bot π
          """
  em1 = EmailMessage()
  em1['Fromπ€'] = send
  em1['to'] = receiver1
  em1['Subject'] = subject1
  em1.set_content(body1)
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contest) as smtp:
          smtp.login(send, password)
          smtp.sendmail(send, receiver1, em1.as_string())
        

def msend2():
    #2 mailcode
  subject2 ="hello π"
  body2 = """
hello 
i am ai  
good morning π
don't forget to bring Document π
           """
  em2 = EmailMessage()
  em2['Fromπ€'] = send
  em2['to'] = receiver4
  em2['Subject'] = subject2
  em2.set_content(body2)
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contest) as smtp:
          smtp.login(send, password)
          smtp.sendmail(send, receiver4, em2.as_string())
         

def msend3():
  #3 mailcode
  subject3 ="Helloπ"
  body3 = """
Hello Heet π
Your Are Programmer π»
          """
  em3 = EmailMessage()
  em3['Fromπ€'] = send
  em3['to'] = receiver3
  em3['Subject'] = subject3
  em3.set_content(body3)
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contest) as smtp:
          smtp.login(send, password)
          smtp.sendmail(send, receiver3, em3.as_string())
          

def msend4():
    #4 mailcode
  subject4 ="Activity"
  body4 = """
Hello Pratham π
Activity Normal β
          """
  em4 = EmailMessage()
  em4['Fromπ€'] = send
  em4['to'] = receiver1
  em4['Subject'] = subject4
  em4.set_content(body4)
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contest) as smtp:
          smtp.login(send, password)
          smtp.sendmail(send, receiver1, em4.as_string())
          

def msend5():
  #5 mailcode
  subject5 ="mail bot π"
  body5 = """
Hello Pratham π
You Are OP Programmer π»
          """
  em5 = EmailMessage()
  em5['Fromπ€'] = send
  em5['to'] = receiver2
  em5['Subject'] = subject5
  em5.set_content(body5)
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contest) as smtp:
          smtp.login(send, password)
          smtp.sendmail(send, receiver2, em5.as_string())


#~~~ MAIN CODE ~~
input("enter")
print("runing")
time.sleep(28800)
msend1()
msend4()
print("ALL MAIN ARE SEND β")
time.sleep(18000)

while time:
   print("....")
   time.sleep(86400)
   msend3()
   msend4()
   msend5()
   msend1()
   print("ALL MAIN ARE SEND β")
   