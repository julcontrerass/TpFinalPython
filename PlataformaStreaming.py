# CLASES PARA LAS SERIES
nombre_series = ["Peaky Blinders", "The Umbrella Academy" ]
visualizaciones_series = [1234567, 2434908]
actores_primera_serie = ["Cillian Murphy", "Paul Anderson" , "Helen McCrory"]
actores_segunda_serie = ["Tom Hopper", "Emmy Raver-Lampman", "Ellen Page", "David Castañeda"]
temporadas = [5 , 2]

# CLASES PARA LAS PELÍCULAS
nombre_peliculas = ["Inception", "Batman Begins", "Inmortales "]
visualizaciones_peliculas = [4760183, 17319533, 35]
actores_primera_pelicula = ["Leonardo DiCaprio", "Ellen Page", "Joseph Gordon-Levitt"]
actores_segunda_pelicula = ["Christian Bale", "Cillian Murphy", "Michael Caine"]
actores_tercera_pelicula = ["Mirtha Legrand", "Leonardo DiCaprio", "Elizabeth Segunda"]
duracion = [148 , 140 , 30]


class Contenido:
    def __init__(self, nombre, visualizaciones, actores):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores

    def obtener_visualizaciones(self):
        return self.visualizaciones

    def obtener_actores(self):
        return self.actores
    

class Serie(Contenido):
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas

    def obtener_temporadas(self):
        return self.temporadas

class Pelicula(Contenido):
    def __init__(self, nombre, visualizaciones, actores, duracion):
        super().__init__(nombre, visualizaciones, actores)
        self.duracion = duracion

    def obtener_duracion(self):
        return self.duracion


class ResultadosDelPrograma:
    def __init__(self):
       #Agrego el contenido de las series 
        self.series = []
        for i in range(len(nombre_series)):
            #use este if para distinguir entre la primera y la segunda serie 
            if i == 0:
                self.series.append(Serie(nombre_series[i], visualizaciones_series[i], 
                                      actores_primera_serie, temporadas[i]))
            else:
                self.series.append(Serie(nombre_series[i], visualizaciones_series[i], 
                                      actores_segunda_serie, temporadas[i]))
        
        #Agrego el contenido de las películas
        self.peliculas = []
        actores_peliculas = [actores_primera_pelicula, actores_segunda_pelicula, actores_tercera_pelicula]
        for i in range(len(nombre_peliculas)):
            self.peliculas.append(Pelicula(nombre_peliculas[i], visualizaciones_peliculas[i], 
                                         actores_peliculas[i], duracion[i]))
        

    #El video (película o serie) de mayor número de visualizaciones.
    def video_mas_visto(self):
        todos_videos = self.series + self.peliculas
        mas_visto = todos_videos[0]
    
        for video in todos_videos:
            if video.obtener_visualizaciones() > mas_visto.obtener_visualizaciones():
                mas_visto = video
    
        return f"El video más visto es {mas_visto.nombre} con {mas_visto.visualizaciones} visualizaciones"

    #El promedio de duración de las películas.
    def promedio_duracion_peliculas(self):
        total_duracion = 0
        contador = 0
    
        for pelicula in self.peliculas:
            total_duracion += pelicula.obtener_duracion()
            contador +=1

        if contador > 0:
            promedio = total_duracion / contador
        else: promedio = 0

        return f"El promedio de duración de las películas es: {promedio} minutos"

    #Los nombres de los actores que trabajan en series y películas.
    def actores_de_ambos_streaming(self):
        actores_series = actores_primera_serie + actores_segunda_serie
        actores_peliculas = actores_primera_pelicula + actores_segunda_pelicula + actores_tercera_pelicula

        actores_comunes = []
    
        for actor in actores_series:
            if actor in actores_peliculas and actor not in actores_comunes:
                actores_comunes.append(actor)
    
        return f"Actores que trabajan en series y películas: {', '.join(actores_comunes)}"


    # Filtra las series con más de 3 temporadas
    def series_mas_tres_temporadas(self):
        mas_temporadas = []
        for serie in self.series:
            if serie.temporadas > 3:
                mas_temporadas.append(serie.nombre)
        return f"Series con más de 3 temporadas: {', '.join(mas_temporadas)}"

    def menu(self):
        while True:
            print("\n=== MENÚ DE OPCIONES ===")
            print("1- Ver video más visto")
            print("2- Ver promedio de duración de películas")
            print("3- Ver actores que trabajan en series y películas")
            print("4- Ver series con más de 3 temporadas")
            print("5- Salir")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                print(self.video_mas_visto())
            elif opcion == "2":
                print(self.promedio_duracion_peliculas())
            elif opcion == "3":
                print(self.actores_de_ambos_streaming())
            elif opcion == "4":
                print(self.series_mas_tres_temporadas())
            elif opcion == "5":
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    ResultadosDelPrograma.menu()