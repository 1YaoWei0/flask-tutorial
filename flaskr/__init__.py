import os

from flask import Flask

from openai import OpenAI

def create_app(test_config = None):
    # Create and configue the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent = True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register db
    from . import db
    db.init_app(app)

    # a simple page that says hello
    @app.route('/hello/')
    def hello():
        return 'Hello, World!'
    
    @app.route('/aitest/', methods=['GET'])
    def aitest():
        client = OpenAI(api_key="sk-613975d20507407399cb67b54a313504", base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model = "deepseek-chat",
            messages = [
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Hello"}
            ],
            stream = False
        )

        return response.choices[0].message.content

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

    return app