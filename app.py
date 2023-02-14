from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/ProccessUserInfo/<string:username>', methods=['POST'])
def ProccessUserInfo(username):
    username = json.loads(username)
    return('/')

@app.route('/ProccessUserInfo/<string:password>', methods=['POST'])
def ProccessUserInfo(password):
    password = json.loads(password)
    return('/')

if __name__ == '__main__':
    app.run()

    
