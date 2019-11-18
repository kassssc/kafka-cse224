#!/usr/bin/env python3

import time

def main():
  # Producer
  ts_array = []

  for i in range(10):
    ts = time.time()
    msg = str(i+1) + ':\t' + str(ts)
    ts_array.append(msg)

  with open('plog.txt', 'w') as f:
    f.write('Producer Log\n')
    for msg in ts_array:
      f.write(msg + '\n')

  # Consumer
  for idx, msg in enumerate(ts_array):
    ts = time.time()
    msg_ts = ts_array[idx] + '\t->\t' + str(ts)
    diff = ts - float(ts_array[idx].split('\t')[1])
    msg_ts = msg_ts + '\t\t' + str(diff)
    ts_array[idx] = msg_ts

  with open('clog.txt', 'w') as f:
    f.write('Consumer Log\n')
    for msg in ts_array:
      f.write(msg + '\n')

if __name__ == '__main__': main()