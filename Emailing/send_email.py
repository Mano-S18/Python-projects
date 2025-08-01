import smtplib
from email.message import EmailMessage
from string import Template
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from credentials.cnfg import mail


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = mail.frm
email['to'] = mail.to
email['subject'] = 'Good Luck Man'

email.set_content(html.substitute({'name' : 'Mano'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(mail.user,mail.pawd)
    connection.send_message(email)