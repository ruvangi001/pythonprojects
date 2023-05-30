import smtplib

#basic
sender_email = 'vekariyaruvi16@gmail.com'
rec_email = 'chanchadkishan37@gmail.com'
password = input('Enter your password:- ')
message = 'Sending email trail.'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print('Login Success')
server.sendmail(sender_email, rec_email, message)
print('Email has been sent to ',rec_email)
server.close()
print('Server closed.')