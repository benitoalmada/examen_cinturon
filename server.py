from flask_app import app

from flask_app.controllers import usuarios
from flask_app.controllers import posteos


if __name__ == "__main__":
    app.run(debug=True)
