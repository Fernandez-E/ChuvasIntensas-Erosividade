from functions import files, rain

rain_data = files.cr1000_data("CR1000_Table5min_2017_02_23_14_52_58.dat")
# RAIN_DATA[0] = Data e hora
# RAIN_DATA[1] = Precipitação


rain.rainfall_events(rain_data)
