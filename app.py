# import os
# from flask import Flask, request, render_template
# from flask import jsonify

# if __name__ == '__main__':
#     app.run(debug=True)
# app = Flask(__name__, template_folder='templates')
# @app.route('/', methods=['GET'])
# @app.route('/fit-score', methods=['POST'])
# # @app.route('/', methods=['POST'])

# def receive_fit_score():
#     data = request.get_json()
#     return jsonify({"status": "success", "fit_score": data['fit_score']})
# def home():
#     if request.method == 'POST':
#         try:
#             market_size = float(request.form['market_size'])
#             competition = float(request.form['competition'])
#             risk = float(request.form['risk'])
#             if market_size < 0 or competition < 0 or risk < 0:
#                 return render_template('index.html', error='Inputs must be non-negative.')
#             score = (market_size / 1000000000 * 50) - (competition * 30) - (risk * 20)
#             score = max(0, min(100, score))
#             return render_template('result.html', score=score, country=request.form['country'])
#         except ValueError:
#             return render_template('index.html', error='Please enter valid numbers.')
#     return render_template('index.html')
# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port, debug=True)


import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            market_size = float(request.form['market_size'])
            competition = float(request.form['competition'])
            risk = float(request.form['risk'])
            if market_size < 0 or competition < 0 or risk < 0:
                return render_template('index.html', error='Inputs must be non-negative.')
            score = (market_size / 1000000000000 * 100) - (competition * 50) - (risk * 50)
            score = max(0, min(100, score))
            return render_template('result.html', score=score, country=request.form['country'])
        except ValueError:
            return render_template('index.html', error='Please enter valid numbers.')
    return render_template('index.html')

@app.route('/fit-score', methods=['POST'])
def receive_fit_score():
    try:
        data = request.get_json()
        if not data or 'fit_score' not in data:
            return jsonify({"error": "Invalid data"}), 400
        return jsonify({"status": "success", "fit_score": data['fit_score']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
