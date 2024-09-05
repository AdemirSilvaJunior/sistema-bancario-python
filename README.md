# 💻 Sistema Bancário em Python

### 🚀 Descrição
Este é um sistema bancário simples desenvolvido em Python que permite realizar operações básicas, como **depósitos**, **saques** e **consultar extratos**. Ele foi criado como parte de um projeto prático para aprimorar habilidades de programação e lógica.

### 🛠️ Funcionalidades
- **Depositar**: Adiciona valores ao saldo da conta.
- **Sacar**: Realiza até 3 saques diários, com limite de R$ 500 por saque.
- **Extrato**: Exibe todas as transações realizadas (depósitos e saques) e o saldo atual.
- **Consultar Saldo**: Permite ao usuário visualizar o saldo sem precisar acessar o extrato completo.
- **Reiniciar Conta**: Restaura o saldo e o histórico de transações para o valor inicial (R$ 0,00).

### 📋 Regras do Sistema
- O **depósito** só aceita valores positivos.
- O **saque** está sujeito às seguintes regras:
  - O valor do saque não pode ser maior que o saldo disponível.
  - O valor do saque não pode exceder o limite de R$ 500 por operação.
  - Limite de **3 saques diários**.
- O **extrato** lista todas as operações e exibe o saldo no formato `R$xxx,xx`.
- Bônus aleatório ao atingir R$1000,00 de saldo! 💰

### 📦 Instalação e Execução
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/sistema-bancario-python.git

2. Navegue até o diretório do projeto:
   ```bash
   cd sistema-bancario-python

3. Execute o arquivo Python:
   ```bash
   python sistema_bancario.py

## 🔧 Tecnologias Utilizadas
- **Python 3.x**

## 🏆 Desafio
Este projeto foi desenvolvido como parte da [Formação Python Developer](https://www.dio.me/) na DIO (Digital Innovation One), com o objetivo de praticar a criação de sistemas com lógica de negócio e estrutura de controle de fluxo.

## 👨‍💻 Autor
- **Seu Nome**  
  Conecte-se comigo no [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ademir-silva-junior) e veja mais projetos no meu [![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github&logoColor=white)](https://github.com/AdemirSilvaJunior).
