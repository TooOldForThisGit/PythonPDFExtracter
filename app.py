from flask import Flask, request, jsonify
from services.pdf_service import extract_text_from_pdf
from services.chatgpt_service import get_chatgpt_response

app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']


    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400


    if file and file.filename.endswith('.pdf'):
        try:

            text = str(extract_text_from_pdf(file))
            
            response_type = request.args.get('response_type', 'ai-processed-json-obj')
            
            if response_type == 'raw-text':
                return jsonify({'raw_text': text})
            elif response_type == 'ai-processed-json-obj':
                # TODO: provide with an uniform model class to map to
                prompt = str("Please take the text input provided and convert it into a valid JSON format. Ensure to remove any escape characters and format it properly for readability. The text should be structured to reflect hierarchical data if necessary. The text: " + text)
                chatgpt_response = get_chatgpt_response(prompt)
                return jsonify({'ai_processed_response': chatgpt_response})
            else:
                return jsonify({'error': 'Invalid response_type specified'}), 400

        except Exception as e:
            # TODO: log
            return jsonify({'error': str(e)}), 500
        
    else:
        return jsonify({'error': 'File is not in a valid PDF format'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
