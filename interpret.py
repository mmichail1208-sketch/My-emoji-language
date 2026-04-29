
import pytest
from my import interpret
def test_i():
    assert interpret("👍 🤖") == chr(1)
    assert interpret("👍" * 65 + "🤖") == "A"
def test_d():
    assert interpret("👍" * 10 + "👎" * 3 + "🤖") == chr(7)
def test_move_rt():
    assert interpret("👍" * 65 + "👉" + "👍" * 66 + "👈" + "🤖") == "B"
def test_move_l():
    assert interpret("👉" + "👍" * 65 + "👈" + "🤖") == "A"
def test_output_c():
    assert interpret("👍" * 72 + "🤖") == "H"
def test_output_n():
    assert interpret("👍" * 42 + "🔢") == "42 "

def test_simple_lo():
    assert interpret("👍" * 5 + "▶ 👎 ◀ 🔢") == "0 "
def test_nested_loo():
    assert interpret("👍" * 3 + "▶ 👉 👍" * 2 + "👈 👎 ◀ 👉 🔢") == "6 "
