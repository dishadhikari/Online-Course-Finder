# 🎓 Course-O-Rama — Smart Online Course Recommendation System 🚀

**Course-O-Rama** is an intelligent online course discovery platform that helps learners find the most relevant courses based on their interests or a specific course topic. Using **Natural Language Processing (NLP)** and **Machine Learning**, the system analyzes user input and recommends similar courses from a curated dataset of online learning resources.

Built with ❤️ using **Python, Flask, Scikit-learn, NLTK, and Pandas**.

🌐 **GitHub Repository:** https://github.com/your-username/course-o-rama

---

## 🧭 Table of Contents

1. Overview
2. Key Features
3. Architecture
4. Tech Stack
5. System Modules
6. Installation & Setup
7. Dataset Information
8. Usage Guide
9. Future Enhancements
10. Contributing
11. Author
12. License

---

## 📖 Overview

With thousands of online courses available across multiple learning platforms, finding the right course can be overwhelming. **Course-O-Rama** simplifies this process by using Machine Learning-based recommendation techniques to suggest courses that match a user's interests and learning goals.

The application offers two recommendation modes:

- 🎯 **Interest-Based Recommendations** – Users enter multiple areas of interest and receive personalized course suggestions.
- 📚 **Course-Based Recommendations** – Users search for a course title and discover similar courses.

By leveraging NLP preprocessing and K-Nearest Neighbors (KNN), Course-O-Rama provides accurate and meaningful recommendations from a large course dataset.

> ⚡ *Our goal is to make online learning more accessible by helping learners discover the best courses tailored to their interests.*

---

# 💡 Key Features

## 🎯 Interest-Based Course Recommendations

- Enter up to three areas of interest
- Combines interests into a single query
- Recommends the most relevant courses

## 📚 Course Similarity Search

- Search using a course title
- Finds courses similar to the entered course
- Helps learners discover related learning paths

## 🧠 NLP-Powered Processing

Utilizes Natural Language Processing techniques:

- Text Normalization
- Tokenization
- Stopword Removal
- Lemmatization
- Stemming

## 🤖 Machine Learning Recommendation Engine

- Count Vectorization for feature extraction
- K-Nearest Neighbors (KNN) algorithm
- Cosine Similarity metric for recommendation accuracy

## 🌐 User-Friendly Interface

- Flask-based web application
- Clean and simple UI
- Detailed course information display

---

# 🏗️ Architecture

```text
User Input (Interests / Course Search)
                ↓
      Text Preprocessing (NLTK)
                ↓
     Feature Extraction (CountVectorizer)
                ↓
      KNN Recommendation Engine
                ↓
      Course Retrieval from Dataset
                ↓
        Flask Web Application
                ↓
      Recommended Courses Display
