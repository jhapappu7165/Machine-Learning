#QTA: What does the vectorizer look like? How to ensure once built model doesn't have to be re-built?


#FEATURES: input (independent variable), LABELS: Output (dependent)

#sklearn (or scikit-learn): A popular Python library for ML that provides tools to help build ML models, evaluate their performance, and use them for prediction.
#datasets module (from sklearn): Includes several small datasets and tools to create synthetic datasets for practicing ML or load real-world datasets (iris, digits).
#train_test_split function (from sklearn.model_selection): split your data into two parts: training data and testing data.

#RandomForestClassifier (from sklearn.ensemble): used for classification tasks. builds many decision trees and combines their predictions to get more accurate results. Called an “ENSEMBLE” model becz it uses multiple models (trees) working together.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier #used for classification tasks
from sklearn.feature_extraction.text import CountVectorizer #convert text data (e.g.passwords) into a vector of word counts. Each pw into numerical representation
from sklearn.metrics import classification_report, confusion_matrix
from joblib import dump #serializing (saving) & deserializing (loading) Python objects-store trained ML models to disk, so NOT rebuild each time to use them


df = pd.read_csv('new_file_combined.csv')

x = df[['password']]
y = df['strength'].values.ravel() #.values.ravel() converts the target values into a 1D array which is required by scikit_learn

# Preprocess the password data
vectorizer = CountVectorizer() #max_features=100    # x['password'] selects the password column from the DataFrame x
x = vectorizer.fit_transform(x['password']) #transforms 'password' into a matrix of token counts. Each unique word from the dataset becomes a column in this matrix.

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=345, stratify=y) #random_state to ensure same set of 80% of data used for training


# Print the number of rows and columns
print('Data used to TRAIN the model has', x_train.shape[0], 'rows and', x_train.shape[1], 'columns.')
print('UNSEEN Data used to TEST the model has', x_test.shape[0], 'rows and', x_test.shape[1], 'columns.')
print('Total Data for training & testing has', df.shape[0], 'rows and', df.shape[1], 'columns.', '\n')

## max_features=100: The training set has 536,082 rows and 100 columns, which means there're 536,082 password samples, & each password is represented by a vector of 100 features (tokens).


# Create and train the Random Forest Classifier
model = RandomForestClassifier(random_state=345, ) #instance of the RandomForestClassifier 
model.fit(x_train, y_train) #trains RandomForestClassifier on the training data (x_train, y_train), allowing model to learn the patterns between passwords and strengths


# Make predictions
y_pred = model.predict(x_test) #predict the strength labels for the test data (x_test) - predicted labels are stored in y_pred


# Evaluate the model
print("Confusion Matrix:") #shows how many instances were correctly and incorrectly classified for each class. 3 classes labeled 0,1,&2
print(confusion_matrix(y_test, y_pred))

print("Classification Report:") #provides key metrics for each class: precision, recall, F1-score, and support
print(classification_report(y_test, y_pred))


#SERIALIZATION of the TRAINED MODEL TO AVOID REBUILDING OF THE MODEL EVERY TIME
dump(model, 'password_strength_model.joblib') 
dump(vectorizer, 'vectorizer.joblib')
