import ml4all as ml
import pandas as pd
import pytest

# coverage run --source=src -m pytest -s -v -ra
# coverage report -m

def test_initialization_ok():
    assert type(ml.store) is dict, "store should exist as a dict"
    sl = len(ml.store)
    ml.Project('foo')
    assert sl == len(ml.store), "An unreferenced object should be removed from store"
    p = ml.Project('foo3hr6')
    assert sl+1 == len(ml.store), "A referenced object should extend the store"
    assert ml.store['foo3hr6'], "The inserted project should be retrievabe from the store"
    p = None
    assert sl == len(ml.store), "a de-referenced object should be removed from store"
    #assert ml.Command(1, 2), "It should be possible to create a command"


def test_Project_creation_and_version():
    p = ml.Project('p1')
    assert p.name == 'p1', "name should be as initialized"
    assert type(p.input) is dict, "input should exist as a dict"
    assert type(p.output) is dict, "output should exist as a dict"
    assert type(p.models) is dict, "models should exist as a dict"
    assert type(p._redo) is list, "redo should exist as a list"
    assert type(p._undo) is list, "undo should exist as a list"
    assert p.version == 0, "initial version should be 0"
    p.save()
    p.save()
    p.save()
    assert p.version == 3, "save should increase version"
    p = None
    p = ml.Project('p1')
    assert p.version == 0, "initial version should be 0"


@pytest.fixture(scope="module")
def input_files():
    return [
    'data/input/clv.xlsx',
    'data/input/toy_sales.csv',
    # 'data/input/foo.html',
]

@pytest.mark.parametrize("f", input_files())
def test_load_input(f):
    # create project and setup
    p = ml.Project('baff')
    ul = len(p._undo)

    # load input and test
    p.load_input(f)
    assert ul+1 == len(p._undo), "executing a command should go onto undo stack"
    c = p._undo[-1]
    assert c[0] == p.load_input, "command name should match"
    assert c[1][0] == f, "command parameter should be correct"
    assert len(c[1]) == 1, "was exactly one parameter"
    assert f in p.input.keys(), "new key should be added to projects' inputs"
    assert isinstance(p.input[f], pd.DataFrame), "new dataframe should exist"

    # undo and test
    rl = len(p._redo)
    p.undo()
    assert ul == len(p._undo), "undoing command should reduce the undo stack"
    assert rl+1 == len(p._redo), "udoing command should increase redo stack"
    c = p._redo[-1]
    assert c[0] == p.load_input, "command name should match"
    assert c[1][0] == f, "command parameter should be correct"
    assert len(c[1]) == 1, "was exactly one parameter"
    assert f not in p.input.keys(), "new key should not be in projects' inputs"

    # redo and test
    ul = len(p._undo)
    rl = len(p._redo)
    p.redo()
    assert ul+1 == len(p._undo)
    assert rl-1 == len(p._redo)
    c = p._undo[-1]
    assert c[0] == p.load_input, "command name should match"
    assert c[1][0] == f, "command parameter should be correct"
    assert len(c[1]) == 1, "was exactly one parameter"
    assert f in p.input.keys(), "new key should be added to projects' inputs"
    assert isinstance(p.input[f], pd.DataFrame), "new dataframe should exist"

    p = None

#@pytest.mark.parametrize(input_files)
def test_map_inputs(input_files):

    p = ml.Project('xzk1')
    for f in input_files():
        p.load_input(f)

def test_combine_inputs():
    pass

def test_model_train():
    pass

def test_model_produce():
    pass