from flask_login import UserMixin
import app.model as md
from app import session

from werkzeug.security import generate_password_hash, check_password_hash


class Admin(md.Base, UserMixin):
    __tablename__ = 'admin'

    id            = md.Column(md.Integer, md.Sequence('admin_id_sequence'), primary_key=True)
    username      = md.Column(md.String(16), unique=True, nullable=False)
    password_hash = md.Column(md.String(128), nullable=False)


    def __repr__(self):
        return f'<Admin id: {self.id} user: {self.username}>'


    def save_to_db(self):
        session.add(self)
        session.commit()


    def set_password(self, pwd):
        self.password_hash = generate_password_hash(pwd)


    def check_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)