# Para generar el archivo requirements.txt si no desea trabajar con poetry

#-----------------------------------Poetry----------------------------------
# Poetry es una herramienta para la gestión de dependencias y el empaquetado en Python. Le permite declarar 
# las bibliotecas de las que depende su proyecto y las administrará (instalará / actualizará) por usted.

#-----------------------------------Instalar---------------------------------
# Linux: curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# powershell: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
poetry export -f requirements.txt --without-hashes > requirements.txt

# Con dependencias de desarrollo
# poetry export -f requirements.txt --without-hashes --dev > requirements.txt