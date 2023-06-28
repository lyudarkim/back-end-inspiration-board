from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer, default=0)
    board_id = db.Column(db.Integer, db.ForeignKey("board.board_id"), nullable=False)
    board = db.relationship("Board", back_populates="cards")
    
    def to_dict(self):
        card_dict = {
            "card_id": self.card_id,
            "message": self.message,
            "board_id": self.board_id
        }

        return card_dict
    
    @classmethod
    def from_dict(cls, card_details):
        new_card = cls(
            message=card_details["message"],
            board_id=card_details["board_id"])
        return new_card