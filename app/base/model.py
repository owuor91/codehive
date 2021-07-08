import datetime
import logging

from sqlalchemy import Column, DateTime, String, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from app.db import db


class BaseModel:
    date_created = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.now
    )
    date_updated = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    created_by = Column(String(100), nullable=False)
    updated_by = Column(String(100), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    meta = Column(JSON, nullable=True, default=dict, server_default="{}")

    def save(self):
        session = db.session
        try:
            session.add(self)
            session.commit()
        except Exception as exc:
            session.rollback()
            logging.exception(exc)
            return exc
        return self

    def get(self, pk=None):
        session = db.session
        if pk:
            return session.query(self).get(pk)
        else:
            return session.query(self).all()

    def delete(self, updated_by):
        self.deleted_at = datetime.datetime.now()
        self.active = False
        self.updated_by = updated_by
        return self.save()

    def set_model_dict(self, model_dict):
        for k, v in model_dict.items():
            getattr(self, k, setattr(self, k, v))


Base = declarative_base(cls=BaseModel)
