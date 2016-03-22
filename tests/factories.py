import factory

from database import db, Document


class SQLAlchemyModelFactory(factory.Factory):

    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = db.session
        session.begin(nested=True)
        obj = model_class(*args, **kwargs)
        session.add(obj)
        session.commit()
        return obj


class DocumentFactory(SQLAlchemyModelFactory):

    class Meta:
        model = Document

    data = factory.LazyAttribute(lambda x: dict())
