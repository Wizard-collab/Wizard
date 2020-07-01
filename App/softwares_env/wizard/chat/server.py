from socket import *
from PyQt5.QtCore import QThread, pyqtSignal
from wizard.tools import log
from wizard.prefs import project
from wizard.tools import utility as util
import traceback
import popup
from wizard.project.chat_archives import archives
import time

logger = log.server_log()


class server(QThread):
    new_client_connection = pyqtSignal(str)
    new_client_chat_connection = pyqtSignal(str)

    def __init__(self):
        super(server, self).__init__()

        self.port = 5000
        self.clients = []
        self.clients_chat = []
        self.host_name = gethostname()
        self.host_ip = gethostbyname(self.host_name)
        print(self.host_name)
        print(self.host_ip)
        self.local = None
        self._init_server()
        self.archives = archives()
        
        self.dump_timer = dump_timer()
        self.dump_timer.start()
        self.dump_timer.dump_signal.connect(self.archives.write_chat_file)

    def _init_server(self):
        host_ip = project.get_server_ip()
        if host_ip and host_ip != self.host_ip:
            try:
                self.test_connection(host_ip)
                print(f'Connected to server : {host_ip}')
            except:
                print(f'Failed to connect to server : {host_ip}')
                self.host()
        else:
            print(f'No server found')
            self.host()

    def host(self):
        host_ip = self.host_ip
        project.set_server_ip(host_ip)
        self.create_server(host_ip)

    def test_connection(self, ip):
        server = socket(AF_INET, SOCK_STREAM)
        server.settimeout(1)
        server.connect((ip, self.port))
        server.close()

    def create_server(self, ip):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((ip, self.port))
        self.server.listen(10)
        self.local = 1
        logger.info(f'Server initiated on port {self.port}, ip : {ip}')
        popup.popup().server_pop(f'Server initiated on port {self.port}, ip : {ip}')

    def _new_client(self, conn, addr):
        user = conn.recv(2048)
        user = user.decode('utf-8')
        if user == 'temp_conn':
            message = conn.recv(2048)
            conn.close()
            self.broadcast(message)
        elif user == 'temp_conn_chat':
            message = conn.recv(2048)
            conn.close()
            self.broadcast_chat(message)
            self.archives.add_message(util.decode_message(message))
        elif user == 'null_conn':
            conn.close()
        elif user.startswith('chat_user_'):
            user = user.replace('chat_user_', '')
            logger.info(f'{user} joined the chat (ip : {addr})')
            self.client_chatThread = client_chatThread(user, self, conn, addr)
            self.clients_chat.append([conn, self.client_chatThread])
            self.client_chatThread.start()
            self.new_client_chat_connection.emit('')
        else:
            logger.info(f'{user} joined the wall (ip : {addr})')
            self.client_thread = clientThread(user, self, conn, addr)
            self.clients.append([conn, self.client_thread])
            self.client_thread.start()
            self.new_client_connection.emit('')

    def broadcast(self, message):
        for client in self.clients:
            try:
                client[0].send(message)
            except:
                client[0].close()
                self._remove(client)

    def broadcast_chat(self, message):
        for client in self.clients_chat:
            try:
                client[0].send(message)
            except:
                client[0].close()
                self._remove_chat(client)

    def _remove(self, client):
        if client in self.server.clients:
            self.server.clients.remove(client)
            self.client[-1].quit()
            logger.info(f'{self.user} just leaved the wall')
            self.new_client_connection.emit('')

    def _remove_chat(self, client):
        if client in self.server.clients_chat:
            self.server.clients_chat.remove(client)
            self.client[-1].quit()
            logger.info(f'{self.user} just leaved the chat')
            self.new_client_chat_connection.emit('')

    def run(self):
        while 1:
            try:
                conn, addr = self.server.accept()
                self._new_client(conn, addr)
            except AttributeError:
                self.host()
            except:
                logger.critical(str(traceback.format_exc()))


class clientThread(QThread):
    def __init__(self, user, server, conn, addr):
        super(clientThread, self).__init__()
        self.conn = conn
        self.server = server
        self.user = user
        self.run = 1
        self.addr = addr

    def run(self):
        while self.run:
            try:
                message = self.conn.recv(2048)
                if message != '':
                    self._broadcast(message)
            except:
                try:
                    self._remove(self.conn)
                except:
                    pass

    def _broadcast(self, message):
        for client in self.server.clients:
            try:
                client[0].send(message)
            except:
                client[0].close()
                try:
                    self._remove(client)
                except:
                    pass

    def _remove(self, client):
        for walk_client in self.server.clients:

            if walk_client[-1].conn == client:
                self.server.clients.remove(walk_client)

        if client == self.conn:
            logger.info(f'{self.user} just leaved the wall')
            self.server.new_client_connection.emit(self.user)
            self.quit()
            self.run = 0

class client_chatThread(QThread):
    def __init__(self, user, server, conn, addr):
        super(client_chatThread, self).__init__()
        self.conn = conn
        self.server = server
        self.user = user
        self.run = 1
        self.addr = addr

    def run(self):
        while self.run:
            try:
                message = self.conn.recv(2048)
                if message != '':
                    self._broadcast(message)
            except:
                try:
                    self._remove(self.conn)
                except:
                    pass

    def _broadcast(self, message):
        for client in self.server.clients_chat:
            try:
                client[0].send(message)
            except:
                client[0].close()
                try:
                    self._remove(client)
                except:
                    pass

    def _remove(self, client):
        for walk_client in self.server.clients_chat:

            if walk_client[-1].conn == client:
                self.server.clients_chat.remove(walk_client)

        if client == self.conn:
            logger.info(f'{self.user} just leaved the chat')
            self.server.new_client_chat_connection.emit(self.user)
            self.quit()
            self.run = 0

class dump_timer(QThread):
    
    dump_signal = pyqtSignal(str)

    def __init__(self):
        super(dump_timer, self).__init__()

    def run(self):
        while 1:
            time.sleep(1)
            self.dump_signal.emit('')