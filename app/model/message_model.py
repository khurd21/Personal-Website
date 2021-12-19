import app.model as md
from app import session
from app.model.validators import MessageValidate

class Message(md.Base):
    __tablename__ = 'message'

    id      = md.Column(md.Integer, md.Sequence('message_id_seq'), primary_key=True)
    name    = md.Column(md.String(32),   nullable=False)
    email   = md.Column(md.String(32),   nullable=False)
    message = md.Column(md.String(1028), nullable=False)

    validators = MessageValidate()

    def __repr__(self):
        return f'<Message id: {self.id} name: {self.name} email: {self.email}>'

    
    def save_to_db(self):
        session.add(self)
        session.commit()


    def populate(self, form):

        new_items = {
            self.validators.NAME   : form.get('name'),
            self.validators.EMAIL  : form.get('email'),
            self.validators.MESSAGE: form.get('message'),
        }

        if not self.validators.validate(new_items):
            return False

        self.name = new_items[self.validators.NAME]
        self.email = new_items[self.validators.EMAIL]
        self.message = new_items[self.validators.MESSAGE]
        self.save_to_db()
        return True


