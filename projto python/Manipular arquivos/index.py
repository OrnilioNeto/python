from library import*


home = home_()
entrada = menu_()


if entrada == "X":
    filexlsx = input("Digite o nome do arquivo ")
    filexlsx = filexlsx + ".xlsx"
    df = pd.read_excel(filexlsx)
    print(filexlsx)
    sub = acao()

elif entrada == "E":
    print("Sessão encerrada com sucesso !")


if sub == "W":
    df = pd.read_excel(filexlsx)
    print(df)

    
if sub == "G":
    df["LojaID"].value_counts(ascending=True).plot.barh(title="Qnt_ID", color ="Blue")
    plt.ylabel("ID")
    plt.xlabel("Qtde");
    plt.legend()
    plt.show()

if sub == "I":
    pi = df.groupby(df["Data"].dt.year)["Qtde"].sum().plot.pie();
    plt.legend()
    plt.show()


if sub == "E":
    print("Sessão encerada com sucesso!")

if entrada == "C":
    filecsv = input("Digite o nome do arquivo ")
    filecsv = filecsv + ".csv"
    acao()
    print(filecsv)

if entrada == "J":
    filejson = input("Digite o nome do arquivo ")
    filejson = filejson + ".json"
    acao()
    print(filejson)