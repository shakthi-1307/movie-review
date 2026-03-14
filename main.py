from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal
import joblib

vectorizer = joblib.load(r"tfidf_vectorizer.pkl")
model = joblib.load(r"sentiment_model.pkl")
app = FastAPI()

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/review")
def add_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):

    text = [review.review]

    X = vectorizer.transform(text)

    pred = model.predict(X)[0]

    sentiment = "positive" if pred == 1 else "negative"

    new_review = models.Review(
        movie=review.movie,
        rating=review.rating,
        review=review.review
    )

    db.add(new_review)
    db.commit()

    return {
        "message": "Review saved",
        "sentiment": sentiment
    }

@app.get('/reviews')
def get_reviews(db:Session = Depends(get_db)):
    return db.query(models.Review).all()

@app.get("/reviews/{movie_name}")
def get_reviews(movie_name: str, db: Session = Depends(get_db)):
    reviews = db.query(models.Review).filter(models.Review.movie == movie_name).all()
    return reviews


    