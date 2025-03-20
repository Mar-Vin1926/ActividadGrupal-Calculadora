# Calculadora con Registro de Usuarios y Operaciones

Este proyecto es una aplicación web de calculadora creada con Streamlit, que permite a los usuarios realizar operaciones aritméticas básicas y registrar tanto los usuarios que acceden a la calculadora como las operaciones que realizan. Los datos se almacenan en archivos Excel (`usuarios.xlsx` y `operaciones.xlsx`).

## Funcionalidades

* Registro de usuarios: Cada vez que un usuario ingresa su nombre, se registra en el archivo `usuarios.xlsx` junto con la fecha y hora de acceso.
* Calculadora básica: Permite realizar sumas, restas, multiplicaciones, divisiones y raíces cuadradas.
* Registro de operaciones: Cada vez que un usuario realiza una operación, se registra en el archivo `operaciones.xlsx` junto con el usuario, la operación realizada, el resultado y la fecha y hora.

## Requisitos

* Python 3.6 o superior
* Streamlit
* Pandas
* Openpyxl

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone https://github.com/Mar-Vin1926/ActividadGrupal-Calculadora.git
    ```

2.  Navega a la carpeta del proyecto:

    ```bash
    cd ActividadGrupal-Calculadora
    ```

3.  Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

4.  Activa el entorno virtual:

    * En Windows (cmd.exe):

        ```bash
        venv\Scripts\activate
        ```

    * En Windows (PowerShell):

        ```bash
        venv\Scripts\Activate.ps1
        ```

    * En macOS y Linux:

        ```bash
        source venv/bin/activate
        ```

5.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

6.  Ejecuta la aplicación:

    ```bash
    streamlit run app.py
    ```

7.  Abre el navegador en la URL que se muestra en la terminal.

## Uso

1.  Ingresa tu nombre de usuario en el campo de texto.
2.  Ingresa los números que deseas operar en los campos correspondientes.
3.  Selecciona la operación que deseas realizar.
4.  Haz clic en el botón "Calcular".
5.  El resultado se mostrará en la pantalla.
6.  Los registros de usuarios y operaciones se guardarán en los archivos `usuarios.xlsx` y `operaciones.xlsx`.

## Archivos

* `app.py`: Contiene el código fuente de la aplicación.
* `requirements.txt`: Lista de dependencias del proyecto.
* `usuarios.xlsx`: Archivo Excel que registra los usuarios que acceden a la calculadora.
* `operaciones.xlsx`: Archivo Excel que registra las operaciones realizadas por los usuarios.

## Autor

* Marvin, Paola, Kevin.