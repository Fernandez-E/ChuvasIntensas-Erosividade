from datetime import datetime

linhas, time, rain, temp = [], [], [], []


def cr1000_data(file):
    with open(file, 'r') as arquivo:
        for linha in arquivo:
            linhas.append(linha.strip().replace('""', ' ').replace('"', '').replace(',', ';'))

        for i in range(4):
            linhas.pop(0)

        for data in linhas:
            data = data.split(";")
            time.append(datetime.strptime(data[0], "%Y-%m-%d %H:%M:%S"))
            rain.append(float(data[2]))

        return [time, rain]
