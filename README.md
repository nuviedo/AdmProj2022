# AdmProj2022
Proyecto Final de Administración de Proyectos 2022-2: ENES Unidad Morelia, UNAM, México.
Demostración de técnicas de Ingeniería de Software utilizando las librerías [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) y [sqlite3](https://docs.python.org/3/library/sqlite3.html) para emular una terminal de venta en una farmacia.

> Alexis H. Nuviedo Arriaga [@nuviedo](https://github.com/nuviedo)
> 
> Jadiel Zúñiga Rodríguez [@JZRodriguez](https://github.com/JZRodriguez)
> 
> José I. Esparza Ireta [@ignacio-ireta](https://github.com/ignacio-ireta)
> 
> Sofía García De La Rosa [@SofiaDeLaRosa](https://github.com/SofiaDeLaRosa)

### Tabla de Contenidos
* Introducción
* Sobre el uso de la documentación
* Conceptos de las operaciones - Modo Instruccional
* Procedimientos - Modo Referencial
* Información sobre comandos de software - Atajos
* Mensajes de Error y Troubleshooting
* Glosario
* Características de navegación
* Índice
* Herramientas de Búsqueda


### Introducción
El propósito de este documento es el definir la funcionalidad del proyecto. El proyecto está planeado para poder simplificar el sistema de medicinas de diferentes tiendas de fármacos para poder hacer su búsqueda, sus ventas, y su control de inventario más simple, con una interfaz fácil de entender para el usuario.
Esto se hace con una terminal dividida en tres secciones principales:
* Inventario : Para revisar los ítems en stock
* Ventas : Para ver el registro de ventas hechas con anterioridad
* Terminal : Para realizar ventas



### Sobre el uso de la documentación

Para el uso de la aplicación se asume que el usuario es relativamente familiar con el funcionamiento de una farmacia, el proceso de ventas convencional, y las características presentes en un medicamento en general, como lo son el nombre de marca, nombre genérico, compuesto activo, dosage, precio unitario, presentaciones, etc. 

Una advertencia a hacerse es que el sistema no contempla correcciones o devoluciones a las ventas, por lo que cualquier venta realizada es final.
El usuario debe tener en cuenta que su credencial de acceso es única y solo se dictamina por el administrador de red a petición de un empleado, y que cada venta realizada se asigna al empleado que la finalizó, por lo que es vital preservar las contraseñas como un secreto.


### Conceptos de las operaciones - Modo Instruccional

El programa, al ser un archivo interpretable, no requiere de instalación: sin embargo, requiere las siguientes dependencias instaladas en el sistema:

* [Python > 3.10.4](https://www.python.org/)
* [pysimplegui > 4.60.1](https://pypi.org/project/PySimpleGUI/)
* [pandas > 1.4.2](https://pypi.org/project/pandas/)

Y posteriormente descomprimir el proyecto en una carpeta con permisos de ejecución, lectura y escritura.

Para desinstalar, simplemente elimine el directorio donde se descomprimió el proyecto, y de ser posible, elimine las dependencias siguiendo el manual de las mismas.

Para utilizar el programa es necesario iniciar sesión, tal como se muestra en la siguiente imagen:

![python_zVWIIOAELQ](https://user-images.githubusercontent.com/100146672/171526837-e1aa5cb6-8cbb-4f1b-bdf5-dc2b32b219cf.png)

Donde el primer campo solicita el identificador numérico del empleado y el segundo su contraseña designada.
De perder la información de ingreso, se sugiere contactar al administrador del sistema a la brevedad.


Una vez iniciada sesión, se puede utilizar 3 pestañas para navegar la aplicación:

#### Inventario

![python_mfJ5A0EX6E](https://user-images.githubusercontent.com/100146672/171527343-a517f151-2a46-4b0d-bba3-35adafef36f1.png)
En la ventana de inventario se puede visualizar los medicamentos en existencia según su nombre, compuesto activo, o identificador único. Al introducir valores válidos, la búsqueda tratará de reducirse a medida de lo posible, para dar una lista de medicamentos seleccionables que cumplen las características.

#### Ventas

![python_GTVv7m2qoz](https://user-images.githubusercontent.com/100146672/171527348-249bf50a-d6ce-49f1-981e-20c43cc348e4.png)
En la ventana de ventas se permite al vendedor buscar ventas particulares que se realizaron en el pasado, sea por fecha, por el vendedor que las emitió, o por un identificador único de la medicina involucrada o de la venta en sí. De manera similar a la interfaz anterior, se muestran los datos relacionados a la venta, así como algunos atajos a datos sobre el fármaco vendido.

#### Terminal

![python_XAvwq7g9Ob](https://user-images.githubusercontent.com/100146672/171527386-6cbb1075-50a6-4e5e-baab-7b0ce30252fc.png)
Por último, la terminal permite realizar una venta, incluyendo múltiples medicamentos en diversas cantidades, asociadas al identificador del empleado cuya sesión esté activa. Esto realiza una operación de escritura sobre la base de datos, por lo que debe ser tratada con cautela: no se permite realizar modificaciones a los registros por motivos de auditoría, por lo que toda compra de fármacos es final.


#### Cancelación de Operaciones

Debido a la cantidad mínima de tiempo en la que se ejecutan las operaciones necesarias, generalmente no se tiene el tiempo suficiente para cancelar una operación de escritura, y en caso de que sí se demore la aplicación por alguna falla de conexión, la aplicación tendría que reiniciarse.


### Procedimientos - Modo Referencial

En cuanto a procesos, los procesos de búsqueda se hacen utilizando la técnica de _fuzzy search_, donde se busca una cadena que se aproxime a un resultado dado para cada consulta, y se combinan de forma exclusiva. Para introducir valores, se especifican sin dejar ningún dato nulo, y haciendo ejecuciones secuenciales por cada compra para aprovechar la optimización de multiconsultas.

Por defecto, las contraseñas generadas deben ser cambiadas, puesto a que se generan en función de el ID del empleado de forma muy poco segura.

Para concluir una venta, es imperativo tener a la mano la información identificante del medicamento a vender.

### Mensajes de Error y Troubleshooting

El único mensaje de error presente en la aplicación es al fallar un inicio de sesión: se le avisará al usuario que vuelva a introducir su contraseña, y se esperará 3 segundos por defecto antes de cerrar el mensaje de manera automática.
