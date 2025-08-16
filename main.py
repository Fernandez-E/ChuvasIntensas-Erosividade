from functions import files, rain, erosivity

rainfall_events = (rain.rainfall_events(files.cr1000_data("CR1000_Table5min_2017_02_23_14_52_58.dat")))

ke = erosivity.kinetic_energy(rainfall_events[0][3])
ei30 = erosivity.rainfall_erosivity_index(ke, rainfall_events[0][3])

print(f'Energia cinetica: {ke} | EI30: {ei30}')
