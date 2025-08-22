class Paciente:
    numero = 0
    def __init__(self, nome, idade, sexo, cpf, historico):
        Paciente.numero += 1
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.numero = Paciente.numero
        self.__cpf = cpf
        self.__historico = historico


    def __str__(self):
        return (
            f"\nInformações do Paciente\n"
            f"Paciente Nº {Paciente.numero}\n"
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Sexo: {self.sexo}\n"
            f"CPF: {self.__cpf}\n"
            f"Histórico Médico: {self.__historico}\n"
        )


pacientes = []

print("Sistema de Cadastro de Pacientes\n")

while True:
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    sexo = input("Digite o sexo do paciente (M/F): ")
    cpf = input("Digite o CPF do paciente: ")
    historico = input("Digite o histórico médico: ")


    paciente = Paciente(nome, idade, sexo, cpf, historico)
    pacientes.append(paciente)


    continuar = input("Deseja cadastrar outro paciente? (s/n): ")
    if continuar.lower() != "s":
        break

print("\n Lista de Pacientes Cadastrados")
for p in pacientes:
    print(p)
