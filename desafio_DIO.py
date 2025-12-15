import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

import textwrap
from dataclasses import dataclass


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


@dataclass
class Usuario:
    nome: str
    data_nascimento: str
    cpf: str
    endereco: str


class Conta:
    def __init__(self, agencia: str, numero: int, titular: Usuario, limite: float = 500.0):
        self.agencia = agencia
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []
        self.limite = limite
        self.numero_saques = 0
        self.limite_saques = 3

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito:\tR$ {valor:.2f}")
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor: float):
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return

        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return

        if valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return

        if self.numero_saques >= self.limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return

        self.saldo -= valor
        self.extrato.append(f"Saque:\t\tR$ {valor:.2f}")
        self.numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for linha in self.extrato:
                print(linha)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")


class ContaCorrente(Conta):
    """Conta corrente: herda comportamento padrão de Conta."""
    pass


class ContaPoupanca(Conta):
    """Conta poupança: permite apenas um saque por dia (simulado via limite_saques=1)."""
    def __init__(self, agencia: str, numero: int, titular: Usuario, limite: float = 500.0):
        super().__init__(agencia, numero, titular, limite)
        self.limite_saques = 1


class Banco:
    def __init__(self, agencia_default: str = "0001"):
        self.usuarios: list[Usuario] = []
        self.contas: list[Conta] = []
        self.agencia_default = agencia_default

    def filtrar_usuario(self, cpf: str):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        if self.filtrar_usuario(cpf):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuario = Usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        self.usuarios.append(usuario)
        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            numero_conta = len(self.contas) + 1
            conta = Conta(self.agencia_default, numero_conta, usuario)
            self.contas.append(conta)
            print("\n=== Conta criada com sucesso! ===")
            return

        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return

        for conta in self.contas:
            linha = f"""\
Agência:\t{conta.agencia}
C/C:\t\t{conta.numero}
Titular:\t{conta.titular.nome}
"""
            print("=" * 100)
            print(textwrap.dedent(linha))

    def buscar_conta(self, numero: int):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None


def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "d":
            try:
                numero = int(input("Informe o número da conta: "))
            except ValueError:
                print("Número de conta inválido.")
                continue

            conta = banco.buscar_conta(numero)
            if not conta:
                print("Conta não encontrada.")
                continue

            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("Valor inválido.")
                continue

            conta.depositar(valor)

        elif opcao == "s":
            try:
                numero = int(input("Informe o número da conta: "))
            except ValueError:
                print("Número de conta inválido.")
                continue

            conta = banco.buscar_conta(numero)
            if not conta:
                print("Conta não encontrada.")
                continue

            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("Valor inválido.")
                continue

            conta.sacar(valor)

        elif opcao == "e":
            try:
                numero = int(input("Informe o número da conta: "))
            except ValueError:
                print("Número de conta inválido.")
                continue

            conta = banco.buscar_conta(numero)
            if not conta:
                print("Conta não encontrada.")
                continue

            conta.exibir_extrato()

        elif opcao == "nu":
            banco.criar_usuario()

        elif opcao == "nc":
            banco.criar_conta()

        elif opcao == "lc":
            banco.listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()