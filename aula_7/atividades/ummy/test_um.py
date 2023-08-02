from um import count

def test_if_um():
    assert count('um, testando ,um umdois umido um...') == 3
    assert count('umido') == 0
    assert count('...um...dois...um...ai') == 2