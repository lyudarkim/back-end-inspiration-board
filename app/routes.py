from flask import Blueprint, request, jsonify, make_response
from app import db

boards_bp = Blueprint('boards', __name__, url_prefix="/boards")
cards_bp = Blueprint('cards', __name__, url_prefix="/cards")

# Create a new board


# Read one board

# Read all boards


# Get all cards


# Create a card

# Delete a card


