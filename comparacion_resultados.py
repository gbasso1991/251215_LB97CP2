#%%
"""
analizar_experimento.py
Ejemplo simple para analizar un experimento ESAR."""
import os
import glob
from clase_resultados import ResultadosESAR
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt

#%% ============================================================

# Ruta completa al directorio que quieres analizar
# Estructura: directorio_actual/LB97OH/251112_112723_RT/Analisis_[fecha]
directorio_a_analizar = os.path.join(os.getcwd(),"LB97CP2", "251216_150445_RT")

print("=" * 70)
print(f"Directorio actual: {os.getcwd()}")
print(f"Buscando en: {directorio_a_analizar}")

# ============================================================
# BUSCAR DIRECTORIOS DE ANÁLISIS
# ============================================================

patron_analisis = os.path.join(directorio_a_analizar, "Analisis_*")
directorios_analisis = glob.glob(patron_analisis)

if not directorios_analisis:
    print(f"✗ No se encontraron directorios 'Analisis_' en:")
    print(f"  {directorio_a_analizar}")
    print("\nPosibles causas:")
    print("1. El directorio no existe")
    print("2. El análisis no se ha procesado aún")
    print("3. El nombre no sigue el patrón 'Analisis_YYYYMMDD'")
    exit()

print(f"\n✓ Se encontraron {len(directorios_analisis)} directorios de análisis:")
for d in directorios_analisis:
    print(f"  • {os.path.basename(d)}")

# Tomar el más reciente (último en la lista)
directorio_analisis = directorios_analisis[-1]
print(f"\nDirectorio seleccionado: {os.path.basename(directorio_analisis)}")

#% ============================================================
# PASO 2: CARGAR LOS RESULTADOS
# ============================================================

try:
    print("\n" + "=" * 70)
    print("CARGANDO RESULTADOS...")
    print("=" * 70)
    
    # Esta línea hace TODO automáticamente:
    # 1. Busca resultados.txt
    # 2. Carga todos los datos
    # 3. Busca ciclos_H_M/
    # 4. Carga primer y último ciclo
    resultados = ResultadosESAR(directorio_analisis)
    
    print("\n✅ ¡Datos cargados exitosamente!")
    
except Exception as e:
    print(f"\n❌ Error al cargar los datos: {e}")
    print("\nSolución:")
    print("1. Asegúrate de que existe 'resultados.txt' en el directorio")
    print("2. Verifica que exista el subdirectorio 'ciclos_H_M/'")
    print("3. Comprueba que las funciones lector_resultados y lector_ciclos estén definidas")
    exit()

#%% ============================================================
# PASO 3: ACCEDER A LOS DATOS
# ============================================================

print("\n" + "=" * 70)
print("DATOS DISPONIBLES:")
print("=" * 70)

# Información básica
print(f"\n📊 Información básica:")
print(f"  • Mediciones: {len(resultados.files)}")

# Temperatura
if hasattr(resultados, 'temperatura'):
    temp_min = resultados.temperatura.min()
    temp_max = resultados.temperatura.max()
    print(f"  • Temperatura: {temp_min:.1f}°C --> {temp_max:.1f}°C")
    print(f"  • ΔT: {temp_max - temp_min:.1f}°C")

# Valores clave
if hasattr(resultados, 'Hc'):
    print(f"  • Hc promedio: {ufloat(resultados.Hc.mean(),resultados.Hc.std()):.1uS} kA/m")

if hasattr(resultados, 'SAR'):
    print(f"  • SAR promedio: {ufloat(resultados.SAR.mean(),resultados.SAR.std()):.1uS} W/g")

if hasattr(resultados, 'tau'):
    print(f"  • Tau promedio: {ufloat(resultados.tau.mean(),resultados.tau.std()):.2uS} ns")


# ============================================================
# PASO 4: VISUALIZACIÓN DE RESULTADOS Y CICLOS
# ============================================================

print("\n" + "=" * 70)
print("VISUALIZACIÓN:")
print("=" * 70)

# 1. Comparación de ciclos
print("  • Gráfico 1: Comparación de ciclos de magnetización")
fig1, ax1 = resultados.plot_ciclos_comparacion(guardar=True)

# 2. Evolución temporal (solo si hay suficientes datos)
if len(resultados.time) > 1:
    print("  • Gráfico 2: Evolución temporal de parámetros")
    fig2, ax2 = resultados.plot_evolucion_temporal(guardar=True)
    fig3, ax3 = resultados.plot_evolucion_temperatura(guardar=True)
print("\n✅ Gráficos generados y guardados en el directorio de análisis")

plt.show()


#%%
import os
import glob
from clase_resultados import ResultadosESAR
from uncertainties import ufloat
import matplotlib.pyplot as plt

subdirectorios=os.listdir(os.path.join(os.getcwd(),"LB97CP2"))
subdirectorios.sort()
print(subdirectorios)

#%%
for sd in subdirectorios:
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
