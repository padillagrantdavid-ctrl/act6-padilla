from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

STUDENT_PROFILE = {
	"student_id": "24-00170",
	"name": "Grant David Padilla",
	"program": "BSIT",
	"year": 3,
	"section": "B",
}


@app.route("/")
def home():
	return render_template("index.html")


@app.route("/student")
def get_student():
	return jsonify(STUDENT_PROFILE)


@app.route("/hello")
def say_hello():
	name = request.args.get("name", "Student")
	return jsonify({"message": f"Hello, {name}!"})


@app.route("/academic")
def get_academic_profile():
	return jsonify(
		{
			"student_id": STUDENT_PROFILE["student_id"],
			"name": STUDENT_PROFILE["name"],
			"program": STUDENT_PROFILE["program"],
			"year": STUDENT_PROFILE["year"],
			"section": STUDENT_PROFILE["section"],
		}
	)


if __name__ == "__main__":
	app.run(debug=True)