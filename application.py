from flask import Flask, request, jsonify

app = Flask(__name__)

# We'll use this of users as our "database" (this example just stores
# data in memory). The caveat here is that our data will disappear when
# the server is stopped.
USERS = []


@app.route('/api/users/', methods=['GET', 'POST'])
def user_list():
    """This endpoint gives you a list of all the data in our list of USERS.
    It also accepts a POST request allowing you to create a User.

    A User should have the following attributes:

    - name
    - email
    - id (the id will be generated automatically)

    """
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
    """This endpoint gives you details for a single User. It also accepts
    PUT requests in order to update a User.

    """
    # Handle PUT requests
    if request.method == "PUT":
        for user in USERS:
            if user['id'] == int(user_id):
                user['name'] = request.form.get('name', user['name'])
                user['email'] = request.form.get('email', user['email'])
                return jsonify(user)
        return jsonify({'error': 'User not found'}), 404

    # TODO: Handle DELETE requests.

    # GET requests
    for user in USERS:
        if user['id'] == int(user_id):
            return jsonify(user)

    return jsonify({'error': 'User not found'}), 404
