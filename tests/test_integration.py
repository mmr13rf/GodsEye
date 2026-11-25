import os

def test_layers_exist():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    layers = os.path.join(base, "layers")
    engines = os.path.join(base, "engines")
    assert os.path.isdir(layers)
    assert os.path.isdir(engines)
    for i in range(11):
        assert os.path.isdir(os.path.join(layers, f"L{i}"))
    for i in range(1, 12):
        assert os.path.isdir(os.path.join(engines, f"D{i}"))

def test_docs_exist():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs = os.path.join(base, "docs")
    assert os.path.isdir(docs)
    for i in range(12):
        assert os.path.isfile(os.path.join(docs, f"PHASE{i}.md"))
