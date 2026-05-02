import os
import requests
from bs4 import BeautifulSoup


import pandas as pd

url = "https://www.formula1.com/en/results.html"

print(
    "\n\t\t=================== Historical Results - F1 Automation ===================\n Welcome to the Result Verifyer!\n \n"
)


localDir = os.getcwd().replace("\\", "/")


def createDir(folder):
    path = ""
    for i in range(len(folder)):
        path = path + "/" + folder[i]
        if not os.path.exists(localDir + path):
            os.makedirs(localDir + path)

    return localDir + path


localSaveFile = createDir(["F1_bulks"])


def menu():
    years = []
    # Um ou mais anos
    try:
        quote = input(
            "Would you like to check a single or a range of years? \nS - for single / R - for range: "
        ).lower()
        if quote == "s":
            start_year = int(input("What is the year woul like to check (YYYY)?  "))
            years.append(str(start_year))
        else:
            start_year = int(
                input("What is the first year woul like to check (YYYY)?  ")
            )
            end_year = int(input("What is the last year to check?  "))
            for year in range(start_year, end_year + 1):
                years.append(str(year))

    except ValueError:
        print(
            "This is not the correct date format. Please, input the format (DD/MM/YYYY)"
        )
        menu()
        print("This is all the dates to check \n", years)
    newYear = input("Would like to scrap other year? [y/n] ")
    if newYear == "y":
        menu()
    else:
        return years, main(years)


# um = variavel
# Vários = lista
def main(years):
    print(years[0])
    for year in years:
        url = f"https://www.formula1.com/en/results.html/{year}/races.html"
        print(url)
        df = pd.DataFrame()
        response = (
            requests.get(url, verify=False)
            .content.decode("ISO-8859-1")
            .encode("latin-1")
        )
        soup = BeautifulSoup(response, "html.parser")
        table = soup.find("table")
        # print(table, type(table))
        for row in table.find_all("tr"):
            columns = row.find_all("td")
            if columns != []:
                GRAND_PRIX = columns[1].text.strip()
                DATE = columns[2].text.strip()
                WINNER = " ".join([span.get_text(strip=True) for span in columns[3]])
                CAR = columns[4].text.strip()
                LAPS = columns[5].text.strip()
                TIME = columns[6].text.strip()

                # print(GRAND_PRIX, DATE, WINNER, CAR, LAPS, TIME) #

                df = df._append(
                    {
                        "GP": GRAND_PRIX,
                        "Data": DATE,
                        "Vencedor": WINNER,
                        "Carro": CAR,
                        "Volta": LAPS,
                        "Tempo": TIME,
                    },
                    ignore_index=True,
                )
        print(df)

        # >>> Gerar único (data que rodou)  >>> Exportar os arquivos para .xlsx (excel) e .csv para bancos de dados  os dois
        yearTosave = year[0]
        df.to_csv(f"{localSaveFile}/F1_bulks_{yearTosave}.csv")


# | enviar por e-mail|


# | abrir os arquivos dentro do python |

menu()
