from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    from .routes.job_routes import job_bp
    app.register_blueprint(job_bp)

    return app
