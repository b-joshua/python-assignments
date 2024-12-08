from seq import count_bases

def test_counter_As():
    res = count_bases("AAAA")
    assert res == {"A": 4, "C": 0, "G": 0, "T": 0, "Unknown": 0}

def test_counter_mix():
    res = count_bases("ACGTAGCT")
    assert res == {"A": 2, "C": 2, "G": 2, "T": 2, "Unknown": 0}

def test_counter_unknown():
    res = count_bases("ZZZZYYYY")
    assert res == {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 8}

def test_counter_none():
    res = count_bases("")
    assert res == {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}

print(test_counter_As(), test_counter_mix(), test_counter_unknown(), test_counter_none())