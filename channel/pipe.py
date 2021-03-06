import os, time, logging

class Channel:
  def __init__(self, read_path:str, write_path: str):
    self.rf = None
    self.wf = None
    self.buf = []
    
    self.read_path = read_path
    self.write_path = write_path
    
    if not os.path.exists(read_path):
        os.mkfifo(read_path)
    if not os.path.exists(write_path):
        os.mkfifo(write_path)

  def __exit__(self):
    os.remove(self.read_path)
    os.remove(self.write_path)

  def open(self):
    self.rf = os.open(self.read_path, os.O_CREAT | os.O_RDWR | os.O_SYNC)
    self.wf = os.open(self.write_path, os.O_CREAT | os.O_RDWR | os.O_SYNC)

  def receive(self) -> str:
    buf = os.read(self.rf, 1024)
    self.buf = buf.decode()
    logging.debug('received {0} bytes: {1}'.format(len(self.buf), self.buf))
    return self.buf

  def send(self, buf: str):
    logging.debug('send {0} bytes: {1}'.format(len(buf), buf))
    os.write(self.wf, buf.encode())
    time.sleep(0.01)

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
