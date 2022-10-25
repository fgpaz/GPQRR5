# Web scraper de mercadolibre, venex, compragamer y Amazon
En este proyecto realizaremos un web scraper para cada una de las páginas web mencionadas y luego realizaremos una comparativa de precios.

## Recomendaciones
Recomiendo utilizar [pipenv](https://pipenv.pypa.io/en/latest/) para manejar el entorno virtual en el cual estaremos trabajando.

## Instalación y configuración del entorno virtual
Primero necesitamos instalar [pipenv](https://pipenv.pypa.io/en/latest/), en caso de tenerlo ya instalado se puede omitir este paso.
```python
pip install pipenv
```
En caso de querer comprobar si lo tenemos instalado, podemos hacerlo desde la consola, con el comando:
```bash
[~]$ pipenv --version
pipenv, version 2022.9.8
```
Una vez instalada la herramienta con la que controlaremos nuestro entorno virtual, necesitamos clonar el repositorio del [proyecto](https://github.com/ispc-programador2022/GPQRR5.git) para luego movernos con 'cd' hasta la ubicación del mismo. Una vez dentro del directorio del proyecto, podemos ejecutar el entorno virtual de la siguiente manera
```bash
# Iniciamos el entorno virtual
$ pipenv shell
# Instalamos las dependencias necesarias
$ pipenv install -r requirements.txt
# Para desactivar el entorno virtual utilizaremos 
$ deactivate

```
El proceso puede demorar, cuando termine de ejecutar ya tendremos todas las dependencias necesarias para trabajar con el proyecto instaladas
### Integrantes:
    -Agustin Piccoli
    -Lina Mikaela Gutierrez Arribas
    -Lourdes Reynaldo
    -Horacio Quiroga
    -Ignacio Rocha