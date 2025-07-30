from flask import Flask, request, jsonify, render_template
from parser.jd_matcher import extract_text_from_jd, match_resume_to_jd
import fitz  # PyMuPDF

app = Flask(__name__)

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

@app.route("/")
def home():
    print("✅ Home route reached")
    return render_template("index.html", result=None)

@app.route("/jd-matcher", methods=["POST"])
def match_jd():
    if 'resume' not in request.files or 'jd' not in request.files:
        return jsonify({"error": "Both resume and JD files are required."}), 400

    resume_file = request.files["resume"]
    jd_file = request.files["jd"]

    try:
        resume_text = extract_text_from_pdf(resume_file)
        jd_text = extract_text_from_jd(jd_file)

        result = match_resume_to_jd(resume_text, jd_text)

        return render_template("results.html", matched_keywords=result["matched_keywords"], similarity_score=result["similarity_score"])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
