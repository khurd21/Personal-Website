import dataclasses
import app.model as md
from app import session

from dataclasses import dataclass

@dataclass
class Song:
    artist  : str
    mp3     : str
    pdf     : str



### Contemplating if this is worth doing. I won't be making that many tabs

class Tab(md.Base):
    __tablename__ = 'tab'

    id      = md.Column(md.Integer, md.Sequence('tab_id_seq'), primary_key=True)
    mp3     = md.Column()
    pdf     = md.Column()