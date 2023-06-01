import uteis


def header(msg):
    print("-" * 40)
    print(f"{msg :^40}")
    print("-" * 40)


def fileExists(name):
    try:
        with open(name, "r", encoding="utf-8"):
            return True
    except (FileNotFoundError, IOError):
        return False


while True:
    header("Menu Principal")
    print("1- Ver pessoas cadastradas\n2- Cadastrar novas pessoas\n3- Sair do sistema")
    opt = uteis.lerOption("Sua opção: ", 3)

    if opt == 1:
        header("Pessoas cadastradas")
        if not fileExists("cadastro.txt"):
            print("Não existe pessoas cadastradas ainda.\n")
            continue

        print("Nº".ljust(3), end="")
        print("Nome:".ljust(30), end="")
        print("Idade:")
        with open("cadastro.txt", "r", encoding="utf-8") as file:
            for i, v in enumerate(file, start=1):
                print(str(i).ljust(3), end="")
                v = v.split(";")
                print(v[0].ljust(30), end=" ")
                print(v[1], end="")

    elif opt == 2:
        header("Cadastrar pessoa")
        created = fileExists("cadastro.txt")

        name = uteis.lerString("Nome: ").capitalize()
        age = uteis.lerInteiro("Idade: ", "Idade inválida")
        access = "a" if created else "w"

        with open("cadastro.txt", access, encoding="utf-8") as file:
            file.write(f"{name};{age}\n")

        print(f"{name} cadastrado com sucesso")

    else:
        header("Saindo do sistema ...")
        break
