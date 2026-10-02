"""Sistema de Registro de Calificaciones - PFU-111."""

NOTA_MINIMA = 0
NOTA_MAXIMA = 100
NOTA_APROBACION = 51  # ajusta según el criterio de tu docente
CANTIDAD_NOTAS = 3


def pedir_nombre():
    """Solicita un nombre y repite hasta que no esté vacío."""
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre:
            return nombre
        print("ERROR: El nombre no puede estar vacío.")


def pedir_calificacion(numero):
    """Solicita una calificación numérica entre 0 y 100."""
    mensaje = f"Ingrese la calificación {numero}: "
    while True:
        try:
            nota = float(input(mensaje).strip())
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")
            mensaje = "Ingrese nuevamente la calificación: "
            continue
        except (EOFError, KeyboardInterrupt):
            raise
        if nota != nota or nota in (float("inf"), float("-inf")):
            print("ERROR: Debe ingresar un número válido.")
        elif NOTA_MINIMA <= nota <= NOTA_MAXIMA:
            return nota
        else:
            print(f"ERROR: La calificación debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}.")
        mensaje = "Ingrese nuevamente la calificación: "


def calcular_promedio(notas):
    """Devuelve el promedio; evita la división entre cero."""
    if not notas:
        raise ValueError("No hay calificaciones para calcular el promedio.")
    return sum(notas) / len(notas)


def determinar_estado(promedio):
    return "APROBADO" if promedio >= NOTA_APROBACION else "REPROBADO"


def registrar_estudiante():
    nombre = pedir_nombre()
    notas = [pedir_calificacion(i) for i in range(1, CANTIDAD_NOTAS + 1)]
    promedio = calcular_promedio(notas)
    return {"nombre": nombre, "notas": notas, "promedio": promedio,
            "estado": determinar_estado(promedio)}


def mostrar_resultado(est):
    print("\n--- RESULTADO ---")
    print(f"Estudiante: {est['nombre']}")
    print("Calificaciones:", ", ".join(f"{n:g}" for n in est["notas"]))
    print(f"Promedio: {est['promedio']:.2f}")
    print(f"Estado: {est['estado']}\n")


def preguntar_continuar():
    while True:
        r = input("¿Desea registrar otro estudiante? (s/n): ").strip().lower()
        if r in ("s", "n"):
            return r == "s"
        print("ERROR: Responda con 's' o 'n'.")


def main():
    estudiantes = []
    try:
        while True:
            est = registrar_estudiante()
            estudiantes.append(est)
            mostrar_resultado(est)
            if not preguntar_continuar():
                break
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada interrumpida. Se finaliza el programa.")
    print(f"Total de estudiantes registrados: {len(estudiantes)}")


if __name__ == "__main__":
    main()