import os   
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.clean_text import clean_text
import docx2txt

def extract_text_from_jd(file):
    if file.filename.endswith('.txt'):
        return file.read().decode("utf-8")
    elif file.filename.endswith('.docx'):
        return docx2txt.process(file)
    else:
        raise ValueError("Unsupported file type")

def match_resume_to_jd(resume_text, jd_text):
    # Clean both texts
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_clean, jd_clean])

    # Compute cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

    # Extract matched keywords
    resume_tokens = set(resume_clean.split())
    jd_tokens = set(jd_clean.split())
    matched_keywords = list(resume_tokens.intersection(jd_tokens))

    return {
        "matched_keywords": sorted(matched_keywords),
        "similarity_score": round(similarity, 2)
    }
