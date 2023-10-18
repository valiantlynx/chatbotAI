'''
this might be part of the final report. im thinking of making the same ai without using the ai library. for now it is not working. i will try to make it work later.
'''


import wikipedia
import re
import numpy as np

# Scrape the Wikipedia page for the given topic and return the summary and content


def learn_from_wikipedia(topic):
    page = wikipedia.page(topic)
    summary = page.summary
    content = page.content
    return summary, content

# Preprocess the summary and content by lowercasing and removing punctuation


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Define the activation function and its derivative


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)

# Train the ANN on the summary and content


def train(summary, content):
    # Tokenize the summary and content
    summary_tokens = summary.split()
    content_tokens = content.split()

    # Create a vocabulary of all the unique words in the summary and content
    vocabulary = set(summary_tokens + content_tokens)

    # Create a mapping from words to integer indices and a reverse mapping from integer indices to words
    word_to_index = {word: i for i, word in enumerate(vocabulary)}
    index_to_word = {i: word for i, word in enumerate(vocabulary)}

    # Convert the summary and content to sequences of integer indices
    summary_sequence = [word_to_index[word] for word in summary_tokens]
    content_sequence = [word_to_index[word] for word in content_tokens]

    # Create an ANN with a single hidden layer and random weights
    input_size = len(vocabulary)
    hidden_size = 100
    output_size = len(vocabulary)
    global W1, W2, b1, b2
    W1 = np.random.randn(input_size, hidden_size)
    W2 = np.random.randn(hidden_size, output_size)
    b1 = np.zeros((1, hidden_size))
    b2 = np.zeros((1, output_size))

    # Define the activation function and its derivative
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(x):
        return x * (1 - x)

       # Train the ANN on the summary and content
    for i in range(50000):
        # Forward pass
        z1 = np.dot(summary_sequence, W1) + b1
        a1 = sigmoid(z1)
        z2 = np.dot(a1, W2) + b2
        a2 = sigmoid(z2)

        # Backward pass
        error = content_sequence - a2
        dz2 = error * sigmoid_derivative(a2)
        da1 = np.dot(dz2, W2.T)
        dz1 = da1 * sigmoid_derivative(a1)

        # Update the weights and biases
        W2 += np.dot(a1.T, dz2)
        b2 += np.sum(dz2, axis=0, keepdims=True)
        W1 += np.dot(summary_sequence.T, dz1)
        b1 += np.sum(dz1, axis=0, keepdims=True)

    # Define the predict function to generate answers
    
    
    def predict(question, num_words=20):
        # Preprocess the question
        question = preprocess(question)
    
        # Tokenize the question
        question_tokens = question.split()
    
        # Convert the question to a sequence of integer indices
        question_sequence = [word_to_index[word] for word in question_tokens]
    
        # Feed the question sequence through the ANN
        z1 = np.dot(question_sequence, W1) + b1
        a1 = sigmoid(z1)
        z2 = np.dot(a1, W2) + b2
        a2 = sigmoid(z2)
    
        # Convert the output of the ANN back to a sequence of words
        words = []
        for i in np.argmax(a2, axis=1):
            words.append(index_to_word[i])
            if len(words) >= num_words:
                break
    
        # Return the predicted answer as a string
        return ' '.join(words)
    
    # Test the ANN by learning from Wikipedia and asking it questions
    def main():
        # Choose a topic to learn about
        topic = 'Artificial intelligence'
    
        # Scrape the Wikipedia page for the topic
        summary, content = learn_from_wikipedia(topic)
    
        # Preprocess the summary and content
        summary = preprocess(summary)
        content = preprocess(content)
    
        # Train the ANN on the summary and content
        train(summary, content)
    
        # Ask the ANN questions
        while True:
            question = input('Ask a question (or type "exit" to quit): ')
            if question == 'exit':
                break
            answer = predict(question)
            print(f'Answer: {answer}')
    
    
    # Run the main function
    if __name__ == '__main__':
        main()
