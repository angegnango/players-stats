import os
from flask import Flask, jsonify, request, abort, render_template
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from api.services import crud
from api.services.feature import retrieve_player_stat
from api.middlewares import auth
from api.middlewares.auth import auth_required

def init_server():
    
    # Create application
    app = Flask(__name__)
    CORS(app)

    #  mongodb config
    app.config["MONGODB_SETTINGS"] = {'DB': "database", "host": "mongodb+srv://db_user:db_password@cluster0.xtkvx.mongodb.net/database?retryWrites=true&w=majority"}

    db = MongoEngine(app)

    # Endpoints API
    @app.route('/api/docs')
    def docs():
        return render_template('swagger-ui.html')

    @app.route('/api/token', methods=['POST'])
    def generate_token():
        payload = request.get_json()
        token = auth.generate_token(payload)
        return jsonify(token), 201


    @app.route('/api/players', methods=['GET'])
    @auth_required
    def get():
        players = crud.all()
        return jsonify(players)
    

    @app.route('/api/players', methods=['POST'])
    @auth_required
    def create():
        payload = request.get_json()
        player = crud.create(payload)
        if isinstance(player, str):
            return jsonify({'error': player}), 400
        else:
            return jsonify(player), 200


    @app.route('/api/players/<nickname>', methods=['PUT'])
    @auth_required
    def update(nickname:str):
        payload = request.get_json()
        player = crud.update(nickname, payload)
        if isinstance(player, str):
            abort(404)
        else:
            return jsonify(player), 201
        

    @app.route('/api/players/<nickname>', methods=['DELETE'])
    @auth_required
    def destroy(nickname:str):
        crud.destroy(nickname)
        return jsonify({}), 204


    @app.route('/api/players/stats/<nickname>', methods=['GET'])
    @auth_required
    def stats(nickname:str):
        player_stats = retrieve_player_stat(nickname)
        if isinstance(player_stats, str):
            abort(404)
        else:
            stat = crud.store_stats(nickname, player_stats)
            return jsonify(stat), 200
        

    return app