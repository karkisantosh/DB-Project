# DB-Project
The David Bombal Project

## This project was designed to help fellow David Bombal fans to sky-rocket their python skills with GNS3 and Cisco.
David Bombal has been my hero ever since he introduced me into Python and how to automate very simple things so I decided to write a basic function (which will be updated with later functions if I get recommendations) to create a backup and remove passwords from the running-configuration, and saves a file in the scripts directory.

The main thing about this is that the script is using the Netmiko module which is safer than running a 'show run' via Telnet. Telnet on your own company network is still something that people don't worry about but a running config flying around on the network unencrypted, in plain text is a no no and I'm sure my hero David would agree.

I encourage you to use Netmiko (SSH) because the plain communication over the network is technically encrypted until it hits your computer and the text is displayed in python/in the text file.


An example to use this script is provided in the file itself, but you will need to initiate the class which establishes the SSH connection and then further run functions provided in the class like 'createbackup()'

```py
mgr = bombalinator('10.198.224.10','cisco','cisco',secret='cisco') #initiate the class object
mgr.createbackup('backup1') #call the backup function and pass the name of
```
