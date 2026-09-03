### Tu la hoja de tu archivo excel a usar debe de tener el nombre de "FORMATO PARA NUEVOS CODIGOS"

# Aviso(Windows)
Antes de que uses este programa debes instalar la carpeta de requirements.txt para que no susedan problemas a la hora de correr el programa para eso ve a tu terminal y dirigente a donde se encuentra el archivo de requirements.txt despues copia este comando para crear tu entorno virtual ```python -m venv [nombre_del_entorno]``` despues activalo con ```[nombre_del_entonro]\Scripts\activate.bat``` (si quieres desactivarlo usa solo ```deactivate```) mientras esta activo el entorno usa el siguente comando y se te descargaran todos los paquetes necesarios para iniciar el programa sin problemas.

```bash copy
pip install -r .\requirements.txt
```

Por ultimo NO TE SALGAS DEL ENTORNO VISUAL usa este comando para iniciar el programa.

```bash copy
python reescribir_informacion.py
```


# Aviso(Linux)
Antes de que uses este programa debes instalar la carpeta de requirements.txt para que no susedan problemas a la hora de correr el programa para eso ve a tu terminal y dirigente a donde se encuentra el archivo de requirements.txt despues copia este comando para crear tu entorno virtual ```python3 -m venv [nombre_del_entorno]``` despues activalo con ```source [nombre_del_entonro]/bin/activate``` (si quieres desactivarlo usa solo ```deactivate```) mientras esta activo el entorno usa el siguente comando y se te descargaran todos los paquetes necesarios para iniciar el programa sin problemas.

```bash copy
pip install -r requirements.txt
```

Por ultimo NO TE SALGAS DEL ENTORNO VISUAL usa este comando para iniciar el programa.

```bash copy
python3 reescribir_informacion.py
```

# Copiar plantilla de estructura
Si quieres tener la plantilla de la estructura del proyecto con los archivos de este utiliza ```cookiecutter```. Si no lo tienes instalado ve a tu terminal entra o crea un entorno virtual ```python -m venv [nombre_del_entorno]``` y activalo despues copia este comando:

```bash copy
pip install cookiecutter
```

Al ya tenerlo usa este otro comando para empezar la copia de plantilla. Antes de hacerla te pedira un par de cosas debes de responder todo lo que te pida ```cookiecutter``` antes de crear la copia de la estructura.

```bash copy
cookiecutter https://github.com/ianaoperezliska-eng/work_proyects.git
```
