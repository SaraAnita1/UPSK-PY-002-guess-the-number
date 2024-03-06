import sys
sys.path.insert(0, '../src/main.py')


def test_turno_jogador_return_input_number():
  actual_result = turno_jogador(0-100)

  assert actual_result == 0 - 100