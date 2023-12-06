# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import make_pipeline

# def train_model():
#     # Training data (example)
#     emails = ["This is a legitimate email.", "Buy now and get 50% off!", "Meeting at 2 PM"]
    
#     labels = [0, 1, 0]  # 0 for legitimate, 1 for spam

#     # Create a pipeline with CountVectorizer and Multinomial Naive Bayes
#     model = make_pipeline(CountVectorizer(), MultinomialNB())

#     # Train the model
#     model.fit(emails, labels)

#     return model

# def is_spam(email_text):
#     model = train_model()
#     prediction = model.predict([email_text])
#     return bool(prediction[0])
# spam_detector.py

def is_spam(email_text):
    # Basic spam detection using keywords
    spam_keywords = ["buy now", "limited time offer", "earn money fast", "free gift", "click here","URGENT: You've Won"]

    for keyword in spam_keywords:
        if keyword.lower() in email_text.lower():
            return True

    return False


# spam_detector.py
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import make_pipeline

# def train_model():
#     # Training data (example)
#     emails = ["This is a legitimate email.", "Buy now and get 50% off!", "Meeting at 2 PM"]

#     labels = [0, 1, 0]  # 0 for legitimate, 1 for spam

#     # Create a pipeline with CountVectorizer and Multinomial Naive Bayes
#     model = make_pipeline(CountVectorizer(), MultinomialNB())

#     # Train the model
#     model.fit(emails, labels)

#     return model

# def is_spam(email_text):
#     model = train_model()
#     prediction = model.predict([email_text])
#     return bool(prediction[0])
