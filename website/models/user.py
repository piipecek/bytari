from website import db, create_app
from flask_login import UserMixin
from sqlalchemy import select, text

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    
    def __repr__(self) -> str:
        return f"Uživatel | {self.email}"
    
    @staticmethod
    def get_by_email(email) -> "User":
        # app = create_app()
        # with app.app_context():
        #     db.session.execute(text('SELECT 1'))
        #     if User.__table__.exists():
        #         print("all good")
        return db.session.scalars(select(User).where(User.email == email)).first()