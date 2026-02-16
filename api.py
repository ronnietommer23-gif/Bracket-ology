#!/usr/bin/env python3
"""
Bracket Matrix API Server
Serves bracket data via REST API
"""

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

DATA_FILE = 'bracket_data.json'

def load_data():
    """Load bracket data from JSON file"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


@app.route('/api/brackets', methods=['GET'])
def get_brackets():
    """Get all bracket data"""
    data = load_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Data not found'}), 404


@app.route('/api/teams', methods=['GET'])
def get_teams():
    """Get just team data"""
    data = load_data()
    if data:
        return jsonify({
            'teams': data.get('teams', []),
            'last_updated': data.get('last_updated', '')
        })
    else:
        return jsonify({'error': 'Data not found'}), 404


@app.route('/api/bracketologists', methods=['GET'])
def get_bracketologists():
    """Get bracketologist information"""
    data = load_data()
    if data:
        return jsonify({
            'bracketologists': data.get('bracketologists', []),
            'update_dates': data.get('update_dates', [])
        })
    else:
        return jsonify({'error': 'Data not found'}), 404


@app.route('/api/team/<team_name>', methods=['GET'])
def get_team(team_name):
    """Get data for a specific team"""
    data = load_data()
    if data:
        for team in data.get('teams', []):
            if team['team'].lower() == team_name.lower():
                return jsonify(team)
        return jsonify({'error': 'Team not found'}), 404
    else:
        return jsonify({'error': 'Data not found'}), 404


@app.route('/api/update', methods=['POST'])
def update_data():
    """Endpoint to trigger data refresh (calls scraper)"""
    # This would call the scraper script
    # For now, just reload the file
    data = load_data()
    if data:
        return jsonify({
            'status': 'success',
            'message': 'Data reloaded',
            'teams': len(data.get('teams', []))
        })
    else:
        return jsonify({'error': 'Failed to reload data'}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    print("Starting Bracket Matrix API Server...")
    print("API available at http://localhost:5000")
    print("Endpoints:")
    print("  GET  /api/brackets - Get all data")
    print("  GET  /api/teams - Get team data")
    print("  GET  /api/bracketologists - Get expert info")
    print("  GET  /api/team/<name> - Get specific team")
    print("  POST /api/update - Refresh data")
    app.run(debug=True, host='0.0.0.0', port=5000)
