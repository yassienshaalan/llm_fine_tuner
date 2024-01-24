from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load your model
model_path = "path/to/your/model"
model = pipeline("text-generation", model=model_path)

@app.route('/generate-sql', methods=['POST'])
def generate_sql():
    content = request.json
    input_text = content['input']
    generated_sql = model(input_text)[0]['generated_text']
    return jsonify({'sql_query': generated_sql})

if __name__ == '__main__':
    app.run(debug=True)
