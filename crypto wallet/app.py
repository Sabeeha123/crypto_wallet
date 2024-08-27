from flask import Flask, render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/flip', methods=['POST'])
def flip():
    data = request.json
    # Extract data from the request
    blockchain = data.get('blockchain')
    choice = data.get('choice')
    amount = data.get('amount')

    # Logic to connect to the blockchain and flip the coin
    result = simulate_coin_flip(choice)  # Simulate coin flip (for demo purposes)
    
    # Return result
    if result == choice:
        return jsonify({'status': 'win', 'amount': amount * 2})
    else:
        return jsonify({'status': 'lose', 'amount': 0})

def simulate_coin_flip(choice):
    # Simulate a coin flip (heads or tails)
    import random
    return 'heads' if random.choice(['heads', 'tails']) == choice else 'tails'



if __name__ == "__main__":
    app.run(debug= True)