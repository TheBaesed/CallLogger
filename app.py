from flask import Flask, render_template, request, redirect, url_for
from calls import log_call_db, get_recent_calls, search_calls_db, get_call_by_id
from database import create_table

app = Flask(__name__)
create_table()

@app.route("/")
def index():
    calls = get_recent_calls()
    return render_template("index.html", calls=calls)

@app.route("/log", methods=["GET", "POST"])
def log_call():
    if request.method == "POST":
        caller_name = request.form["caller_name"]
        caller_phone = request.form["caller_phone"]
        caller_address = request.form["caller_address"]
        issue = request.form["issue"]
        troubleshooting = request.form["troubleshooting"]
        resolution = request.form["resolution"]
        agent_name = request.form["agent_name"]

        log_call_db(caller_name, caller_phone, caller_address, issue, troubleshooting, resolution, agent_name)
        return redirect(url_for("index"))

    return render_template("log_call.html")

@app.route("/call/<int:call_id>")
def call_detail(call_id):
    call = get_call_by_id(call_id)
    return render_template("call_detail.html", call=call)

if __name__ == "__main__":
    app.run(debug=True)