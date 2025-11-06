from comunidadeimpressionadora import app
from comunidadeimpressionadora.criarbanco import db


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    from comunidadeimpressionadora import routes
    app.run(debug=True)