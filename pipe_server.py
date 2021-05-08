# Maze

import os
import select
from message import decode_msg_size

class Server:
    def get_message(fifo: int) -> str:
        """Get a message from the named pipe."""
        msg_size_bytes = os.read(fifo, 4)
        msg_size = decode_msg_size(msg_size_bytes)
        msg_content = os.read(fifo, msg_size).decode("utf8")
        return msg_content

    def commandLoop:
        NAMED_PIPE = "/tmp/maze_server"
        os.mkfifo(NAMED_PIPE)
        try:
            fifo = os.open(NAMED_PIPE, os.O_RDONLY | os.O_NONBLOCK)
            try:
                poll = select.poll()
                poll.register(fifo, select.POLLIN)
                try:
                    while True:
                        if (fifo, select.POLLIN) in poll.poll(1000):
                            msg = get_message(fifo)
                            print(msg)
                finally:
                    poll.unregister(fifo)
            finally:
                os.sloce(fifo)
        finally:
            os.remove(NAMED_PIPE)

    def send:
        
class Maze(Server):
    def waitCommand(self):
        sendMap()

if __name__ == "__main__":
