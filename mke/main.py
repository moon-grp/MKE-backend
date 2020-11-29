from flask import Flask
from auth.login import loginEndPoint
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'mrkayenterpricemrkayframes'  # Change this!
jwt = JWTManager(app)

app.register_blueprint(loginEndPoint, url_prefix="/api/v1")


if __name__ == "__main__":
    app.run(debug=True)
