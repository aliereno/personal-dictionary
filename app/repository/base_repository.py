from app import db


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, item_id):
        return self.model.query.filter_by(id=item_id).first()

    def get_by_specific_column(self, **kwargs):
        query = self.model.query
        for key in kwargs:
            query = query.filter(getattr(self.model, key) == kwargs[key])

        return query.first()

    def get_count_by_specific_columns(self, **kwargs):
        query = self.model.query
        for key in kwargs:
            query = query.filter(getattr(self.model, key) == kwargs[key])

        return query.count()

    def get_by_specific_column_order_limit(self, order, limit, **kwargs):
        query = self.model.query
        for key in kwargs:
            query = query.filter(getattr(self.model, key) == kwargs[key])

        return query.order_by(order).limit(limit).all()

    def get_all_by_specific_column(self, **kwargs):
        query = self.model.query
        for key in kwargs:
            query = query.filter(getattr(self.model, key) == kwargs[key])
        return query.all()

    def get_all(self):
        return self.model.query.all()

    def save(self, new_obj):
        db.session.add(new_obj)
        db.session.commit()

    def update(self, id, **kwargs):
        num_rows_updated = self.model.query.filter_by(id=id).update(kwargs)
        db.session.commit()
