
#%% 
import os
import glob
from clase_resultados import ResultadosESAR
from uncertainties import ufloat
import matplotlib.pyplot as plt

subdirectorios=os.listdir(os.path.join(os.getcwd(),"LB97CP2"))
subdirectorios.sort()
print(subdirectorios)

#%% LB97CP2 
for sd in subdirectorios:
    print(sd)
    directorio_a_analizar = os.path.join(os.getcwd(), "LB97CP2", sd)

    patron_analisis = os.path.join(directorio_a_analizar, "Analisis_*")
    directorios_analisis = glob.glob(patron_analisis)

    if not directorios_analisis:
        print(f"No se encontraron directorios 'Analisis_' en {directorio_a_analizar}")
        exit()

    directorio_analisis = directorios_analisis[-1]

    try:
        resultados = ResultadosESAR(directorio_analisis)
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        exit()

    print(f"Mediciones: {len(resultados.files)}")

    print(f'Concentracion: {resultados.meta["Concentracion g/m^3"]/1000} mg/mL')
    if hasattr(resultados, 'temperatura'):
        temp_min = resultados.temperatura.min()
        temp_max = resultados.temperatura.max()
        print(f"Temperatura: {temp_min:.1f}°C → {temp_max:.1f}°C")

    if hasattr(resultados, 'SAR'):
        print(f"SAR: {ufloat(resultados.SAR.mean(), resultados.SAR.std()):.1uS} W/g")

    if hasattr(resultados, 'tau'):
        print(f"Tau: {ufloat(resultados.tau.mean(), resultados.tau.std()):.2uS} ns")

    if hasattr(resultados, 'Hc'):
        print(f"Hc: {ufloat(resultados.Hc.mean(), resultados.Hc.std()):.1uS} kA/m")

    fig, ax = resultados.plot_ciclos_comparacion(guardar=True)

    fig1, ax1 = resultados.plot_ciclos_comparacion(guardar=True)

    fig2, ax2 = resultados.plot_evolucion_temporal(guardar=True)

    fig3, ax3 = resultados.plot_evolucion_temperatura(guardar=True)

    plt.show()

#%% LB97CP2 + VS55
subdirectorios=os.listdir(os.path.join(os.getcwd(),"LB97CP2+VS55"))
subdirectorios.sort()
print(subdirectorios)


for sd in subdirectorios:
    print(sd)
    directorio_a_analizar = os.path.join(os.getcwd(), "LB97CP2+VS55", sd)

    patron_analisis = os.path.join(directorio_a_analizar, "Analisis_*")
    directorios_analisis = glob.glob(patron_analisis)

    if not directorios_analisis:
        print(f"No se encontraron directorios 'Analisis_' en {directorio_a_analizar}")
        exit()

    directorio_analisis = directorios_analisis[-1]

    try:
        resultados = ResultadosESAR(directorio_analisis)
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        exit()

    print(f"Mediciones: {len(resultados.files)}")

    print(f'Concentracion: {resultados.meta["Concentracion g/m^3"]/1000} mg/mL')
    if hasattr(resultados, 'temperatura'):
        temp_min = resultados.temperatura.min()
        temp_max = resultados.temperatura.max()
        print(f"Temperatura: {temp_min:.1f}°C → {temp_max:.1f}°C")

    if hasattr(resultados, 'SAR'):
        print(f"SAR: {ufloat(resultados.SAR.mean(), resultados.SAR.std()):.1uS} W/g")

    if hasattr(resultados, 'tau'):
        print(f"Tau: {ufloat(resultados.tau.mean(), resultados.tau.std()):.2uS} ns")

    if hasattr(resultados, 'Hc'):
        print(f"Hc: {ufloat(resultados.Hc.mean(), resultados.Hc.std()):.1uS} kA/m")


    fig1, ax1 = resultados.plot_ciclos_comparacion(guardar=True)

    fig2, ax2 = resultados.plot_evolucion_temporal(guardar=True)

    fig3, ax3 = resultados.plot_evolucion_temperatura(guardar=True)

    plt.show()

# %%
