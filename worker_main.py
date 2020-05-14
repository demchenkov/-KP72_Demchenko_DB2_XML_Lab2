from worker.message_handler import MessageHandler
from worker.worker import WorkerInstance

if __name__ == '__main__':
    handler = MessageHandler()
    worker = WorkerInstance(handler)
    worker.run()
