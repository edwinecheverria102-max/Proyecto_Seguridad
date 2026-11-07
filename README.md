Plataforma Segura de Venta y Distribución de Contenido Digital

Aplicación web de comercio electrónico orientada a la venta y distribución de productos digitales. Este proyecto implementa medidas de seguridad avanzadas como almacenamiento seguro de contraseñas (Argon2id), control de acceso por roles, firma digital de comprobantes y fingerprinting de archivos descargados.

Requisitos Previos

Python 3.10 o superior instalado de forma nativa en el sistema.

Git instalado.

Guía de Instalación para el Equipo de Desarrollo

Sigue estos pasos para configurar el proyecto en tu máquina local.

1. Clonar el repositorio

Abre tu terminal y clona el proyecto en la carpeta de tu preferencia:

git clone <AQUI_URL_DE_TU_REPOSITORIO_GITHUB>
cd <NOMBRE_DE_LA_CARPETA_DEL_PROYECTO>


2. Crear el entorno virtual

Para aislar las dependencias del proyecto, crearemos un entorno virtual.

En Windows:

py -m venv venv


En macOS o Linux:

python3 -m venv venv


3. Activar el entorno virtual

En Windows (PowerShell):

.\venv\Scripts\activate


(Si PowerShell te muestra un error de directivas de ejecución, ejecuta Set-ExecutionPolicy Unrestricted -Scope CurrentUser, presiona "S" y vuelve a intentarlo).

En macOS o Linux:

source venv/bin/activate


(Sabrás que funcionó porque aparecerá el texto (venv) al inicio de tu terminal).

4. Instalar las dependencias

Con el entorno virtual activado, instala Django y las bibliotecas criptográficas necesarias:

pip install django argon2-cffi cryptography


5. Ejecutar el servidor de desarrollo

Levanta el servidor local con el siguiente comando:

python manage.py runserver


Abre tu navegador y visita http://127.0.0.1:8000/. Para detener el servidor en cualquier momento, presiona Ctrl + C en la terminal.

🔒 Notas sobre Seguridad (Próximas implementaciones)

Las contraseñas de los usuarios nunca se guardan en texto plano; el sistema utiliza Argon2id.

Posteriormente, el servidor se ejecutará sobre HTTPS mediante un certificado TLS emitido por una CA local.

Las claves privadas para la firma de comprobantes no deben subirse a este repositorio.
