# agenda-tareas-segura
nuevo proyecto segunda y tercera evaluación digitalización 
Inicialmente tenía pensado el anterior proyecto que entregué , pero debido a que me estaba resultando bastante complicado he decidido cambiar de proyecto , haciendo este desde 0.He optado por desarrollar una Agenda de Tareas Segura, sencilla pero funcional, que me permite aplicar todos los conocimientos necesarios para la práctica: manejo de datos, seguridad, almacenamiento y trabajo en la nube.

El objetivo de este proyecto es crear una aplicación de línea de comandos que funcione como una agenda personal de tareas. La aplicación permite:
Añadir tareas pendientes.
Ver las tareas actuales.
Marcar tareas como hechas.
Eliminar tareas completadas o innecesarias.
Exportar las tareas a un archivo CSV.
Subir ese archivo CSV a Google Drive como copia de seguridad.
Todo esto con una capa básica de seguridad mediante una contraseña de acceso.

Seguridad:El acceso a la agenda está protegido por una contraseña simple, pedida al iniciar el programa. Esto ayuda a evitar que cualquier persona pueda modificar las tareas si accede al dispositivo.

Almacenamiento:Las tareas se guardan en un archivo llamado tareas.csv, que actúa como base de datos local. Cada vez que el usuario añade, elimina o marca como completada una tarea, el archivo se actualiza automáticamente, asegurando la persistencia de los datos.

Este enfoque me permitió entender cómo se guarda, modifica y elimina información

Almacenamiento en la nube:Además de guardar los datos localmente, implementé la funcionalidad para subir el archivo tareas.csv a Google Drive usando la API oficial de Google. Esto garantiza una copia de seguridad en la nube y permite recuperar las tareas desde cualquier dispositivo, si es necesario.

Tecnologias usadas:
Python 3
CSV para almacenamiento local de tareas.
Google Drive API para el almacenamiento en la nube.
OAuth 2.0 para autenticación segura con Google.
Git y GitHub para control de versiones y alojamiento del proyecto.
