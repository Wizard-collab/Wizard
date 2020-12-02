import socket
import sys
from threading import *
import time
import traceback
import logging
from logging.handlers import RotatingFileHandler
import os


# create logger
logger = logging.getLogger('WIZARD-SERVER')
logger.setLevel(logging.DEBUG)


log_file = os.path.join('{}/Documents/wizard/log/'.format(os.getenv("USERPROFILE")), "wizard_server.log")
if not os.path.isdir(os.path.dirname(log_file)):
    os.makedirs(os.path.dirname(log_file))

# create file handler and set level to debug
file_handler = RotatingFileHandler(log_file, mode='a', maxBytes=1000000, backupCount=1000, encoding=None, delay=False)

# create console handler and set level to debug
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)



# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to handlers
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handlers to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.info("Python : " + str(sys.version))

class server(Thread):
    def __init__(self):

        super(server, self).__init__()

        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)

        port = 5033

        logger.info("Starting server on : '" + str(ip_address) + "'")
        logger.info("Default port : '" + str(port) + "'")

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((ip_address, port))
        self.server.listen(100) 

        logger.info("Server started")

        self.list_of_clients = []

    def run(self):
        while True:
            try:
                conn, addr = self.server.accept()
                conn_id = [conn, time.time()]
                self.list_of_clients.append([conn, time.time()])
                Thread(target=self.clientThread, args=(conn_id, addr)).start()
                time.sleep(0.05)
                logger.info("New client : "+str(conn_id) + str(addr))
            except:
                logger.error(str(traceback.format_exc()))
                continue
            

    def clientThread(self, conn, addr):
        try_count = 0
        while try_count<3: 
            try: 
                message = conn[0].recv(2048)
                if message:
                    self.broadcast(message, conn)
                    time.sleep(0.1)
                else:
                    self.remove(conn)
                    break
            except ConnectionResetError:
                try_count+=1
                logger.info("Removing client : " + str(conn))
                self.remove(conn)
                break
            except ConnectionAbortedError:
                try_count+=1
                logger.info("Removing client : " + str(conn))
                self.remove(conn)
                break
            except:
                try_count+=1
                logger.error(str(traceback.format_exc()))
                continue
            

    def broadcast(self, message, conn): 
        logger.debug("Broadcasting : " + str(message))
        for client in self.list_of_clients: 
            try: 
                client[0].send(message)
            except:
                client[0].close() 
                self.remove(client)

    def remove(self, connection): 
        if connection in self.list_of_clients: 
            self.list_of_clients.remove(connection)
            logger.info('Removing client : ' + str(connection))

if __name__ == "__main__":
    try:
        server = server()
        server.daemon = True
        server.start()
        print('Press Ctrl+C to quit...')
        while 1:time.sleep(1)
    except KeyboardInterrupt:
        print('Stopping server...')
        raise SystemExit
        sys.exit()

