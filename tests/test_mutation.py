import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fuzzer.inputs.mutation import mutate


def test_mutation_changes_input():
    original = b"GET / HTTP/1.1\r\n\r\n"
    mutated = mutate(original, num_mutations=5)
    assert mutated != original
    assert isinstance(mutated, bytes)
