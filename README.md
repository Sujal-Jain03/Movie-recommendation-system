# Movie Recommendation System

A Streamlit web app that takes a movie as input and suggests 5 similar movies.

## How it works

The app loads a movies dataset (`movies.pickle`) and a precomputed similarity
matrix (`similarity.joblib`). When you pick a movie, it looks up that movie's
row in the similarity matrix, sorts the other movies by similarity score, and
returns the top 5.

## Features

- Dropdown list of all movies in the dataset
- One-click recommendations — 5 similar movies per selection
- Simple Streamlit interface, no database or API calls needed

## Tech stack

- Python
- Streamlit — web UI
- pandas — movie data handling
- scikit-learn, nltk, joblib — supporting libraries

## Project structure

```
Movie-recommendation-system/
├── app.py             # Streamlit app
├── movies.pickle      # Movie dataset (pandas DataFrame)
├── similarity.joblib  # Precomputed movie similarity matrix
└── requirements.txt   # Dependencies
```

## How to run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL shown in the terminal, pick a movie from the dropdown,
and click **Recommend**.

## Notes

- The similarity matrix is precomputed and shipped with the repo; this project
  contains the app only, not the code that built the matrix.
- A learning project built to practise content-based recommendation and
  Streamlit.
