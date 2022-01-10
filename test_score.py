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

def test_pins_with_spares():
    assert 150 == score_spares1.pins_with_spares()

