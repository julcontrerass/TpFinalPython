# Plataforma de Streaming - Proyecto Final

Este proyecto tiene como objetivo desarrollar el backend de una plataforma de streaming de videos, donde se podrán encontrar películas y series. 

## Requerimientos

Deberás crear el backend de la plataforma, estructurando y manipulando datos como se detalla a continuación.

### Datos Disponibles

A continuación, se presentan los datos iniciales que deben ser organizados en diferentes listas para crear instancias de películas y series:

#### Series

- **Peaky Blinders** (1.234.567 visualizaciones)
  - **Actores**: Cillian Murphy, Paul Anderson, Helen McCrory
  - **Temporadas**: 5

- **The Umbrella Academy** (2.434.908 visualizaciones)
  - **Actores**: Tom Hopper, Emmy Raver-Lampman, Ellen Page, David Castañeda
  - **Temporadas**: 2

#### Películas

- **Inception** (4.760.183 visualizaciones)
  - **Actores**: Leonardo DiCaprio, Ellen Page, Joseph Gordon-Levitt
  - **Duración**: 148 minutos

- **Batman Begins** (17.319.533 visualizaciones)
  - **Actores**: Christian Bale, Cillian Murphy, Michael Caine
  - **Duración**: 140 minutos

- **Inmortales** (35 visualizaciones)
  - **Actores**: Mirtha Legrand, Leonardo DiCaprio, Elizabeth Segunda
  - **Duración**: 30 minutos

### Requerimientos Funcionales

La plataforma debe cumplir con las siguientes funcionalidades:

1. **Determinar el video con mayor número de visualizaciones** (serie o película).
2. **Calcular el promedio de duración de las películas**.
3. **Listar los nombres de los actores que participan en series y películas**.
4. **Listar las series que tienen más de 3 temporadas**.

### Reglas

- Las listas de datos iniciales solo pueden usarse para instanciar los objetos correspondientes de series y películas. **No pueden usarse directamente para los algoritmos de resolución.**
- Se debe implementar **herencia** al definir las clases necesarias.
- Se debe implementar **al menos un método para cada uno de los requerimientos funcionales** mencionados.

### Requerimiento Final

Crear una función **Menú** que permita visualizar todos los datos generados de forma independiente en la terminal. El menú debe ofrecer una opción numérica para cada funcionalidad, permitiendo al usuario seleccionar y ejecutar cada opción más de una vez, si así lo desea.

## Tip

Organiza tus clases de manera que simplifiquen el procesamiento y eviten duplicación de código mediante el uso de herencia y encapsulación.

---
