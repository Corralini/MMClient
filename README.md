# MMClient
MM Client is used to Manage and Monitor computers in network.

## Installation
First you have to clone git repository.
```bash
git clone https://github.com/Corralini/MMClient.git
```
Next you have to install requirements.
```bash
pip install requirements.txt
```
Run MM Client by terminal.
```bash
py main.py
```
## Configuration
Inside config directory there are two files.

### main.cfg
Here is all the configuration related to this application directly
```cfg
[global]
;Rate to refresh data in Seconds
;Default 30 seconds
refreshRate = 30

;Rate to read received instructions in Seconds
;Default 15 seconds
instructionsRate = 15


[disk]
;Disk to monitoring
disk1=c:/
disk2=d:/
disk3=H:/
```

### server.cfg
Here is all the configuration about MMCore.

```
[global]
;network name where M&MCore is running
serverIp = ARCFDC01

;Path to M&MCore shared folder
;In this folder M&MClient save and receives all data
;IMPORTANT: WITHOUT IP OR NETWORK NAME
pathName = /mm


;Letter for mapping net folder
;Only if Windows
mappingLetter = Y

[user]
userLogin = arcfernandez.com\\mm
psswdLogin = abc123.
```

## Note
MMClient have to be installed in all computer you want to monitor and manage
