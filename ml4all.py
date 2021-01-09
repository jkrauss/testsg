# projects
# projects contain metadata about input and output files
# projects contain models and model configurations
# projects have a version number that is incremented on each save command
# FUTURE: Using git projects might also contain the files themselves

# commands
# commands are everything a user can do
# commands ands their parameters are by default put onto an undo stack
# the undo command undoes the command on top of the stack
# and puts it onto the redo stack

import json
import os.path


# INITIALIZE THE MODULE: undo and redo stack, STOREFILE and store
undo = []
redo = []
STORE_FILE = 'ml4all_store.json'


def save_store():
    with open(STORE_FILE, 'w') as out:
        json.dump(store, out)


def read_store():
    if os.path.isfile(STORE_FILE):
        with open('ml4all_store.json') as f:
            store = json.load(f)
    else:
        store = {}
    return store


store = read_store()
save_store()


class Project:
    def __init__(self, name):
        super().__init__()
        self.name = name
        if name in store:
            self.input = store['name']['input']
            self.output = store['name']['output']
            self.models = store['name']['models']
            self.version = store['name']['version']
        else:
            self.input = {}
            self.output = {}
            self.models = {}
            self.version = 0
            self.save(self, increase_version=False)

    def __del__(self):
        del store[self.name]
        save_store()

    def save(self, increase_version=True):
        if increase_version:
            self.version += 1
        store[self.name] = {
            'input': self.input,
            'output': self.output,
            'models': self.models,
            'version': self.version,
        }
        save_store()


class Command:
    def __init__(self, command, undo):
        super(self).__init__(self)
        self.command = command
        self.undo = undo


if __name__ == "__main__":
    pass
