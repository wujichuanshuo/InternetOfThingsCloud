from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/SensorInformation', methods=['GET', 'Post'])
def getSensorInfo():
    name = 'all'
    if name is 'all':
        info = {'x':[1,2,3,4,5],'y':[2,3,4,5],'title':'123','company':'%'}
        info1 = [info,info,info,info]
        return json.dumps(info1)


if __name__ == '__main__':
    app.run(host='localhost')
