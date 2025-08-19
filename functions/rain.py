events = []
events_indexes = []


# FUNCAO PARA INTEGRACAO DE CHUVAS EROSIVAS COM DURACAO DE ATE 6 HORAS E ATE 15 MINUTOS
def rainfall_events(rain_data: list):
    erosive_rainfall_event(rain_data, 6)
    erosive_rainfall_event(rain_data, 0.25)

    return events


# FUNCAO PARA IDENTIFICACAO DE EVENTOS DE CHUVAS EROSIVAS
# interval = tempo em horas do evento (6 = 6 horas, 0.25 = 15 minutos)
def erosive_rainfall_event(rain_data, interval):
    max_index = len(rain_data[1])
    start = 0

    while start + (interval * 12) <= max_index:
        block = rain_data[1][start:start + int(interval * 12)]
        print(block)

        if block[0] != 0:
            total = sum(block)
            if total >= 10:
                # print(f"Evento de até 6 horas detectado de {total}mm: {block}")
                intensity = round(rainfall_intensity(total, rain_data[0][start], rain_data[0][start + (interval * 12)]),
                                  4)
                i30 = max_rainfall_intensidy_30min(block) * 2
                events.append([rain_data[0][start], rain_data[0][start + (interval * 12)], total, intensity, i30])
                events_indexes.extend(range(start, start + (interval * 12)))
                start += (interval * 12)
            else:
                start += 1
        else:
            start += 1
    return


# FUNCAO PARA DETERMINACAO DA INTENSIDADE TOTAL
# total_precipitation = lamina precipitada, event_start e event_end = datetimes de inicio e fim do evento de chuva
def rainfall_intensity(total_precipitation, event_start, event_end):
    return total_precipitation / ((event_end - event_start).total_seconds() / 3600)


# FUNCAO PARA IDENTIFICACAO DA MAIOR INTENSIDADE EM 30 MINUTOS PARA O EVENTO IDENTIFICADO
# rainfall e o bloco identificado ao percorrer o array de chuvas
def max_rainfall_intensidy_30min(rainfall: list):
    max_index = len(rainfall)
    start = 0
    i30 = 0

    while start + 6 <= max_index:
        block = rainfall[start:start + 6]
        if sum(block) > i30:
            i30 = sum(block)
        start += 1

    return i30
