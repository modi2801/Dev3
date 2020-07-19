import smtplib as sm
msg="This mail is regarding your Third Task of Devops Assembly Lines. Your web-app is not found... Restarting!!!!"
server=sm.SMTP_SSL("smtp.gmail.com", 465)
server.login("robertjr.2801@gmail.com","<YOUR PASSWORD>")
server.sendmail("robertjr.2801@gmail.com","modifearless@gmail.com", msg)
server.close()
