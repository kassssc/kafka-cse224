import time
from kafka import KafkaProducer

def main():
  producer = KafkaProducer(bootstrap_servers='34.221.164.208:9092')
  ts_array = []

  user_input = input('Messages to send: ')
  print('\n')

  for i in range(int(user_input)):
    ts = time.time()
    msg = '{}:\t{}'.format(str(i+1), str(ts))
    producer.send('experiment', msg.encode())
    ts_array.append(msg)
    time.sleep(2)
  producer.flush()

  with open('plog.txt', 'w') as f:
    f.write('Producer Log\n')
    for msg in ts_array:
      f.write('{}\n'.format(msg))

if __name__ == '__main__': main()