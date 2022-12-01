
import json
from flask import Flask, render_template, request
import magic


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/converter_1', methods=['POST', 'GET'])
def convert_1():
    inp = request.get_json()
    res = json.loads(inp)
    elem = res['item']
    step = magic.work_1(elem)
    result = {'item': step}
    end = json.dumps(result)
    return end

@app.route('/converter_2', methods=['POST', 'GET'])
def convert_2():
    inp = request.get_json()
    res = json.loads(inp)
    elem = res['item']
    step = magic.work_2(elem)
    result = {'item': step}
    end = json.dumps(result)
    return end


if __name__ == '__main__':
    app.run()

