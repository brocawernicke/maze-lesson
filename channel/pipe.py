import os, time

class Channel:
  def __init__(self):
    self.rf = None
    self.wf = None
    self.buf = []

  def open(self, read_path: str, write_path: str):
    if not os.path.exists(read_path):
        os.mkfifo(read_path)
    if not os.path.exists(write_path):
        os.mkfifo(write_path)

    self.rf = os.open(read_path, os.O_CREAT | os.O_RDWR | os.O_SYNC)
    self.wf = os.open(write_path, os.O_CREAT | os.O_RDWR | os.O_SYNC)

  def receive(self) -> str:
    buf = os.read(self.rf, 1024)
    self.buf = buf.decode()
    print('received {0} bytes: {1}'.format(len(self.buf), self.buf))
    return self.buf

  def send(self, buf: str):
    print('send {0} bytes: {1}'.format(len(buf), buf))
    os.write(self.wf, buf.encode())
    time.sleep(1)

  def listen(self) -> str:
    while True:
      buf = os.read(self.rf, 1024)
      self.buf = buf.decode()
      if len(self.buf) > 0:
        return self.buf
      time.sleep(1)

  def close(self):
    os.close(self.rf)
    os.close(self.wf)
