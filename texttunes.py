from flask import Flask, request, redirect
import sys
sys.path.append("/home/j/jt/jtcramer/.local/lib/python2.7/site-packages/")
import twilio.twiml
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def receive_message():
    text = request.values.get("Body", None)

    resp = twilio.twiml.Response()
    resp.message("You said: " + text)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


