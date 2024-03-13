from main import turno_jogador

def test_turno_jogador():
 result = turno_jogador(1, 100)
 assert(1 <= result <= 100)

def test_verificar_vencedor_numero_certo():
    resultado, mensagem = verificar_vencedor("Teste", 42, 42, [])
    assert resultado == True
    assert mensagem == ""

def test_verificar_vencedor_numero_menor():
    resultado, mensagem = verificar_vencedor("Teste", 42, 41, [])
    assert resultado == False
    assert mensagem == "Teste, seu palpite é menor que o número secreto. Tente novamente!"

def test_verificar_vencedor_numero_maior():
    resultado, mensagem = verificar_vencedor("Teste", 42, 43, [])
    assert resultado == False
    assert mensagem == "Teste, seu palpite é maior que o número secreto. Tente novamente!"
