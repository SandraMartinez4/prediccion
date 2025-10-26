#!/usr/bin/env bash
# build.sh — Render ejecuta esto antes del despliegue
set -o errexit  # termina si hay un error

# Instala dependencias
pip install -r requirements.txt

# Aplica migraciones de Django
python manage.py migrate

# Recolecta archivos estáticos
python manage.py collectstatic --noinput