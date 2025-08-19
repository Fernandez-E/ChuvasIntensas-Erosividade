from datetime import datetime

linhas, time, rain = [], [], []


# FUNCAO PARA LEITURA E ORGANIZACAO DE ARQUIVO CAMPBELL
# O arquivo campbell deve ser organizado com o primeiro registro em formato datetime (YYYY-mm-dd HH:MM:SS) e
# registros de precipitacao na terceira posicao do arquivo
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
