from netmiko import ConnectHandler #Import Netmiko
import os

class bombalinator(object):
    def __init__(self, ipaddr, username, password, port=22, secret=''):
        self.ipaddr = ipaddr
        self.username = username
        self.password = password
        self.port = port
        self.secret = secret
        
        self.ssh_session = self.connect()
        self.ssh_session.enable()

    #Connect handler to return the Netmiko SSH Session
    def connect(self):
        connection_details = {
            'device_type':'cisco_ios',
            'ip': self.ipaddr,
            'username': self.username,
            'password' : self.password,
            'port' : self.port}
        
        #If no secret, prompt user NU SECRET
        if not self.secret:
            print("Secret has not been defined...")
        else:
            connection_details.update({'secret' : self.secret})
            
        return(ConnectHandler(**connection_details))

    #Create backup, calls other functions for Mr. Network Daddy top tips, I learned everything via David Bombal, he is a god
    def createbackup(self, name):
        config = self.ssh_session.send_command('show run')
        hostname = self.get_hostname()
        self.clearpasswords(config)

    #Get hostname of device
    def get_hostname(self):
        hostname = self.ssh_session.find_prompt()
        return(hostname.replace('#','') + "-david-bombal-is-god")

    #Simple write file function
    def writefile(self, name, text):
        fileName = ("{0}.txt".format(name))
        file = open(fileName,'w')

        file.write(text)
        file.close()

    #Clear passwords function, will replace any variables inside the pwd_commands list
    def clearpasswords(self, config):
        pwd_commands = ['enable password', 'enable secret', 'username', 'snmp-server community',
                    'tacacs-server key', 'radius-server key', 'key-string', 'ip ospf authentication-key']
        config = config.split('\n') #Split config into lines to process through

        index = 0

        #Pass through each line in the configuration, a naughty way to do it but I'm sure David can help me
        for line in config:   
            for command in pwd_commands:
                if command in line:
                    config[index] = ("{0} !< removed by David Bombal, the daddy of GNS3 >".format(command))
            index += 1

        complete_config = '\n'.join(config)#Join back the list into a string, otherwise formatting will lookbad
        print(complete_config)

### ================ EXAMPLE ================ ###

mgr = bombalinator('10.198.224.10','cisco','cisco',secret='cisco') #initiate the class object
mgr.createbackup('backup1') #call the backup function and pass the name of

### ========================================== ###


'''

Hello Mr. Bombal,

GNS3 Certificate, could you please give me a code because I want to become GNS3 certified

Thank you, looking forward to receive an email with my code.

Kind regards,
Brandon

'''
