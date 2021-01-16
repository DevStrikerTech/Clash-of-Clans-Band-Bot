from threading import Thread


class CreateTask(Thread):
    def __init__(self, object):
        Thread.__init__(self)
        self.method = object['method']
        self.parameters = object['parameters']

        self.daemon = True
        self.active = True

        self.start()

    def run(self):
        while self.active:
            self.method(self.parameters)

    def stop(self):
        self.active = False
