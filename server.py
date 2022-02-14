from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "Oreo"

@app.route('/')
def default():
    if 'visits' in session:
        counter = session['visits']
        session['visits'] = counter + 1
        return render_template('index.html', visits = session['visits'])
    else:
        counter = 1
        session['visits'] = counter
        return render_template('index.html', visits = session['visits'])

@app.route('/process', methods=['POST'])
def counter():
    if 'increment' in request.form:
        counter = session['visits']
        session['visits'] = counter + 1
        return redirect('/')
    else:
        session.clear()
        return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)