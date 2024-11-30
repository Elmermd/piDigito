# Generador de Dígitos del Número PI

Este proyecto es un programa en Python que extrae y muestra una cantidad específica de dígitos del número π (PI) según la solicitud del usuario. Utiliza las bibliotecas `requests` y `BeautifulSoup` para obtener los datos de un sitio web, analizar el contenido y extraer los dígitos de PI.

## Requisitos

Para ejecutar este programa, asegúrate de tener instaladas las siguientes bibliotecas:

- `requests`
- `beautifulsoup4`
  
# Descripción del Programa

El programa realiza los siguientes pasos:

1. **Obtención de Datos**: Utiliza la biblioteca `requests` para extraer el contenido de la página web de [Pi Day](https://www.piday.org/million/), que contiene un millón de dígitos de PI.

2. **Análisis del HTML**: Usa `BeautifulSoup` para procesar el HTML y localizar el elemento que contiene los dígitos del número PI.

3. **Interacción con el Usuario**: Solicita al usuario la cantidad de dígitos que desea visualizar después del punto decimal.

4. **Mostrar Resultados**: Muestra los dígitos solicitados y ofrece la opción de realizar otra consulta o finalizar el programa.

---

# Cómo Ejecutarlo

1. Clona este repositorio o copia el código fuente en un archivo llamado, por ejemplo, `pi_digits_generator.py`.

2. Asegúrate de que tus dependencias estén instaladas:

   ```bash
   pip install requests beautifulsoup4
# Ejemplo de Uso
Bienvenido al generador de digitos del número PI!!!
Por favor, indique cuantos digitos despues del punto quiere visualizar del número PI: 5
3.14159
¿Desea realizar otra consulta? Escriba 'Y' para continuar. 'N' para salir. Y
Por favor, indique cuantos digitos despues del punto quiere visualizar del número PI: 10
3.1415926535
¿Desea realizar otra consulta? Escriba 'Y' para continuar. 'N' para salir. N

# Notas

- El programa obtiene los dígitos de PI directamente del sitio web [Pi Day](https://www.piday.org/million/). Si el sitio cambia su estructura, es posible que el programa necesite ajustes.
- La cantidad máxima de dígitos que puedes solicitar es **1,000,000** (el límite del sitio web).

---

# Limitaciones

- El programa depende de la conexión a Internet para obtener los datos de la página.
- No se implementa manejo de errores en caso de que el sitio web no esté disponible.
