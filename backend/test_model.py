import joblib

model = joblib.load("career_model.pkl")
encoder = joblib.load("encoder.pkl")

sample = [[9, 8, 9, 2, 7]]

prediction = model.predict(sample)

print(
    encoder.inverse_transform(prediction)[0]
)