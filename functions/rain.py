from datetime import timedelta
from time import sleep

def rainfall_events(rain_data: list):
    max = len(rain_data[1])
    print(max)
    for x in range(1, max):
        start = 0
        end = x
        sleep(1)
        print(f'------------------------------------')
        while end < max:
            if rain_data[0][start] - rain_data[0][end] > timedelta(hours=6):
                print(rain_data[0][start] - rain_data[0][end])
                break
            else:
                rain = rain_data[1][start:end]
                print(f'Inicio: {rain_data[0][start]} - Fim: {rain_data[0][end]} - Soma: {sum(rain)}')
            start+=1
            end+=1