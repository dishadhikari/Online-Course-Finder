from flask import Flask, request, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

def preprocess(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(lemmatizer.lemmatize(w)) for w in tokens]
    return ' '.join(tokens)

df = pd.read_csv('Online_Courses.csv')
df['processed'] = df['Title'].apply(preprocess)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['processed'])
knn = NearestNeighbors(n_neighbors=10, metric='cosine')
knn.fit(X)

train_data = pd.DataFrame({
    'feature1': [0.1, 0.2, 0.4, 0.8, 0.5, 0.3],
    'feature2': [1, 2, 3, 4, 5, 6],
    'relevance': [3, 2, 1, 0, 2, 1],
    'query_id': [1, 1, 1, 2, 2, 2]  
})

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    interest_recommendations = []
    course_recommendations = []

    if request.method == 'POST':
        button_type = request.form.get('submit_button')

        if button_type == 'interests':
            search1 = request.form.get('search1', '')
            search2 = request.form.get('search2', '')
            search3 = request.form.get('search3', '')

            user_input = f"{search1} {search2} {search3}"
            processed_input = preprocess(user_input)
            user_vector = vectorizer.transform([processed_input])
            distances, indices = knn.kneighbors(user_vector)
            interest_recommendations = df.iloc[indices.flatten()].to_dict(orient='records')

        elif button_type == 'course':
            course_search = request.form.get('course_search', '')
            processed_input = preprocess(course_search)
            user_vector = vectorizer.transform([processed_input])
            distances, indices = knn.kneighbors(user_vector)
            course_recommendations = df.iloc[indices.flatten()].to_dict(orient='records')

    return render_template('html.html',
                           interest_recommendations=interest_recommendations,
                           course_recommendations=course_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
