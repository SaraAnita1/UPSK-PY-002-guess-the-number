from main import turno_jogador


def test_turno_jogador_return_input_number():
  actual_result = turno_jogador(0-100)

  assert actual_result == 0 - 100