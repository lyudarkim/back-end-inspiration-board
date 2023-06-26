from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)

    def to_dict(self):
        return {
            "board_id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }
    
    @classmethod
    def from_dict(cls, board_details):
        new_board = cls(
            title=board_details["title"],
            owner=board_details["owner"]
        )
        return new_board