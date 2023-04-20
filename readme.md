# TARS
## Overview
TARS is a machine learning model that predicts fake news. The model can be used to classify news articles as either real or fake based on the text data in the article. This can be a valuable tool in the fight against misinformation and propaganda.

### Dataset

The dataset used to train TARS consisted of various news articles, both real and fake. The articles were labeled as either "real" or "fake" to provide a basis for the model to learn from. The dataset was carefully selected to ensure that it was representative of the types of articles that the model would encounter in the real world.

### TfidfVectorizer

Scikit-learn's TfidfVectorizer was used to process the text data in the dataset. TfidfVectorizer stands for "term frequency-inverse document frequency vectorizer." This vectorizer converts a collection of raw documents into a matrix of TF-IDF features. TF-IDF stands for "term frequency-inverse document frequency," which is a measure of how important a word is to a document in a collection or corpus. The TfidfVectorizer was chosen because it is a simple yet effective way to convert raw text data into a set of features that can be used to train a machine learning model.

### PassiveAggressive Classifier

After the text data was processed, a PassiveAggressive Classifier was used to fit the model. This classifier is a linear algorithm used for large-scale learning. It works by training the model to make correct predictions on the dataset, while also penalizing incorrect predictions. The PassiveAggressive Classifier was chosen because it is a fast and efficient algorithm that is well-suited for text classification tasks.

### Evaluation

The accuracy of TARS was evaluated using a confusion matrix. The matrix was calculated by comparing the predicted labels for a test set of news articles to their true labels. The resulting matrix showed the number of true positives, true negatives, false positives, and false negatives. The accuracy was calculated by summing the true positives and true negatives and dividing by the total number of predictions. The resulting accuracy for TARS was 92.98%.

### Conclusion

TARS is a machine learning model that predicts fake news. It was built using scikit-learn's TfidfVectorizer on a provided dataset and trained using a PassiveAggressive Classifier. With this model, it is possible to accurately predict whether a news article is real or fake. The model has been evaluated and found to be effective at its task, making it a valuable tool in the fight against misinformation and propaganda.
