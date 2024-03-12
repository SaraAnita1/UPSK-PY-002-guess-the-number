from main import turno_jogador

def test_turno_jogador():
 result = turno_jogador(1, 100)
 assert(1 <= result <= 100)