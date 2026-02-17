from flask import Flask, render_template, request, jsonify
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
import os
from pathlib import Path

app = Flask(__name__)

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Get the absolute paths to both text files
current_dir = Path(__file__).parent
file_path1 = current_dir / "salarjung.txt"
file_path2 = current_dir / "salarjung2.txt"

try:
    # Load both museum data files
    print(f"Attempting to load files from: {file_path1} and {file_path2}")
    
    # Load first file
    loader1 = TextLoader(str(file_path1), encoding='utf-8')
    documents1 = loader1.load()
    print("Successfully loaded salarjung.txt")
    
    # Load second file
    loader2 = TextLoader(str(file_path2), encoding='utf-8')
    documents2 = loader2.load()
    print("Successfully loaded salarjung2.txt")
    
    # Combine documents
    all_documents = documents1 + documents2
    
    # Split combined documents
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(all_documents)
    print(f"Successfully processed {len(texts)} total text chunks")

except Exception as e:
    print(f"Error loading files: {e}")
    raise

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_documents(texts, embeddings)
chain = load_qa_chain(OpenAI(), chain_type="stuff")

# Conversation patterns and responses
GREETING_PATTERNS = {
    'hi': True,
    'hello': True,
    'hey': True,
    'greetings': True,
    'good morning': True,
    'good afternoon': True,
    'good evening': True,
}

def get_greeting_response():
    return {
        'response': """Hello! Welcome to the Salarjung Museum AI Guide. I'm here to help you explore our magnificent collection and answer any questions about:
- Museum locations and directions
- Transportation and how to reach us
- Museum facilities and amenities
- Our galleries and exhibitions
- Museum publications and resources
- Scholar facilities and library
- And much more!

What would you like to know about the museum?"""
    }

def is_greeting(text):
    return text.lower().strip() in GREETING_PATTERNS

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('bot.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json['question']
    
    # Check if it's a greeting
    if is_greeting(user_question):
        return jsonify(get_greeting_response())
    
    # For non-greeting questions, use the museum knowledge base
    docs = docsearch.similarity_search(user_question)
    response = chain.run(input_documents=docs, question=user_question)
    
    # If response is too short or empty, provide a helpful message
    if len(response.strip()) < 10:
        response = """I apologize, but I'm not sure about that. However, I can help you with information about:
- Museum locations and directions
- Transportation options
- Museum facilities and galleries
- Publications and resources
- Scholar facilities
Please feel free to ask about any of these topics!"""
    
    return jsonify({'response': response})

@app.route('/voice')
def voice_interface():
    return render_template('voiceassistant.html')

if __name__ == '__main__':
    app.run(debug=True) 