#%% 
import os
import glob
from clase_resultados import ResultadosESAR
from uncertainties import ufloat
import matplotlib.pyplot as plt
#%%
subdirectorios=os.listdir(os.path.join(os.getcwd(),"LB97CP2"))
subdirectorios.sort()
print(subdirectorios)

#% LB97CP2 
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
#%% SOLO RT
subdirectorios=os.listdir(os.path.join(os.getcwd(),"LB97CP2"))
subdirectorios_RT = [sd for sd in subdirectorios if "RT" in sd]
subdirectorios_RT.sort()
print(subdirectorios_RT)


#%%RT1

directorio_a_analizar = os.path.join(os.getcwd(), "LB97CP2", subdirectorios_RT[0])
patron_analisis = os.path.join(directorio_a_analizar, "Analisis_*")
directorios_analisis = glob.glob(patron_analisis)

if not directorios_analisis:
    print(f"No se encontraron directorios 'Analisis_' en {directorio_a_analizar}")
    exit()

directorio_analisis_RT_1 = directorios_analisis[-1]

try:
    resultados_RT_1 = ResultadosESAR(directorio_analisis_RT_1)
except Exception as e:
    print(f"Error al cargar los datos: {e}")
    exit()

#% RT2

directorio_a_analizar = os.path.join(os.getcwd(), "LB97CP2", subdirectorios_RT[1])
patron_analisis = os.path.join(directorio_a_analizar, "Analisis_*")
directorios_analisis = glob.glob(patron_analisis)

if not directorios_analisis:
    print(f"No se encontraron directorios 'Analisis_' en {directorio_a_analizar}")
    exit()

directorio_analisis_RT_2 = directorios_analisis[-1]

try:
    resultados_RT_2 = ResultadosESAR(directorio_analisis_RT_2)
except Exception as e:
    print(f"Error al cargar los datos: {e}")
    exit()



#%%

directorio_a_analizar = glob.glob(os.path.join(os.getcwd(),'LB97CP2','*RT','Analisis_*'))


resultados_RT_1 = ResultadosESAR(directorio_a_analizar[0])
resultados_RT_2 = ResultadosESAR(directorio_a_analizar[1])

fig1, (ax1,ax2) = plt.subplots(1,2,figsize=(12,5),sharex=True,sharey=True)

ax1.plot(resultados_RT_1.primer_ciclo['H_kAm'], resultados_RT_1.primer_ciclo['M_Am'], '.',label="RT1 1" )
ax1.plot(resultados_RT_1.ultimo_ciclo['H_kAm'], resultados_RT_1.ultimo_ciclo['M_Am'], '.',label="RT1 u")
ax2.plot(resultados_RT_2.primer_ciclo['H_kAm'], resultados_RT_2.primer_ciclo['M_Am'], label="RT2 1")
ax2.plot(resultados_RT_2.ultimo_ciclo['H_kAm'], resultados_RT_2.ultimo_ciclo['M_Am'], label="RT2 u")


ax1.legend()
plt.show()



# %%
subdirectorios=os.listdir(os.path.join(os.getcwd(),"LB97CP2"))
subdirectorios_RT = [sd for sd in subdirectorios if "RT" in sd]
subdirectorios_RT.sort()
print(subdirectorios_RT)

for sd in subdirectorios_RT:
    print(sd)
    directorio_a_analizar = os.path.join(os.getcwd(), "LB97OH", sd)

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
    
# %%
#%% LB97CP2 + VS55
subdirectorios=os.listdir(os.path.join(os.getcwd(),"LB97CP2+VS55"))
subdirectorios.sort()
print(subdirectorios)

#%%
res_VS55=[]
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
        res_VS55.append(resultados)
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
