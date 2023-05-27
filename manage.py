from codes import app
from config.configManager import host, port, debug


if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)
