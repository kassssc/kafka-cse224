
import time
from kafka import KafkaProducer

def main():
  producer = KafkaProducer(bootstrap_servers='34.221.164.208:9092')
  ts_array = []

  for i in range(10):
    ts = time.time()
    msg = str(i+1) + ':\t' + str(ts)
    producer.send('experiment', msg.encode())
    ts_array.append(msg)
  producer.flush()

  with open('plog.txt', 'w') as f:
    f.write('Producer Log\n')
    for msg in ts_array:
      f.write(msg + '\n')

if __name__ == '__main__': main()