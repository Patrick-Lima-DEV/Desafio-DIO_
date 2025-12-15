from desafio_DIO import Banco, Usuario, ContaCorrente, ContaPoupanca


def run_extra_tests():
    banco = Banco()

    # Usuários
    u1 = Usuario(nome="Ana", data_nascimento="02-02-1992", cpf="11122233344", endereco="Rua A, 1")
    u2 = Usuario(nome="Bruno", data_nascimento="03-03-1993", cpf="55566677788", endereco="Rua B, 2")
    banco.usuarios.extend([u1, u2])

    # Contas: corrente e poupança
    cc = ContaCorrente(banco.agencia_default, 1, u1)
    cp = ContaPoupanca(banco.agencia_default, 2, u2)
    banco.contas.extend([cc, cp])

    # Operações na conta corrente
    cc.depositar(500)
    cc.sacar(100)

    # Operações na poupança: permite um saque apenas
    cp.depositar(300)
    cp.sacar(100)  # primeiro saque ok
    cp.sacar(50)   # segundo saque deve falhar devido ao limite

    # Exibir extratos
    print('\n-- Extrato Conta Corrente --')
    cc.exibir_extrato()

    print('\n-- Extrato Conta Poupanca --')
    cp.exibir_extrato()

    print('\nTestes extras concluídos.')


if __name__ == '__main__':
    run_extra_tests()
