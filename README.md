# Flask docs

Doc for setting up Flask

## Setup

### Install Python

Install Python 3.10

### Install pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Install Flask

```bash
pip install Flask
```

### Install virtualenv

Virtualenv una herramienta para crear entornos virtuales de Python. Esto es útil para aislar las dependencias de un proyecto de las dependencias de otros proyectos.

```bash
pip install virtualenv
```

### Crear una maquina virtual

```bash
virtualenv venv --python=python3.10
```

### Activar la maquina virtual

```bash
source venv/bin/activate
```

- windows

```bash
venv\Scripts\activate

venv/Scripts/activate.ps1
```

### Varaible Flask

Unix

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

window

```bash
set FLASK_APP=app.py
set FLASK_DEBUG=1
```

### Run

```bash
flask run
```

### End virtualenv

```bash
deactivate
```

### Requirements

Si han clonado un proyecto de github y quieren instalar las dependencias, pueden usar el archivo requirements.txt

```bash
pip install -r requirements.txt
```
