from flask import Blueprint, request, jsonify, make_response
from app import db

from app.models.board import Board
# from app.models.card import Card

boards_bp = Blueprint('boards', __name__, url_prefix="/boards")
cards_bp = Blueprint('cards', __name__, url_prefix="/cards")

# Read all boards
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

# Post one board
@boards_bp.route("",methods=['POST'])
def create_board():
    request_body = request.get_json()
    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return {
        "board_id": new_board.board_id,
        "title": new_board.title,
        "owner": new_board.owner,
        "msg": "Successfully created"
    }, 201


# Read one board
@boards_bp.route("/<board_id>", methods=['GET'])
def get_one_board(board_id):
    board = get_valid_item_by_id(Board, board_id)
    return board.to_dict(), 200


# Get all cards


# Create a card

# Delete a card


