# 📚 End-to-End Book Recommendation System

An interactive, collaborative filtering-based book recommender built using **Streamlit**, **Scikit-learn**, and **pandas**. This system suggests similar books based on user selection using a KNN-based similarity model trained on user ratings.

---

## 🚀 Features

- 🔁 **Trainable Engine**: Retrain the recommendation model directly from the app
- 🔍 **Book Search**: Search or select any book title
- 🎯 **Top Recommendations**: Instantly get 5 similar book recommendations with cover images
- 📊 **Collaborative Filtering**: Uses KNN on pivoted ratings for personalized recommendations
- 🖥️ **Modern UI**: Built with Streamlit and optimized for a clean, intuitive experience

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Scikit-learn, Numpy, Pandas
- **Serialization**: Pickle
- **Logging & Exception Handling**: Custom modules
- **Architecture**: Modular (config, pipeline, logger, exception)

---

## 📂 Project Structure

📁 End-to-End-Book-Recommendation-System/ │ ├── app.py # Streamlit UI & Entry Point ├── templates/ │ └── book_names.pkl # Serialized list of all book titles │ ├── books_recommender/ │ ├── config/ │ │ └── configuration.py # Configuration loader │ ├── logger/ │ │ └── log.py # Logging utility │ ├── pipeline/ │ │ └── training_pipeline.py # Training pipeline logic │ ├── exception/ │ │ └── exception_handler.py # Custom exception class │ └── artifacts/ # Serialized models and pivot tables


---
## Demo

![image](https://github.com/user-attachments/assets/1fac9b4c-1b28-4490-bae0-97320584651b)
![image](https://github.com/user-attachments/assets/8bbe7077-d43e-4b22-be11-69e184e39980)


## 📦 Installation

1. **Clone the repository:**

```bash
[git clone https://github.com/sundaram25018/Book-Recommendation-System
```
2. Create a virtual environment (optional but recommended):
```base
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```base
pip install -r requirements.txt
```
▶️ Run the App
```base
streamlit run app.py
```
## 🙌 Acknowledgements
This app was built as a learning project to understand recommendation systems and build real-world ML-powered applications.

## 📃 License
This project is licensed under the MIT License. See the LICENSE file for details.


