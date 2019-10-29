from configparser import ConfigParser
import os, sys
class Cfg:
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, '../config/')
    parser = ConfigParser()
    try:
        parser.read(filename + "config.ini")
    except Exception as e:
        print('[ ERROR ] Config Error:', e)
    else:
        try:
            TOKEN = parser.get("settings", "token")
            LOG_CHANNEL = parser.get("settings", "log_channel")
            NEW_MEMBER_CHANNEL = parser.get("settings", "new_member_channel")
            PREFIX = parser.get("settings", "prefix")
        except Exception as e:
            print('[ ERROR ] Config Error:', e)

class FileRead:
    try:
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '')
    except Exception as e:
        print("[ ERROR ] Path Error:", e)
    else:
        try:
            website = open(filename + '../config/website.txt')
            wsite = website.read()
        except FileNotFoundError as e:
            print('[ ERROR ] File Not Found Error:', e)
            wsite = 'webiste'
        except Excpetion as e:
            print('[ ERROR ] File Error:', e)
            wsite = 'website'
        else:
            website.close()

        try:
            newuser = open(filename + '../config/newuser.txt')
            hellonewuser = newuser.read()
        except FileNotFoundError as e:
            print('[ ERROR ] File Not Found Error:', e)
            hellonewuser = 'Wellcome!'
        except Excpetion as e:
            print('[ ERROR ] File Error:', e)
            hellonewuser = 'Wellcome!'
        else:
            newuser.close()
