from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Enkel konfigurasjon, kan utvides senere
    app.config.from_mapping(
        SECRET_KEY='dev', # Bør endres for produksjon
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Sikre at instance folder eksisterer
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    with app.app_context():
        from . import routes
        # app.register_blueprint(routes.bp) # Hvis vi bruker blueprints

    return app
