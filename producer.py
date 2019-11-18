import time
from kafka import KafkaProducer

def main():
  print('Starting Kafka producer...')
  producer = KafkaProducer(bootstrap_servers='34.221.164.208:9092')
  ts_array = []

  user_input = input('Messages to send: ')
  print('Sending {} messages...\n'.format(user_input))

  for _ in range(int(user_input)):
    ts = time.time()
    producer.send('experiment', str(ts).encode())
    log_msg = '{}\t->'.format(ts)
    print(log_msg)
    ts_array.append(log_msg)
    time.sleep(1)
  producer.flush()

  with open('plog.txt', 'w') as f:
    f.write('Producer Log\n')
    for msg in ts_array:
      f.write('{}\n'.format(msg))

if __name__ == '__main__': main()