#  FUNCTION     Week 12 
#               subprocess
#  DATE         APRIL 2020 - Week 12
#  FILE         W12_Lecture_example.py
#--------------------------------------------------

import subprocess
import datetime
datNow = datetime.datetime.now()
datDate = datetime.datetime.now().date()
print(datNow)
print("Output with out.stdout.decode() ")

print()
p = subprocess.run(["ping", "fanshawec.ca"], stdout=subprocess.PIPE)
print(p.stdout.decode())

print("\nOutput with out.stdout and with universal_newlines=True")
print()
prog = subprocess.run(["ping", "fanshawec.ca"], stdout=subprocess.PIPE, universal_newlines=True)
print(prog.stdout)

print("\nOutput with out.stdout and without universal_newlines=True")
print()
prog = subprocess.run(["ping", "fanshawec.ca"], stdout=subprocess.PIPE)
print(prog.stdout)

print("\nping 10.0.0.1")
prog = subprocess.run(["ping", "10.0.0.1"], stdout=subprocess.PIPE)
print(prog.stdout.decode())

print("\nping 8.8.8.8")
prog = subprocess.run(["ping", "8.8.8.8"], stdout=subprocess.PIPE)
print(prog.stdout.decode())



print('\nOutput with subprocess.run(["dir"]')
print()

prog = subprocess.run(["dir"], shell=True)
print(prog.stdout)

print('\nOutput with subprocess.run(["dir", "c:\\"]')
print()
prog = subprocess.run(["dir", "c:\\"], shell=True)
print(prog.stdout)


print("\narp for 192.168.2.1")
prog = subprocess.run(["arp", "-a", "192.168.2.1"])
print(prog.stdout)

print("\narp for all")
prog = subprocess.run(["arp", "-a"])
print(prog.stdout)


print("\output for IPCONFIG")
x =subprocess.run(['IPCONFIG'])
print(x.stdout)


print("output for IPCONFIG")
x =subprocess.run(['IPCONFIG'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(x.stdout)

print("Output for NetStat")
x =subprocess.run(['NETSTAT'])
print(x.stdout)


print("Output for SYSTEMINFO")
x = subprocess.run(['SYSTEMINFO'], stdout=subprocess.PIPE, universal_newlines=True)

print(x.stdout)    # if needed output x to a file (week 5)


print("Output for nslookup")
subprocess.run( [ 'nslookup', 'wikipedia.com'] )

import smtplib, getpass

print("getting IPCONFIG to send in email")
x =subprocess.run(['IPCONFIG'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


#to_email = input("To email: ")  #gets user to enter email address to send to
#from_email = input("From email: ") #gets user to enter email address to from
#upassword = getpass.getpass()  #gets password but it is not visible when entered password. works in Terminal not in wing idle

#smtpObj = smtplib.SMTP('imap-mail.outlook.com', 587) #hotmail / outlook account, if you want gmail need to change it

#smtpObj.starttls()

#smtpObj.login(from_email, upassword)
#'''
#sendmail method gets 
#from email address, 
#email address to send to, and 
#messsage. notice that message starts with Subject: 
#Everything between 'Subject:' and '\n\n' will be in subject line of email.  
#You need the '\n\n' to start writing into the body. 
#everthing on the right will be in the body of the email.
#'''
#smtpObj.sendmail(from_email, to_email, 'Subject: Test,\n\nDear tester, this is a test!!!!!! {0}'.format(x.stdout)) #the output of x will be in the body of the email
#smtpObj.quit()
#print()
#print("Sent email")
#input()