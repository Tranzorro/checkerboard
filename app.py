from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def defaultboard():
    rows = 8
    columns = 8
    return render_template('index.html', rows = rows, columns = columns)

@app.route('/<rows>/<columns>')
def checkerboardchanger(rows, columns):
    return render_template("index.html", rows = int(rows), columns = int(columns))

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "hello," + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__ == "__main__":
    app.run(debug=True)