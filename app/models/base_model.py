from collections import OrderedDict
from app.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        result = OrderedDict()

        for k in self.__mapper__.attrs.keys():
            result[k] = getattr(self, k)

        return result
