# Importamos Flask y la función render_template para poder mostrar archivos HTML
from flask import Flask, render_template

# Creamos la aplicación de Flask y la guardamos en una variable llamada 'app'
app = Flask(__name__)

# Definimos qué pasará cuando alguien entre a la página principal (la raíz '/')
@app.route('/')
def inicio():
    # Le decimos a Flask que busque el archivo 'index.html' dentro de la carpeta 'templates' y lo muestre
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)