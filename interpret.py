import pytest
from my import interpret
def test_increment():  # 👍
    assert interpret("👍 🤖") == chr(1)
def test_decrement():  # 👎
    assert interpret("👍" * 10 + "👎" * 3 + "🤖") == chr(7)
def test_move_right():  # 👉
    assert interpret("👍" * 65 + "👉" + "👍" * 66 + "👈" + "🤖") == "B"
def test_move_left():  # 👈
    assert interpret("👉" + "👍" * 65 + "👈" + "🤖") == "A"
def test_output_char():  # 🤖
    assert interpret("👍" * 72 + "🤖") == "H"
def test_output_number():  # 🔢
    assert interpret("👍" * 42 + "🔢") == "42"
def test_input_number(x:  # ⏬
    x.setattr('builtins.input', lambda _: "42")
    assert interpret("⏬ 🔢") == "42"
def test_loop_start_end():  # 😂 и 😭 (цикл)
    assert interpret("👍" * 5 + "😂 👎 😭 🔢") == "0"
def test_old_loop_start(monkeypatch):  # ▶ 
    assert interpret("👍" * 3 + "▶ 👎 ◀ 🔢") == "0"
def test_old_loop_end(monkeypatch):  # ◀ 
    assert interpret("👍" * 3 + "▶ 👎 ◀ 🔢") == "0"
