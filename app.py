from flask import Flask, render_template

app = Flask(__name__)

# 👇 ESTA LÍNEA ES CRUCIAL PARA VERCEL: Le dice explícitamente qué usar
app.index = app 

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)