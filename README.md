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

PROYECTO 3:
Motivación real:
He decidido crear una Agenda de Tareas Segura con exportación y subida a la nube, creo que es una cosa bastante práctica , la cual me puede servir para mi día a día y darle mucha utilidad. Cambié de proyecto porque el anterior se me estaba haciendo bastante complicado. Este nuevo proyecto es más manejable y me ha permitido centrarme en la funcionalidad real.

Cmo intalar y usar :
git clone https://github.com/bruninhogomez/agenda-tareas-segura.git
cd agenda-tareas-segura.git
python agenda.py

Ejemplo de uso :
Cuando se ejecuta, la agenda pedirá una contraseña. Luego puedes añadir tareas, marcarlas como hechas, eliminarlas, y exportarlas a CSV para subirlas a Google Drive.

Criterio 6a) Objetivos estratégicos
Mi software ayuda a mejorar la organización personal y del equipo, permitiendo llevar un control seguro de tareas y subir datos a la nube, alineándose con la estrategia de digitalización.

🔹 Criterio 6b) Áreas beneficiadas
Producción se beneficia al poder asignar tareas. Comunicación mejora al tener visibilidad de lo que se ha hecho.

🔹 Criterio 6c) Digitalización de áreas
Organizar tareas manualmente es ineficiente. Con mi software se digitaliza la gestión de tareas y mejora la trazabilidad.

🔹 Criterio 6d) Integración con otras áreas
Aunque el sistema de tareas es digital, se puede mejorar integrando con herramientas como correo o chat para notificaciones.

🔹 Criterio 6e) Necesidades actuales resueltas
La necesidad de organizar y priorizar tareas, y tener un registro seguro accesible en la nube.

🔹 Criterio 6f) Tecnologías habilitadoras
He utilizado CSV para estructurar datos, y Google Drive como nube. Esto mejora el almacenamiento, la accesibilidad y la seguridad.

🔹 Criterio 6g) Seguridad
Puede haber brechas si se accede sin contraseña. Por eso se implementa una validación de acceso básica. Se podrían añadir hashes o autenticación externa.

🔹 Criterio 6h) Tratamiento de datos
Se almacenan de forma estructurada (CSV). Se controla que no haya errores y se validan entradas. La consistencia se asegura con escritura inmediata tras cambios.


INGLÉS:

Secure Task Agenda
New project for the second and third evaluation of digitalization. Initially, I had planned to use the previous project I submitted, but because it was becoming quite complicated, I decided to switch projects and start this one from scratch. I chose to develop a Simple yet Functional Secure Task Agenda, which allows me to apply all the necessary knowledge for the practice: data handling, security, storage, and cloud work.

The goal of this project is to create a command-line application that functions as a personal task agenda. The application allows:

Add pending tasks.

View current tasks.

Mark tasks as done.

Delete completed or unnecessary tasks.

Export tasks to a CSV file.

Upload the CSV file to Google Drive as a backup.

All of this with a basic layer of security via an access password.

Security: Access to the agenda is protected by a simple password, which is asked for when starting the program. This helps prevent anyone from modifying the tasks if they gain access to the device.

Storage: Tasks are stored in a file called tareas.csv, which acts as a local database. Every time the user adds, deletes, or marks a task as complete, the file is automatically updated, ensuring data persistence.

This approach helped me understand how data is saved, modified, and deleted.

Cloud Storage: In addition to saving data locally, I implemented the functionality to upload the tareas.csv file to Google Drive using the official Google API. This ensures a cloud backup and allows retrieving tasks from any device, if necessary.

Technologies used:

Python 3

CSV for local task storage

Google Drive API for cloud storage

OAuth 2.0 for secure authentication with Google

Git and GitHub for version control and hosting the project

PROJECT 3:
Real Motivation: I decided to create a Secure Task Agenda with export and cloud upload because I think it is quite practical, and it could be very useful for my day-to-day tasks. I changed the project because the previous one was getting quite complicated. This new project is more manageable and allowed me to focus on the actual functionality.

How to Install and Use:

bash
Copiar
Editar
git clone https://github.com/bruninhogomez/agenda-tareas-segura.git
cd agenda-tareas-segura.git
python agenda.py
Usage Example: When run, the agenda will ask for a password. Then you can add tasks, mark them as done, delete them, and export them to a CSV to upload to Google Drive.

Evaluation Criteria:
6a) Strategic Objectives: My software helps improve personal and team organization by enabling secure task management and uploading data to the cloud, aligning with the digitalization strategy.

6b) Benefited Areas: Production benefits from being able to assign tasks. Communication improves by providing visibility into what has been done.

6c) Digitalization of Areas: Manually organizing tasks is inefficient. My software digitalizes task management and improves traceability.

6d) Integration with Other Areas: Although the task system is digital, it could be improved by integrating with tools like email or chat for notifications.

6e) Addressed Current Needs: The need to organize and prioritize tasks, and to have a secure record accessible in the cloud.

6f) Enabling Technologies: I used CSV for structuring data and Google Drive as the cloud platform. This improves storage, accessibility, and security.

6g) Security: There could be security gaps if the system is accessed without a password. That's why a basic access validation is implemented. Adding hashing or external authentication could improve security.

6h) Data Handling: Data is stored in a structured format (CSV). Errors are checked, and inputs are validated. Consistency is ensured by immediately writing changes after modifications.
