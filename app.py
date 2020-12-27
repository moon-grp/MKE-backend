from flask import Flask
from auth.login import loginEndPoint
from actions.uploadproduct import uploadEndPoint
from actions.updateproduct import editEndPoint
from actions.deleteproduct import deleteEndPoint
from actions.viewallproduct import viewallEndPoint
from actions.viewproduct import viewEndPoint
from user.getallproducts import viewallEndPointU
from user.getproduct import viewEndPointU
from user.pay import payEndPointU
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import os


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'mrkayenterpricemrkayframes'  # Change this!
jwt = JWTManager(app)

app.register_blueprint(loginEndPoint, url_prefix="/api/v1/admin")
app.register_blueprint(uploadEndPoint, url_prefix="/api/v1/admin")
app.register_blueprint(editEndPoint, url_prefix="/api/v1/admin")
app.register_blueprint(deleteEndPoint, url_prefix="/api/v1/admin")
app.register_blueprint(viewallEndPoint, url_prefix="/api/v1/admin")
app.register_blueprint(viewEndPoint, url_prefix="/api/v1/admin")
app.register_blueprint(viewallEndPointU, url_prefix="/api/v1/user")
app.register_blueprint(viewEndPointU, url_prefix="/api/v1/user")
app.register_blueprint(payEndPointU, url_prefix="/api/v1/user")


if __name__ == "__main__":
    app.run(debug=True)
