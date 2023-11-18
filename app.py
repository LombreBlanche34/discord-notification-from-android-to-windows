from flask import Flask, request
from win10toast import ToastNotifier

app = Flask(__name__)
toaster = ToastNotifier()

@app.route("/", methods=["GET"])
def home():
    return "main server for discord notification<br>usage: POST /notif {title:, message:}"


@app.route("/notif", methods=["POST"])
def notif():
    data = request.get_json()
    print(data)
    user = data.get("title")
    message = data.get("message")
    toaster.show_toast(title=user, msg=message, duration=10)
    return "notification send"


if __name__ == '__main__':
    app.run(host="192.168.0.33", port=5000)