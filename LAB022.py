import smtplib

mailFrom = 'Your automation system'
mailTo = ['proko.piotr@gmail.com', 'patpyska@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello
 
This mail confirms that processing has finished without problems,
 
Have a nice day!'''
 
message = '''From: {}
Subject: {}
 
{}
'''.format(mailFrom, mailSubject, mailBody)

user = 'Proko.Piotr@gmail.com'
password = "HomeOne1234"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')
