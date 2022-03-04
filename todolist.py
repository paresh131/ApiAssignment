from flask import Flask, jsonify, request
app = Flask(__name__)

list = ["task1", "task2", "task3"]

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Welcome to Todo List!"

@app.route('/get_task', methods=['GET', 'POST'])
def get_task():
    return jsonify(list)

@app.route('/add_task', methods=['POST'])
def add_task():
        
        data = request.json
        name=data['name']
        list.append(name)
        return list



@app.route('/delete_task', methods=['delete'])
def delete_task():
        delete_item=list.pop()
        return delete_item



@app.route('/main', methods=['GET', 'POST'])
def main():
    return "main page! \n"+ list


# if __name__ == '__main__':
app.run(host='0.0.0.0', port=105, debug=True)