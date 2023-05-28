import smtplib
import sys
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class SMTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.smtp = smtplib.SMTP(host, port)
        self.smtp.set_debuglevel(1)
    
    def connect(self , email, password):
        try:
            self.smtp.starttls()
            self.smtp.login(email, password)
        except Exception as e:
            print(e)
            
    def disconnect(self):
        self.smtp.quit()
        
    def sendEmail(self, from_addr, to_addr, msg):
        self.smtp.sendmail(from_addr, to_addr, msg)
        
if __name__  == '__main__':
    log_file = open("smtp_debug.log", 'w')
    original_stderr = sys.stderr
    sys.stderr = log_file
    
    with open(os.path.join(BASE_DIR, 'smtp.conf')) as config_file:
        config = dict(line.strip().split('=') for line in config_file)
        
    HOST = config.get("HOST")
    PORT = int(config.get("PORT", 587))
    EMAIL = config.get("EMAIL")
    RECIPIENT_EMAIL = config.get("RECIPIENT_EMAIL")
    PASSWORD = config.get("PASSWORD")
    
    mySMTP = SMTPServer(HOST, PORT)
    mySMTP.connect(EMAIL, PASSWORD)
    mySMTP.sendEmail(EMAIL, RECIPIENT_EMAIL, "Hello World")
    mySMTP.disconnect
    
    log_file.close()
    sys.stderr = original_stderr