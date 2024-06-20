import os
from datetime import datetime

def mostrar_menu():
    print("\nMenu de Consultas")
    print("1. Cadastrar um paciente")
    print("2. Marcações de consultas")
    print("3. Cancelamento de consultas")
    print("4. Sair")

def cadastrar_paciente(pacientes_cadastrados):
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone: ")

    if not validar_telefone(telefone):
        print("Telefone inválido. O telefone deve conter apenas números e ter pelo menos 8 dígitos.")
        return

    for paciente in pacientes_cadastrados:
        if paciente['telefone'] == telefone:
            print("Paciente já cadastrado!")
            return
        
    
    pacientes_cadastrados.append({"nome": nome, "telefone": telefone})
    print("Paciente cadastrado com sucesso!")

def validar_telefone(telefone):
    telefone = telefone.strip()
    if telefone.isdigit() and len(telefone) >= 8:
        return True
    else:
        return False

def marcacao_consulta(lista_agendamentos, pacientes_cadastrados):
    os.system('cls' if os.name == 'nt' else 'clear')
    if not pacientes_cadastrados:
        print("Nenhum paciente cadastrado. Cadastre um paciente primeiro.")
        return
    
    for indice, paciente in enumerate(pacientes_cadastrados, 1):
        print(f"{indice}. {paciente['nome']}")

    num_paciente = input('Escolha o número correspondente ao paciente: ')
    try:
        num_paciente_int = int(num_paciente)
        if 1 <= num_paciente_int <= len(pacientes_cadastrados):
            paciente = pacientes_cadastrados[num_paciente_int - 1]
            data = input("Digite a data da consulta (dd/mm/aaaa): ")
            hora = input("Digite a hora da consulta (hh:mm): ")
            especialidade = input("Especialidade: ")

            try:
                data_hora_consulta = datetime.strptime(f"{data} {hora}", "%d/%m/%Y %H:%M")
                if data_hora_consulta < datetime.now():
                    print("Não é possível agendar consultas retroativas.")
                    return
            except ValueError:
                print("Formato de data ou hora inválido.")
                return

            for agendamento in lista_agendamentos:
                if agendamento['data'] == data and agendamento['hora'] == hora:
                    print("Este horario está indisponível, tente outro.")
                    return
                
        
            lista_agendamentos.append({"paciente": paciente["nome"], "data": data, "hora": hora, "especialidade": especialidade})
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Consulta agendada com sucesso!")
        else:
            print('Este paciente não existe.')
    except ValueError:
            print('Entrada inválida. Por favor, insira um número.')
    except Exception:
            print('Erro desconhecido')   

def cancelamento_consultas(lista_agendamentos):
    os.system('cls' if os.name == 'nt' else 'clear')
    if not lista_agendamentos:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nenhuma consulta foi agendada.")
        return

    for indice, agendamento in enumerate(lista_agendamentos, 1):
        print(f"{indice}. Paciente: {agendamento['paciente']} - Data: {agendamento['data']} - Hora: {agendamento['hora']} - Especialidade: {agendamento['especialidade']}")
    
    num_consulta = input("Escolha o número da consulta a ser cancelada: ")
    try:
        num_consulta_int = int(num_consulta)
        if 1 <= num_consulta_int <= len(lista_agendamentos):
            agendamento = lista_agendamentos[num_consulta_int - 1]
            print(f"Consulta selecionada: \nPaciente: {agendamento['paciente']}\nData: {agendamento['data']}\nHora: {agendamento['hora']}\nEspecialidade: {agendamento['especialidade']}")
            confirmacao = input("Deseja cancelar esta consulta? (s/n): ")

            if confirmacao.lower() == "s":
                lista_agendamentos.pop(num_consulta_int - 1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Consulta cancelada com sucesso.")
            else:
                print("Cancelamento de consulta abortado.")
        else:
            print('Número de Consulta inválido.')
    except ValueError:
            print('Entrada inválida. Por favor, insira um número.')
    except Exception:
            print('Erro desconhecido')  

def main():
    pacientes_cadastrados = []
    lista_agendamentos = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastrar_paciente(pacientes_cadastrados)
        elif escolha == "2":
            marcacao_consulta(lista_agendamentos, pacientes_cadastrados)
        elif escolha == "3":
             cancelamento_consultas(lista_agendamentos)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()