from datetime import timedelta, datetime

events = []
events_indexes = []


def rainfall_events(rain_data: list):
    # 6h
    max_index = len(rain_data[1])
    start = 0

    while start + 72 <= max_index:
        block = rain_data[1][start:start + 72]

        if block[0] != 0:  # verifica se primeiro valor é diferente de zero
            total = sum(block)
            if total >= 10:
                print(f"Evento de até 6 horas detectado de {total}mm: {block}")
                events.append([rain_data[0][start], rain_data[0][start + 72 - 1], total])
                events_indexes.extend(range(start, start + 72))
                start += 72
            else:
                start += 1
        else:
            start += 1

    # 15min
    start = 0

    while start + 3 <= max_index:
        if any(i in events_indexes for i in range(start, start + 3)):
            start += 1
            continue

        block = rain_data[1][start:start + 3]

        if block[0] != 0:  # começa com valor diferente de zero
            total = sum(block)
            if total > 6:
                print(f"Evento de até 15 minutos detectado de {total:.3f}mm: {block}")
                events.append([rain_data[0][start], rain_data[0][start + 3 - 1], total, "Evento 15min"])
                events_indexes.extend(range(start, start + 3))
                start += 3
            else:
                start += 1
        else:
            start += 1

    return events
