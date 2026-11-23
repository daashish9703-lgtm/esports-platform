from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.get("/")
def index():
    return {"message": "Esports Platform API"}


if __name__ == "__main__":
    app.run(debug=True)
