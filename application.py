from flask import Flask, request, jsonify

app = Flask(__name__)


USERS = []  # a list of users instead of a Database.


@app.route('/api/users/', methods=['GET', 'POST'])
def user_list():
    global USERS

    if request.method == "POST":
        user = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'id': len(USERS) + 1
        }
        USERS.append(user)
        return jsonify(user)

    content = {
        'count': len(USERS),
        'results': USERS,
    }
    return jsonify(content)


@app.route('/api/users/<user_id>/', methods=['GET', 'PUT'])
def user_detail(user_id):
    global USERS

    # Handle PUT requests
    if request.method == "PUT":
        for user in USERS:
            if user['id'] == int(user_id):
                user['name'] = request.form.get('name', user['name'])
                user['email'] = request.form.get('email', user['email'])
                return jsonify(user)
        return jsonify({'error': 'User not found'}), 404

    # GET requests
    for user in USERS:
        if user['id'] == int(user_id):
            return jsonify(user)

    return jsonify({'error': 'User not found'}), 404

