from desafio_DIO import Banco, Usuario, Conta


def run_test():
    banco = Banco()

    # Criar usuário e conta programaticamente
    usuario = Usuario(nome="Fulano de Tal", data_nascimento="01-01-1990", cpf="00011122233", endereco="Rua Teste, 123")
    banco.usuarios.append(usuario)

    conta = Conta(banco.agencia_default, 1, usuario)
    banco.contas.append(conta)

    # Operações
    conta.depositar(200.0)
    conta.sacar(50.0)
    conta.sacar(1000.0)  # saque acima do saldo -> deve falhar

    # Exibir extrato
    conta.exibir_extrato()

    print("\nTeste automatizado concluído com sucesso.")


if __name__ == '__main__':
    run_test()
