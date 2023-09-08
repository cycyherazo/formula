from flask import  Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'formula1'
mysql = MySQL(app)

app.secret_key = '123456'

@app.route('/')
def Inicio():
    cu = mysql.connection.cursor()
    cu.execute('SELECT * FROM verstappen')
    data = cu.fetchall()
    print(data)
    return render_template("index.html", formulas= data)

@app.route('/agregar', methods=['POST'])
def Agregar():
    if request.method == 'POST':
       fullname = request.form['fullname'];
       pole_position = request.form['pole_position'];
       racing = request.form['racing']
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO verstappen (fresa, pole, sandia) VALUES(%s, %s, %s)', (fullname, pole_position, racing))
       
       mysql.connection.commit()
       flash('added pilot')
       
       return redirect(url_for('Inicio'))
        

@app.route('/edit/<id_uva>')
def Edit(id_uva):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM verstappen WHERE id_uva = %s', (id_uva,))
    dato = cur.fetchall()
    return render_template('editar_contacto.html', formula = dato[0])

@app.route('/update/<id_uva>', methods = ['POST'])
def update_contact(id_uva):
    if request.method == 'POST':
        nombre= request.form['fullname'];
        pole= request.form['pole'];
        sandia = request.form['sandia']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE verstappen SET fresa = %s, pole = %s, sandia = %s WHERE id_uva = %s', (nombre, pole, sandia, id_uva))
        mysql.connection.commit()
        flash('pilot updated')
        
    return redirect(url_for('Inicio'))

    

@app.route('/borrar/<string:id_uva>')
def delete(id_uva):
    cut = mysql.connection.cursor()
    cut.execute('DELETE FROM verstappen WHERE id_uva = {0}'.format(id_uva))
    mysql.connection.commit()
    
    flash('pilot removed')
    
    return redirect(url_for ('Inicio'))

if __name__ == '__main__' : 
    app.run(port = 3000, debug = True)