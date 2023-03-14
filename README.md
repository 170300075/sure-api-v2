# SURE API Rev. 2

El Sistema Unificado de Recomendación Escolar es un conjunto de herramientas cuya finalidad es mantener a los estudiantes actualizados con la información pertinente de su trayectoria universitaria.

Una de las principales caracteristicas de este software respecto a los actuales usados en la Universidad del Caribe, es que la información es usada de forma conveniente para permitir al estudiantado tomar mejores decisiones respecto a indicadores. 

La caracteristica más importante de este sistema, que es un factor diferenciador, es que cada estudiante puede recibir recomendaciones curriculares, o bien, validar nuevas que hayan sido creadas manualmente. 

El proyecto está destinado a la administración de los datos y la adquisición de nuevos registros. Toda la infraestructura transaccional se realiza mediante endpoints que permiten mantener actualizada la información en todo momento. 

Alguna de las funcionalidades en las que se desarrolla el proyecto incluyen:
Recuperacion de información en SIGMAA: 

*Los datos se obtienen por través de webscrapers*


- Oferta académica por categoría
    - Asignaturas.
    - Horarios.
    - Nombres de los docentes.
    - Modalidades.
    - Aulas.
- Calificaciones semestrales
    - Docentes.
    - Asignaturas.
    - Modalidades.
    - Calificaciones parciales y finales.
- Información personal del estudiante
    - Nombre y apellidos.
    - Números de telefono (personal y hogar).
    - Dirección.
    - Información parental.
    - Estado civil (personal y parental).
    - Información laboral.
        - Empresa.
        - Telefono de trabajo.
        - Dirección.
        - Horario.
- Estatus escolar del estudiante
    - Estatus (regular, condicionado, etc).
    - Programa educativo.
    - Nombre de la carrera.
    - Estatus de servicio social.
- Listado de pagos y adeudos
    - Historial de pagos efectuados/atrasados.
    - Fichas de pago generadas por el sistema.

2. Datos obtenidos del SIPP:

- Oferta de prácticas profesionales

3. Datos obtenidos del SASS:

- Oferta de Servicio Social

## Objetivos especificos

- Consultar la oferta académica
    - Todas las asignaturas ofertadas.
    - Solo las asignaturas por acreditar.
    - Mostrar la tasa de reprobación/aprobación (dinámica).
    - Veces que se ha seleccionado por un estudiante.
- Registrar al información del estudiante
    - Recuperarla por primera vez para el registro.
    - Permitir actualizar algunos datos de ellos en el sistema.