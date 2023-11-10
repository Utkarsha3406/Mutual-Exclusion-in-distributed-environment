from threading import Thread, Lock
import time
import random
import sys
import queue

class Process:
    def __init__(self, process_id, num_processes, shared_lock, request_queue, reply_queue):
        self.process_id = process_id
        self.num_processes = num_processes
        self.shared_lock = shared_lock
        self.request_queue = request_queue
        self.reply_queue = reply_queue
        self.requesting = False
        self.replies_received = 0

    def request_cs(self):
        self.requesting = True
        self.replies_received = 0

        with self.shared_lock:
            timestamp = time.time()
            self.request_queue.put((self.process_id, timestamp))
            print(f"Process {self.process_id} requested the critical section at time {timestamp}")

    def release_cs(self):
        self.requesting = False
        with self.shared_lock:
            print(f"Process {self.process_id} released the critical section")

    def handle_requests(self):
        while True:
            with self.shared_lock:
                if self.requesting:
                    self.requesting = False
                    self.reply_queue.put(self.process_id)

    def run(self):
        request_handler_thread = Thread(target=self.handle_requests)
        request_handler_thread.daemon = True
        request_handler_thread.start()

        while True:
            # Simulate some computation before requesting the critical section
            time.sleep(random.uniform(1, 3))
            self.request_cs()

            # Wait for replies from other processes
            while self.replies_received < self.num_processes - 1:
                reply = self.reply_queue.get()
                print(f"Process {self.process_id} received a reply from Process {reply}")
                self.replies_received += 1

            # Enter the critical section
            print(f"Process {self.process_id} is in the critical section")
            time.sleep(random.uniform(1, 3))

            # Release the critical section
            self.release_cs()

def main(num_processes, duration):
    shared_lock = Lock()
    request_queue = queue.Queue()
    reply_queue = queue.Queue()
    processes = []

    for i in range(num_processes):
        process = Process(i, num_processes, shared_lock, request_queue, reply_queue)
        processes.append(process)

    for process in processes:
        thread = Thread(target=process.run)
        thread.daemon = True
        thread.start()

    time.sleep(duration)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python distributed_mutual_exclusion.py <num_processes> <duration>")
        sys.exit(1)

    num_processes = int(sys.argv[1])
    duration = int(sys.argv[2])
    main(num_processes, duration)



