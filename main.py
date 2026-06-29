from flask import Flask, render_template, request
import os
import csv

app = Flask(__name__)

CLIP_FOLDER = os.path.join("static", "clips")
CSV_FILE = "labels.csv"

# Load all clips
clips = sorted(os.listdir(CLIP_FOLDER))

# Ensure CSV exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["clip", "label", "timestamp"])
    labeled_clips = set()  # no CSV yet, start from first clip
else:
    # Load already labeled clips
    labeled_clips = set()
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            labeled_clips.add(row["clip"])

@app.route("/", methods=["GET", "POST"])
def index():
    global labeled_clips

    if request.method == "POST":
        clip = request.form["clip"]
        label = request.form["label"]
        timestamp = request.form.get("timestamp", "")

        # Append to CSV
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([clip, label, timestamp])

        labeled_clips.add(clip)

    # Find next clip not labeled yet
    for clip in clips:
        if clip not in labeled_clips:
            return render_template("index.html", clip=clip)

    return "All clips labeled!"
    

if __name__ == "__main__":
    app.run(debug=True)