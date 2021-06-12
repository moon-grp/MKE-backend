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
from actions.vieworders import viewOrderEndPointU
from autos.admin.createpost import autosAdminCEndPoint
from actions.processorder import pOrderEndPointU
from autos.refs.signup import signUpEndPoint
from autos.refs.signin import signInEndPoint
from autos.refs.profile import createProfileEndPoint
from autos.admin.deletepost import deleteEndPointC
from autos.admin.updatepost import editEndPointC
from autos.admin.viewposts import viewallEndPointC
from autos.admin.viewpost import viewEndPointC
from autos.refs.viewgarage import viewCarDetailsEndPointC
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import os
from flask_cors import CORS


app = Flask(__name__)

app.config['CORS_HEADERS'] = "Content-Type"
app.config['CORS_RESOURCES'] = {r"/api/*": {"origins": "*"}}
CORS(app)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_S_KEY")
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
app.register_blueprint(viewOrderEndPointU, url_prefix="/api/v1/user")
app.register_blueprint(pOrderEndPointU, url_prefix="/api/v1/user")
app.register_blueprint(autosAdminCEndPoint, url_prefix="/api/v1/autos")
app.register_blueprint(signUpEndPoint, url_prefix="/api/v1/autos")
app.register_blueprint(signInEndPoint, url_prefix="/api/v1/autos")
app.register_blueprint(createProfileEndPoint, url_prefix="/api/v1/autos")

app.register_blueprint(deleteEndPointC, url_prefix="/api/v1/autos")
app.register_blueprint(editEndPointC, url_prefix="/api/v1/autos")
app.register_blueprint(viewallEndPointC, url_prefix="/api/v1/autos")
app.register_blueprint(viewEndPointC, url_prefix="/api/v1/autos")
app.register_blueprint(viewCarDetailsEndPointC, url_prefix="/api/v1/autos")


if __name__ == "__main__":
    app.run(debug=True)
