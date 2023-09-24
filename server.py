import socket
import random

def createServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('10.0.0.138', 3000))
    print("SERVER OK")
    return server

def getRandomChoice():
    return random.randint(0, 3)

def sendCommand(client, GPIOpin):
    client.send(GPIOpin.encode())

def main():
    LEDarray = [17,27,22,25]
    server = createServer()
    server.listen(1)
    print("WAITNIG FOR CLIENT CONNECTION")
    client, address = server.accept()
    print("CLIENT OK")

    while True:
        computerChoice = getRandomChoice()
        sendCommand(client, LEDarray[computerChoice])