from taskmanager.tache import Tache


def test_tache_creation():
    t = Tache("A", 3, [])
    assert t.id == "A"
    assert t.duree == 3
    assert t.prealables == []
    assert t.debut is None
    assert t.fin is None

def test_set_debut():
    t = Tache("B", 4, ["A"])
    t.set_debut(2)
    assert t.debut == 2
    assert t.fin == 6  # 2 + 4
