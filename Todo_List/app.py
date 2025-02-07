from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'todos' not in session:
        session['todos'] = []
    
    if request.method == 'POST':
        todo = request.form.get('todo')
        if todo.strip():
            session['todos'] = session['todos'] + [{'task': todo, 'done': False}]
            session.modified = True
    
    return render_template('index.html', todos=session['todos'])

@app.route('/delete/<int:index>')
def delete(index):
    if 'todos' in session and 0 <= index < len(session['todos']):
        session['todos'].pop(index)
        session.modified = True
    return redirect('/')

@app.route('/done/<int:index>')
def done(index):
    if 'todos' in session and 0 <= index < len(session['todos']):
        session['todos'][index]['done'] = not session['todos'][index]['done']
        session.modified = True
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)