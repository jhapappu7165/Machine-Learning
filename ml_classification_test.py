from joblib import load

# Load the saved model and vectorizer
model = load('password_strength_model.joblib') #DE-SERIALIZATION
vectorizer = load('vectorizer.joblib')

# Function to predict the strength of a new password
def predict_password_strength(password):
    # Transform the new password using the loaded vectorizer
    password_vector = vectorizer.transform([password])  # Transform single password into vector
    
    # Predict the strength using the loaded model
    predicted_strength = model.predict(password_vector)
    
    # Return the result (class label)
    return predicted_strength[0]  # 0: Weak, 1: Moderate, 2: Strong

new_password = input("Enter a password to check its strength: ")
predicted_strength = predict_password_strength(new_password)

print("The predicted strength for the password ", new_password, "is: ",predicted_strength)
