def test_len():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, f"Length must be < 15"

