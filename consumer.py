import sys
import time
from kafka import KafkaConsumer

def main():
  try:
    consumer = KafkaConsumer('experiment', bootstrap_servers='34.221.164.208:9092')
    ts_array = []
    diffs = []

    for msg in consumer:
      ts = time.time()
      msg_ts = '{}\t->\t{}'.format(msg.value, str(ts))
      diff = ts - float(msg.value.split('\t')[1])
      msg_ts = '{}\t{}'.format(msg_ts, str(diff))
      ts_array.append(msg_ts)
      diffs.append(diff)
      print(msg_ts)

  except KeyboardInterrupt:
    with open('clog.txt', 'w') as f:
      f.write('Consumer Log\n')
      for msg in ts_array:
        f.write('{}\n'.format(msg))
      avg_diff = sum(diffs) / len(diffs)
      f.write('Average Diffs:\t{}\n'.format(avg_diff))
      f.write('Average RTT:\t{}\n'.format(avg_diff*2))
    sys.exit()


if __name__ == '__main__': main()