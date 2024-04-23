from flask import Flask, request, jsonify, render_template
import json
import pickle
import os

app = Flask(__name__)

# Define the path to the index.pickle file
INDEX_FILE_PATH = os.path.join(os.path.dirname(__file__), 'index.pickle')

# Function to validate JSON payload
def validate_json(data):
    try:
        parsed_data = json.loads(data)
        if 'Query' not in parsed_data or not isinstance(parsed_data['Query'], str):
            return "Query Error"
        if 'K' not in parsed_data or not isinstance(parsed_data['K'], int):
            return "K Error"
        return 'Valid'
    except json.JSONDecodeError:
        return 'Invalid JSON'

# Function to load inverted index from pickle file
def load_inverted_index_from_pickle(pickle_file):
    try:
        with open(pickle_file, 'rb') as f:
            inverted_index = pickle.load(f)
        return inverted_index
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

# Function to retrieve top documents based on query and inverted index
def retrieve_top_documents(query, inverted_index, k):
    # Your implementation to retrieve top documents based on query and inverted index
    # Replace this with your actual implementation
    return [(1, 0.85), (2, 0.75), (3, 0.72)]  # Example results

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/make-query', methods=['POST'])
def process_query():
    if request.is_json:
        validation_message = validate_json(request.get_data())
        if validation_message == 'Valid':
            data = request.get_json()
            query = data['Query'].lower()
            k = data['K']

            inverted_index = load_inverted_index_from_pickle(INDEX_FILE_PATH)

            if inverted_index:
                try:
                    results = retrieve_top_documents(query, inverted_index, k)
                    response_data = {
                        'query': query,
                        'top_results': [{'document_id': doc_id, 'relevance_score': score} for doc_id, score in results]
                    }
                    return jsonify(response_data), 200
                except Exception as e:
                    return jsonify({'error': str(e)}), 500
            else:
                return jsonify({'error': 'Inverted index not found.'}), 404
        else:
            return jsonify({'error': validation_message}), 400
    else:
        return jsonify({'error': 'Request is not in valid JSON format'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
