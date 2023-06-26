from flask import Blueprint, request, jsonify, make_response
from app import db

from app.models.board import Board
from app.models.card import Card

boards_bp = Blueprint('boards', __name__, url_prefix="/boards")
cards_bp = Blueprint('cards', __name__, url_prefix="/cards")

# Create a new board
@boards_bp.route("", methods=['GET'])
def get_boards():
    title_query = request.args.get("title")
    if title_query:
        boards = Board.query.filter_by(title=title_query)
    else:
        boards = Board.query.all()

    boards_response = []
    for board in boards:
        boards_response.append(board.to_dict())
    return jsonify(boards_response), 200

# Read one board

# Read all boards


# Get all cards


# Create a card

# Delete a card


