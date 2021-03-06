from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from sentry_sdk.integrations.flask import FlaskIntegration

from app.base.db import db
from app.controllers import (
    StudentController,
    StudentLogin,
    CourseController,
    EnrolmentController,
    PhotosController,
    AdditionController,
    SubtractionController,
    MultiplicationController,
    DivisionController,
)

from settings import DB_URL, JWT_SECRET_KEY
import sentry_sdk


def create_app():
    sentry_sdk.init(
        dsn="https://1c8c2eb1ad5e4abf8e1e4fb403c6ceac@o419242.ingest.sentry.io/5854793",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
    )
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    app.config["PROPAGATE_EXCEPTIONS"] = True
    JWTManager(app)

    api = Api(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    api.add_resource(StudentController, "/students/register")
    api.add_resource(StudentLogin, "/students/login")
    api.add_resource(CourseController, "/courses", "/courses/<uuid:pk>")
    api.add_resource(EnrolmentController, "/enrolments")
    api.add_resource(PhotosController, "/photos", "/photos/<uuid:pk>")
    api.add_resource(AdditionController, "/calculator/add")
    api.add_resource(SubtractionController, "/calculator/subtract")
    api.add_resource(MultiplicationController, "/calculator/multiply")
    api.add_resource(DivisionController, "/calculator/divide")

    return app


app = create_app()


@app.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
