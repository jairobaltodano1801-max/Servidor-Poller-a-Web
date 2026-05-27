import os
from flask import Flask, render_template, jsonify

# Inicializamos Flask y le indicamos las carpetas que creaste
app = Flask(__name__, static_folder='static', template_folder='templates')

# Tu diccionario original de combos de la pollería
catalogo_combos = {
    "C001": {"denominacion": "1/4 Pollo a la Brasa + Papas + Ensalada", "precio": 24.90, "stock": True},
    "C002": {"denominacion": "1 Pollo a la Brasa Familiar", "precio": 68.90, "stock": True},
    "C003": {"denominacion": "Parrilla Personal Norkys", "precio": 45.00, "stock": False}
}

# RUTA PRINCIPAL: Cuando alguien entre a tu web, Flask leerá el index.html de /templates
@app.route('/')
def index():
    return render_template('index.html')

# RUTA API: Por si en el futuro usas JavaScript para listar los combos dinámicamente
@app.route('/api/combos')
def get_combos():
    return jsonify(catalogo_combos)

if __name__ == '__main__':
    # El puerto lo asignará el hosting (como Render) dinámicamente en internet
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)