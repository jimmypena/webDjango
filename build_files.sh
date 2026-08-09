#!/bin/bash
echo "=== INICIANDO CONSTRUCCIÓN DE DJANGO ==="
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "=== CONSTRUCCIÓN FINALIZADA ==="