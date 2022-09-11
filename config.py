class DevConfig:
    @staticmethod
    def init_app(app):
        app.config['ENV']='development'


class ProdConfig:
    @staticmethod
    def init_app( app):
        pass


configs = {'DEV': DevConfig, 'PROD': ProdConfig,'testing':DevConfig}
