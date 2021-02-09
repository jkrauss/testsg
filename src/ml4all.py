# projects
# projects contain metadata about input and output files
# projects contain models and model configurations
# projects have a version number that is incremented on each save command
# FUTURE: Using git projects might also contain the files themselves

# commands
# commands are everything a user can do
# commands and their parameters are by default put onto the undo stack
# the undo command undoes the command on top of the stack [-1]
# and puts it onto the redo stack (append)
# for every command the last parameter needs be undo=False
# for every command 'foo' there needs to be a '_foo_undo'
# When a command is called with undo=True it excecutes it's _command_undo

import json
import os.path
import pandas as pd
import os
import ml4all as ml


# INITIALIZE THE MODULE: STOREFILE and store
_STORE_FILE = os.path.join(os.getcwd(), 'ml4all_store.json')


def _save_store():
    with open(_STORE_FILE, 'w') as out:
        json.dump(store, out)


def _read_store():
    if os.path.isfile(_STORE_FILE):
        with open('ml4all_store.json') as f:
            store = json.load(f)
    else:
        store = {}
    return store


store = _read_store()
_save_store()


class Project:
    """
    Project contains lists of input, output, models, version, undo, redo
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
        if name in store:
            self.input = store[name]['input']
            self.input_frames = {}
            self.output = store[name]['output']
            self.models = store[name]['models']
            self.version = store[name]['version']
            self._undo = store[name]['undo']
            self._redo = store[name]['redo']
        else:
            self.input = {}
            self.input_frames = {}
            self.output = {}
            self.models = {}
            self.version = 0
            self._undo = []
            self._redo = []
            self.save(increase_version=False)

    def __del__(self):
        del store[self.name]
        _save_store()

    def save(self, increase_version=True):
        """
        save current project
        """
        if increase_version:
            self.version += 1
        store[self.name] = {
            'input': self.input,
            'output': self.output,
            'models': self.models,
            'version': self.version,
            'undo': self._undo,
            'redo': self._redo,
        }
        _save_store()

    def undo(self):
        """
        undo last operation
        """
        func, params = self._undo[-1]
        func(*params, undo=True)

    def redo(self):
        """
        redo last undone operation
        """
        func, params = self._redo[-1]
        self._redo.pop(-1)
        func(*params)

    def load_input(self, fname, undo=False):
        """
        load input from csv, xls, xlsx to project
        """
        if undo:
            return self._load_input_undo(fname)
        else:
            ext = fname.split('.')[-1]
            if ext in ('xls', 'xlsx'):
                self.input_frames[fname] = pd.read_excel(fname)
                self.input[fname] = "foo" #self.input_frames[fname].describe().to_json()
                r = "Excel-file successfully loaded"
            elif ext == 'csv':
                self.input_frames[fname] = pd.read_csv(fname)
                self.input[fname] = "bar" #self.input_frames[fname].describe().to_json()
                r = "csv-file successfully loaded"
            else:
                r = "Can't read file, supported extensions are csv, xls, xlsx"
            self._undo.append((self.load_input, [fname]))
            return r

    def _load_input_undo(self, fname):
        self.input.pop(fname)
        self.input_frames.pop(fname)
        self._redo.append((self.load_input, [fname]))
        self._undo.pop(-1)
        return "Load input successfully undone"


    def combine_inputs(self, left, right=[],undo=False):
        """
        combine set of inputs, based on given map to one target entity
        """
        if undo:
            return self._combine_inputs_undo(left, right)
    
    def _combine_inputs_undo(self, left, right):
        pass

    def map_inputs(self, inputs=[],undo=False):
        """
            create a map of dependencies between inputs
        """
        if undo:
            return self._map_inputs_undo(inputs)
    
    def _map_inputs_undo(self, inputs):
        pass

    def model_train(self, input, target, type='classifier', undo=False):
        """
        train a model based on input, predict target
        type: in ('classifier', 'regressor', 'deduper')
        """
        if undo:
            return self._model_train_undo(input, target, type)
    
    def _model_train_undo(self, input, target, type):
            pass

    def model_produce(self, model, input, target, type='classifier', undo=False):
        """
        predict target using a given model on input data
        type: in ('classifier', 'regressor', 'deduper')
        """
        if undo:
            return self._model_produce_undo(input, target, type)
    
    def _model_produce_undo(self, model, input, target, type):
        pass

if __name__ == "__main__":
    import ml4all as ml
    p=ml.Project('test')
    p.load_input('data/input/clv.xlsx')
    print('foo')
    print(p.input.keys())
