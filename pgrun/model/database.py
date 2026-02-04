class Database:
    def __init__(self, host: str, port: int, db_name: str, username: str, pwd: str):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.username = username
        self.pwd = pwd
