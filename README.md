# 🏦 Sistema Bancário - Desafio DIO

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Sobre o Projeto

Sistema bancário desenvolvido como parte do desafio da **Digital Innovation One (DIO)**, aplicando conceitos de **Programação Orientada a Objetos (POO)** em Python.

O projeto demonstra a refatoração de um sistema procedural para uma arquitetura orientada a objetos, seguindo boas práticas de design e implementando classes conforme modelo UML.

## ✨ Características

- ✅ **100% POO**: Uso de classes e objetos (sem dicionários para armazenar dados)
- 🏗️ **Arquitetura Modular**: Classes bem definidas e separação de responsabilidades
- 📊 **Herança e Polimorfismo**: Subclasses `ContaCorrente` e `ContaPoupanca`
- 🔒 **Encapsulamento**: Métodos próprios para operações bancárias
- 🧪 **Testes Automatizados**: Scripts de teste não interativos

## 🎯 Funcionalidades

- Cadastro de usuários (clientes)
- Criação de contas bancárias
- Operações de depósito
- Operações de saque com validações:
  - Limite de valor por saque
  - Limite de quantidade de saques diários
  - Validação de saldo
- Extrato detalhado de movimentações
- Listagem de contas cadastradas

## 🏗️ Arquitetura

### Diagrama de Classes (UML)

```
┌─────────────────┐
│    Usuario      │
├─────────────────┤
│ - nome          │
│ - cpf           │
│ - data_nasc     │
│ - endereco      │
└─────────────────┘
         △
         │
         │
┌────────┴────────┐
│     Conta       │
├─────────────────┤
│ - agencia       │
│ - numero        │
│ - titular       │
│ - saldo         │
│ - extrato[]     │
│ - limite        │
├─────────────────┤
│ + depositar()   │
│ + sacar()       │
│ + exibir_ext()  │
└─────────────────┘
    △         △
    │         │
    │         └──────────────┐
    │                        │
┌───┴──────────┐   ┌────────┴────────┐
│ContaCorrente │   │ ContaPoupanca   │
└──────────────┘   └─────────────────┘
```

### Estrutura de Arquivos

```
Exe006/
├── desafio_DIO.py           # Código principal com todas as classes
├── test_desafio.py          # Testes básicos
├── test_desafio_extra.py    # Testes avançados (subclasses)
└── README.md                # Documentação
```

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- Nenhuma dependência externa necessária

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Patrick-Lima-DEV/Desafio-DIO_.git
cd Desafio-DIO_
```

### Execução

#### Modo Interativo (Menu):
```bash
python desafio_DIO.py
```

O sistema apresentará um menu com as seguintes opções:
- `[d]` Depositar
- `[s]` Sacar
- `[e]` Extrato
- `[nc]` Nova conta
- `[lc]` Listar contas
- `[nu]` Novo usuário
- `[q]` Sair

#### Modo de Testes Automatizados:
```bash
# Teste básico
python test_desafio.py

# Testes avançados (ContaCorrente e ContaPoupanca)
python test_desafio_extra.py
```

## 💡 Exemplos de Uso

### Criando Usuário e Conta Programaticamente

```python
from desafio_DIO import Banco, Usuario, ContaCorrente

# Instanciar banco
banco = Banco()

# Criar usuário
usuario = Usuario(
    nome="João Silva",
    data_nascimento="15-05-1990",
    cpf="12345678900",
    endereco="Rua ABC, 123 - Centro - São Paulo/SP"
)
banco.usuarios.append(usuario)

# Criar conta corrente
conta = ContaCorrente(banco.agencia_default, 1, usuario)
banco.contas.append(conta)

# Realizar operações
conta.depositar(1000.0)
conta.sacar(250.0)
conta.exibir_extrato()
```

### Diferenças entre Tipos de Conta

```python
# Conta Corrente: até 3 saques por dia
cc = ContaCorrente("0001", 1, usuario)
cc.depositar(500)
cc.sacar(100)  # OK
cc.sacar(100)  # OK
cc.sacar(100)  # OK
cc.sacar(100)  # ERRO: limite de saques atingido

# Conta Poupança: apenas 1 saque por dia
cp = ContaPoupanca("0001", 2, usuario)
cp.depositar(500)
cp.sacar(100)  # OK
cp.sacar(100)  # ERRO: limite de saques atingido
```

## 🧪 Testes

### Resultado dos Testes

```bash
$ python test_desafio.py
=== Depósito realizado com sucesso! ===
=== Saque realizado com sucesso! ===
@@@ Operação falhou! Você não tem saldo suficiente. @@@

================ EXTRATO ================
Depósito:       R$ 200.00
Saque:          R$ 50.00

Saldo:          R$ 150.00
==========================================

Teste automatizado concluído com sucesso.
```

## 📚 Conceitos Aplicados

- **POO**: Classes, objetos, herança, encapsulamento
- **Dataclasses**: Uso de `@dataclass` para simplificar a classe `Usuario`
- **Type Hints**: Anotações de tipo para melhor legibilidade
- **Docstrings**: Documentação inline das classes
- **Clean Code**: Código limpo e bem estruturado

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Patrick Lima**

- GitHub: [@Patrick-Lima-DEV](https://github.com/Patrick-Lima-DEV)

## 🎓 Agradecimentos

- [Digital Innovation One (DIO)](https://www.dio.me/) - Pelo desafio e conteúdo educacional
- Comunidade Python Brasil

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
