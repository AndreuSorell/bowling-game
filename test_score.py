from bowling_score import Bowling

simple_score = Bowling('9-9-9-9-9-9-9-9-9-9-')
simple_score2 = Bowling('9-9-9-9-9-9-9-9-9-8-')
simple_score3 = Bowling('72729-9-9-9-9-9-9-72')
simple_score4 = Bowling('9-3561368153258-7181')
simple_score5 = Bowling('12345123451234512345')

def test_simple():
    assert 90 == simple_score.punctuation()
    assert 89 != simple_score.punctuation()
    assert 89 == simple_score2.punctuation()
    assert 90 == simple_score3.punctuation()
    assert 82 == simple_score4.punctuation()
    assert 60 == simple_score5.punctuation()

score_spares1 = Bowling('5/5/5/5/5/5/5/5/5/5/5')
score_spares2 = Bowling('9-3/613/815/-/8-7/8/8')

def test_pins_with_spares():
    assert 150 == score_spares1.punctuation()
    assert 131 == score_spares2.punctuation()

def test_with_strikes():
    assert 100 == Bowling('X9-9-9-9-9-9-9-9-9-').punctuation()
    assert 100 == Bowling('9-9-9-9-9-9-9-9-9-X9-').punctuation()
    assert 110 == Bowling('X9-X9-9-9-9-9-9-9-').punctuation()
    assert 120 == Bowling('XX9-9-9-9-9-9-9-9-').punctuation()
    assert 141 == Bowling('XXX9-9-9-9-9-9-9-').punctuation()
    assert 111 == Bowling('9-9-9-9-9-9-9-9-9-XXX').punctuation()
    assert 300 == Bowling('XXXXXXXXXXXX').punctuation()

def test_spares_and_strikes():
    assert 136 == Bowling('62X71548-X1/8-7/X9-').punctuation()
    assert 154 == Bowling('8/X9-XX5/53639/9/-').punctuation()
    assert 94 == Bowling('--337-7/9-X-57-9-9/7').punctuation()
    assert 175 == Bowling('X5/X5/XX5/--5/X5/').punctuation()
    assert 149 == Bowling('8/549-XX5/53639/9/X').punctuation()