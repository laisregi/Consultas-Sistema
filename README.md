# Sistema de Clínica de Consultas

## Visão Geral do Problema

Este programa é um sistema básico para gerenciar o cadastro de pacientes e o agendamento de consultas médicas em uma clínica.

## Design da Solução

O sistema consiste em três principais funcionalidades:
- Cadastro de pacientes
- Marcação de consultas
- Cancelamento de consultas

O programa é estruturado em funções principais que são chamadas a partir de um menu interativo.

## Decisões de Projeto

- **Validação de Telefone**: Implementei uma função simples `validar_telefone` para garantir que os números de telefone sejam válidos antes de cadastrar um paciente.
- **Uso de `datetime`**: Utilizei a biblioteca `datetime` do Python para validar e manipular datas e horas das consultas.
- **Interface do Usuário**: Optei por um menu de texto simples para facilitar a interação do usuário com o sistema.

## Dependências

- Python 3.x (bibliotecas padrão: `os`, `datetime`)

