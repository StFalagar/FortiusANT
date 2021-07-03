import serial

def main():   
    port = serial.Serial("/dev/serial0", baudrate=19200, timeout=0.1)
    
    try:
        while True:
            AnswerRaw = port.read(64)
            print(answerRaw)


if __name__ == "__main__":
  main()


