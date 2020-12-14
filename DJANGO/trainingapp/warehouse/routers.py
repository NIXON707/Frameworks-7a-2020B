class WareHouseRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'warehose' :
            return 'warehouse'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'warehose' :
            return 'warehouse'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hint):
        if app_label == 'warehouse' :
            return db == 'warehouse'
        return None