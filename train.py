import pandas as pd
import re
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample dataset (You can replace with real phishing dataset)
data = {
    "url": [
        "https://google.com",
        "https://facebook.com",
        "http://free-money.ru",
        "http://secure-login-paypal.com",
        "https://github.com",
        "http://bank-verification-alert.net"
    ],
    "label": [0, 0, 1, 1, 0, 1]  # 0 = Legit, 1 = Phishing
}

df = pd.DataFrame(data)

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if "https" in url else 0,
        1 if re.search(r'\d', url) else 0
    ]

X = df['url'].apply(extract_features).tolist()
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

pickle.dump(model, open("model.pkl", "wb"))
