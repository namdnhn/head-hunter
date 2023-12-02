from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.models.job import JobModel
from database import Session

def compute_similarity(job1, job2):
    # Combine text attributes (position, description, location, job requirement)
    text1 = f"{job1.position} {job1.description} {job1.location} {job1.job_requirement}"
    text2 = f"{job2.position} {job2.description} {job2.location} {job2.job_requirement}"

    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    
    # Fit and transform the texts into TF-IDF vectors
    tfidf_matrix = tfidf_vectorizer.fit_transform([text1, text2])

    # Compute the cosine similarity between the two vectors
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return similarity[0][0]

# Example usage
def main():
    session = Session()
    job1 = session.query(JobModel).filter_by(id=1).first()
    job2 = session.query(JobModel).filter_by(id=2).first()
    print(job1)
    if job1 and job2:   
        similarity_score = compute_similarity(job1, job2)
        print(f"Similarity Score: {similarity_score}")

if __name__ == "__main__":
    main()
