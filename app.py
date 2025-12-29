
from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__, static_folder='static')

# 1. Intent Classification (Rule-Based)
def classify_intent(query):
    query = query.lower()
    if any(keyword in query for keyword in ["exam", "marks", "syllabus", "academic", "study"]):
        return "Academic"
    elif any(keyword in query for keyword in ["movie", "song", "book", "entertainment", "watch"]):
        return "Entertainment"
    elif any(keyword in query for keyword in ["code", "debug", "error", "technical", "programming"]):
        return "Technical"
    elif any(keyword in query for keyword in ["feel", "friend", "personal", "relationship"]):
        return "Personal"
    else:
        return "General"

# 2. Neutral Answer Generation
def get_neutral_answer(intent):
    if intent == "Academic":
        return "Studying for exams requires a good understanding of the syllabus and consistent effort."
    elif intent == "Entertainment":
        return "There are many great movies and songs to explore. What genres are you interested in?"
    elif intent == "Technical":
        return "Debugging code can be a challenging but rewarding process. Have you tried using a debugger?"
    elif intent == "Personal":
        return "Building strong personal relationships is an important aspect of a fulfilling life."
    else:
        return "That's an interesting topic. Could you please provide more details?"

# 3. Style Adaptation
def get_styled_response(intent, style):
    neutral_answer = get_neutral_answer(intent)

    if style == "overconfident_genius":
        return f"Obviously, the intent is {intent}. Here's the answer, not that you'd understand its brilliance: {neutral_answer}"
    elif style == "nervous_intern":
        return f"Um, I think this might be about {intent}? I'm not sure, but here is what I found... I hope it's right: {neutral_answer}"
    elif style == "sarcastic_reviewer":
        return f"Oh, look, another query about '{intent}'. Groundbreaking. Here's your answer, I guess: {neutral_answer}"
    elif style == "calm_professor":
        return f"That's an excellent question. It falls under the category of {intent}. Let's explore this further. The answer is: {neutral_answer}"
    else:
        return neutral_answer

# 4. API Endpoint
@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    style = data.get('style', 'calm_professor') # Default to calm_professor

    if not query:
        return jsonify({"error": "Query not provided"}), 400

    intent = classify_intent(query)
    response = get_styled_response(intent, style)

    return jsonify({
        "intent": intent,
        "response": response
    })

# 5. UI Rendering
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
