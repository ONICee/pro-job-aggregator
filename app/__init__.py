from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register API Blueprints
    from .routes.job_routes import job_bp
    app.register_blueprint(job_bp)

    # Register UI Blueprints
    from .routes.ui_routes import ui_bp
    app.register_blueprint(ui_bp)



# just added
    from flask import render_template
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404


    return app
