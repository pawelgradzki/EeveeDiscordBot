from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'TOKEN': 'CHANGE_ME',
    'LOG_CHANNEL': 'CHANGE_ME',
    'NEW_MEMBER_CHANNEL': 'CHANGE_ME',
    'PREFIX': 'CHANGE_ME'
}

with open('config.ini', 'w') as f:
    config.write(f)
