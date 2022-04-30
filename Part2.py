import yagmail

# Edit Register Info, SMTP connection info, and To Email Info

# Initialize Credentials [Username / Password]
yagmail.register('InsertYourEmail', 'InsertYourPassword')

# Start an SMTP connection
yag = yagmail.SMTP('InsertYourEmail')

# Variables of the SMTP 
to = 'InsertAnotherEmail'
subject = 'This is the subject'
body = 'Testing the email SMTP'
attach = ['ThumbsUp.jpg']			# Must Edit Path of Image

# Sending SMTP
yag.send(to = to, subject = subject, contents = body, attachments = attach)

