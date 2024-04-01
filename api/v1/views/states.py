from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage, State

@app_views.route('/states', methods=['GET'])
def Get_sates():
    """Retrieve an object into a valid JSON"""
    state = [state.to_dict() for state in storage.all(State).values]
    return jsonify(state)

@app_views.route('/states/<state_id>', methods=['GET'])
def Getob_sates(states_id):
    state = storage.get(State, states_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DETATE'])
def Delete_states(states_id):
    state = storage.get(State, states_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify([]), '200'

@app_views.route('/states', methods=['POST'])
def Post_states()
