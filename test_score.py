from bowling_score import Bolos

simple_score = Bolos('9-9-9-9-9-9-9-9-9-9-')
simple_score2 = Bolos('9-9-9-9-9-9-9-9-9-8-')
simple_score3 = Bolos('72729-9-9-9-9-9-9-72')
simple_score4 = Bolos('9-3561368153258-7181')
simple_score5 = Bolos('12345123451234512345')
no_simple_score = Bolos('9X9-9-9-9-9-9-9-9-9-')
no_simple_score2 = Bolos('9/9-9-9-9-9-9-9-9-9-')

def test_simple_pins():
    assert 90 == simple_score.simple_pins()
    assert 89 != simple_score.simple_pins()
    assert 89 == simple_score2.simple_pins()
    assert 90 == simple_score3.simple_pins()
    assert 82 == simple_score4.simple_pins()
    assert 60 == simple_score5.simple_pins()
    assert 'No es un calculo simple' == no_simple_score.simple_pins()
    assert 'No es un calculo simple' == no_simple_score2.simple_pins()

score_spares1 = Bolos('5/5/5/5/5/5/5/5/5/5/5')
score_spares2 = Bolos('9-3/613/815/-/8-7/8/8')

def test_pins_with_spares():
    assert 150 == score_spares1.score_bolos()
    assert 131 == score_spares2.score_bolos()

def test_with_strikes():
    assert 100 == Bolos('X9-9-9-9-9-9-9-9-9-').score_bolos()
    assert 100 == Bolos('9-9-9-9-9-9-9-9-9-X9-').score_bolos()
    assert 110 == Bolos('X9-X9-9-9-9-9-9-9-').score_bolos()
    assert 120 == Bolos('XX9-9-9-9-9-9-9-9-').score_bolos()
    assert 141 == Bolos('XXX9-9-9-9-9-9-9-').score_bolos()
    assert 111 == Bolos('9-9-9-9-9-9-9-9-9-XXX').score_bolos()
    assert 300 == Bolos('XXXXXXXXXXXX').score_bolos()

def test_spares_and_strikes():
    assert 149 == Bolos('8/549-XX5/53639/9/X').score_bolos()
