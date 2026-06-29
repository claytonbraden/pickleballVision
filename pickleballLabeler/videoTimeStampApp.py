from flask import Flask, render_template, request, jsonify
import json
import os


app = Flask(__name__)

DATA = "annotations.json"


def get_last_timestamp():

    if not os.path.exists(DATA):
        return 0

    try:
        with open(DATA, "r") as f:
            events = json.load(f)

    except json.JSONDecodeError:
        return 0


    if len(events) == 0:
        return 0


    return events[-1]["timestamp"]


@app.route("/")
def index():

    last_time = get_last_timestamp()

    return render_template(
        "index.html",
        start_time=last_time
    )



@app.route("/log", methods=["POST"])
def log_event():

    data = request.json


    # Load existing events safely
    if not os.path.exists(DATA):
        events = []

    else:
        try:
            with open(DATA, "r") as f:
                events = json.load(f)

        except json.JSONDecodeError:
            events = []


    # add new label
    events.append({
        "timestamp": data["timestamp"],
        "state": data["state"]
    })


    # save
    with open(DATA, "w") as f:
        json.dump(
            events,
            f,
            indent=4
        )


    return jsonify({"success": True})



if __name__ == "__main__":
    app.run(debug=True)