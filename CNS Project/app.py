from flask import Flask, render_template, request, jsonify
from spam_detector import is_spam  # Assume you have a function is_spam for detecting spam

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_spam', methods=['POST'])
def check_spam():
    email_text = request.form['email_text']
    result = is_spam(email_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB

# app = Flask(__name__)

# # Sample spam and ham (non-spam) data for demonstration

# training_data = [
#     ('Buy our products and get a discount', 'spam'),
#     ('Hello, how are you?', 'ham'),
#     ('URGENT: You\'ve Won $1,000,000! To claim your prize, reply to this email with your details.', 'spam'),
#     # Add more examples...
# ]

# # Train a simple Naive Bayes classifier
# vectorizer = CountVectorizer()
# X_train = vectorizer.fit_transform([email for email, label in training_data])
# y_train = [label for email, label in training_data]
# classifier = MultinomialNB()
# classifier.fit(X_train, y_train)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/check_spam', methods=['POST'])
# def check_spam():
#     email_text = request.form['email_text']
#     X_test = vectorizer.transform([email_text])
#     prediction = classifier.predict(X_test)[0]
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)

