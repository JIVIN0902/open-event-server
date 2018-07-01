from app.models import db
from app.models.base import SoftDeletionModel


class SocialLink(SoftDeletionModel):
    __tablename__ = "social_links"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id', ondelete='CASCADE'))
    event = db.relationship("Event", backref="social_link")

    def __init__(self, name=None, link=None, event_id=None, deleted_at=None):
        self.name = name
        self.link = link
        self.event_id = event_id
        self.deleted_at = deleted_at

    def __repr__(self):
        return '<SocialLink %r>' % self.name

    def __str__(self):
        return self.__repr__()

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {'id': self.id, 'name': self.name, 'link': self.link}