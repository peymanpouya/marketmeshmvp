import os
from flask import Flask, request, render_template
import logging
# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)
logger.debug('Flask app initialized')
@app.route('/', methods=['GET', 'POST'])
def home():
    logger.debug('Accessing home route')
    try:
        if request.method == 'POST':
            logger.debug('Processing POST request')
            market_size = float(request.form['market_size'])
            competition = float(request.form['competition'])
            risk = float(request.form['risk'])
            logger.debug(f'Inputs: market_size={market_size}, competition={competition}, risk={risk}')
            if market_size < 0 or competition < 0 or risk < 0:
                logger.warning('Negative inputs detected')
                return render_template('index.html', error='Inputs must be non-negative.')
            score = (market_size / 1000000 * 50) - (competition * 30) - (risk * 20)
            score = max(0, min(100, score))
            logger.debug(f'Calculated score: {score}')
            return render_template('result.html', score=score, country=request.form['country'])
        logger.debug('Rendering index.html for GET request')
        return render_template('index.html')
    except Exception as e:
        logger.error(f'Error in home route: {str(e)}')
        return render_template('index.html', error=f'Server error: {str(e)}')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
