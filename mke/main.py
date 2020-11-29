from flask import Flask
from auth.login import loginEndPoint

app = Flask(__name__)

app.register_blueprint(loginEndPoint, url_prefix="/api/v1")


if __name__ == "__main__":
    app.run(debug=True)
