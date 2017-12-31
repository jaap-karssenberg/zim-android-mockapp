print('LALALALO')

import os
from .flask import Flask, url_for, render_template, jsonify, request, make_response
import webview
import webbrowser
import app

pages_dir = os.path.join(os.getcwd(), "pages")  # development path
if not os.path.exists(pages_dir):  # frozen executable path
    pages_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")

server = Flask(__name__, static_folder=pages_dir, template_folder=pages_dir)
server.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1  # disable caching


@server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


@server.route("/init")
def initialize():
    """
    Perform heavy-lifting initialization asynchronously.
    :return:
    """
    can_start = app.initialize()

    if can_start:
        response = {
            "status": "ok",
        }
    else:
        response = {
            "status": "error"
        }

    return jsonify(response)


@server.route("/")
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template("index.html")


@server.route('/', defaults={'path': ''})
@server.route('/<path:path>')
def other_pages(path):
    """
    Catch all other URLs that are not already caught by specific cases, this enables link clicking.
    """
    return render_template(path)


@server.route("/choose/path")
def choose_path():
    """
    Invoke a folder selection dialog here
    :return:
    """
    dirs = webview.create_file_dialog(webview.FOLDER_DIALOG)
    if dirs and len(dirs) > 0:
        directory = dirs[0]
        if isinstance(directory, bytes):
            directory = directory.decode("utf-8")

        response = {"status": "ok", "directory": directory}
    else:
        response = {"status": "cancel"}

    return jsonify(response)


@server.route("/fullscreen")
def fullscreen():
    webview.toggle_fullscreen()
    return jsonify({})


@server.route("/open-url", methods=["POST"])
def open_url():
    url = request.json["url"]
    webbrowser.open_new_tab(url)

    return jsonify({})


@server.route("/do/stuff")
def do_stuff():
    result = app.do_stuff()

    if result:
        response = {"status": "ok", "result": result}
    else:
        response = {"status": "error"}

    return jsonify(response)


def run_server():
    server.run(host="127.0.0.1", port=23950, threaded=True)


if __name__ == "__main__":
    run_server()
