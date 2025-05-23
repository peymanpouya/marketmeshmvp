from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            market_size = float(request.form['market_size'])
            competition = float(request.form['competition'])
            risk = float(request.form['risk'])
            if market_size < 0 or competition < 0 or risk < 0:
                return render_template('index.html', error='Inputs must be non-negative.')
            score = (market_size / 1000000 * 50) - (competition * 30) - (risk * 20)
            score = max(0, min(100, score))
            return render_template('result.html', score=score, country=request.form['country'])
        except ValueError:
            return render_template('index.html', error='Please enter valid numbers.')
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
