from math import log


# FUNCAO PARA DETERMINACAO DE ENERGIA CINETICA DOS EVENTOS DE CHUVA EROSIVA
def kinetic_energy(rainfall_event_intensity):
    return 0.119 + 0.0873 * log(rainfall_event_intensity, 10)


# FUNCAO PARA DETERMINACAO DE EROSIVIDADE DOS EVENTOS DE CHUVA EROSIVA
def rainfall_erosivity_index(k_energy, rainfall_intensity_30):
    return k_energy * rainfall_intensity_30
