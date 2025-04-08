import os
import sys
import pickle
import streamlit as st
import numpy as np
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.exception.exception_handler import AppException


class Recommendation:
    def __init__(self, app_config=AppConfiguration()):
        try:
            self.recommendation_config = app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    def fetch_poster(self, suggestion):
        try:
            book_name = []
            ids_index = []
            poster_url = []
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))
            final_rating = pickle.load(open(self.recommendation_config.final_rating_serialized_objects, 'rb'))

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])

            for name in book_name[0]:
                ids = np.where(final_rating['title'] == name)[0][0]
                ids_index.append(ids)

            for idx in ids_index:
                url = final_rating.iloc[idx]['image_url']
                poster_url.append(url)

            return poster_url

        except Exception as e:
            raise AppException(e, sys) from e

    def recommend_book(self, book_name):
        try:
            books_list = []
            model = pickle.load(open(self.recommendation_config.trained_model_path, 'rb'))
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))
            book_id = np.where(book_pivot.index == book_name)[0][0]
            distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

            poster_url = self.fetch_poster(suggestion)

            for i in range(len(suggestion)):
                books = book_pivot.index[suggestion[i]]
                for j in books:
                    books_list.append(j)
            return books_list, poster_url

        except Exception as e:
            raise AppException(e, sys) from e

    def train_engine(self):
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            st.success("✅ Training Completed Successfully!")
            logging.info(f"Recommended successfully!")
        except Exception as e:
            raise AppException(e, sys) from e

    def recommendations_engine(self, selected_books):
        try:
            recommended_books, poster_url = self.recommend_book(selected_books)

            st.markdown("---")
            st.subheader("📚 Recommended Books for You")

            cols = st.columns(5)
            for i in range(1, 6):
                with cols[i - 1]:
                    st.image(poster_url[i], use_column_width=True)
                    st.markdown(f"**{recommended_books[i]}**", unsafe_allow_html=True)

        except Exception as e:
            raise AppException(e, sys) from e


if __name__ == "__main__":
    st.set_page_config(page_title="📖 Book Recommendation System", layout="wide")
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>📚 End-to-End Book Recommender</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>A collaborative filtering-based recommendation system built with love ❤️</p>", unsafe_allow_html=True)

    obj = Recommendation()

    with st.sidebar:
        st.header("⚙️ Options")
        if st.button('🔁 Train Recommender System'):
            obj.train_engine()

    st.markdown("### 🔍 Select a book to get recommendations:")
    book_names = pickle.load(open(os.path.join('templates', 'book_names.pkl'), 'rb'))
    selected_books = st.selectbox(
        "Type or select a book from the dropdown below:",
        book_names,
        index=0,
        help="Start typing to search for a book..."
    )

    if st.button('🎯 Show Recommendations'):
        obj.recommendations_engine(selected_books)
