import pytest
from my import interpret
def test_increment():
    assert interpret("👍 🤖") == chr(1)
def test_decrement():
    assert interpret("👍 👍 👍 👍 👍 👍 👍 👍 👍 👍 👎 👎 👎 🤖") == chr(7)
def test_move_right():
    assert interpret("👍 " * 65 + "👉 " + "👍 " * 66 + "👈 🤖") == "B"
def test_move_left():
    assert interpret("👉 👍 " * 65 + "👈 🤖") == "A"
def test_output_char():
    assert interpret("👍 " * 72 + "🤖") == "H"
def test_output_number():
    assert interpret("👍 " * 42 + "🔢") == "42"
def test_input_number():
    import builtins
    original = builtins.input
    builtins.input = lambda _: "42"
    result = interpret("⏬ 🔢")
    builtins.input = original
    assert result == "42"
def test_loop():
    assert interpret("👍 👍 👍 👍 👍 😂 👎 😭 🔢") == "0"
def test_nested_loops():
    assert interpret("👍 👍 👍 👍 👍 😂 👎 😂 👎 😭 😭 🔢") == "0"
