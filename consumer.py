
import time
from kafka import KafkaConsumer

def main():
  consumer = KafkaConsumer('experiment', bootstrap_servers='34.221.164.208:9092')
  ts_array = []

  for msg in consumer:
    ts = time.time()
    msg_ts = msg.value + '\t->\t' + str(ts)
    diff = ts - float(msg.value.split('\t')[1])
    msg_ts = msg_ts + '\t\t' + str(diff)
    ts_array.append(msg_ts)
    print(msg_ts)

  with open('clog.txt', 'w') as f:
    f.write('Consumer Log\n')
    for msg in ts_array:
      f.write(msg + '\n')


if __name__ == '__main__': main()