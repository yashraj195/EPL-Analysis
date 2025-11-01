from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main prediction form"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction logic"""
    try:
        venue_codes = float(request.form['venue_codes'])
        opp_codes = float(request.form['opp_codes'])
        hour = float(request.form['hour'])
        day_code = float(request.form['day_code'])
        gf_rolling = float(request.form['gf_rolling'])
        ga_rolling = float(request.form['ga_rolling'])
        sh_rolling = float(request.form['sh_rolling'])
        sot_rolling = float(request.form['sot_rolling'])
        dist_rolling = float(request.form['dist_rolling'])
        fk_rolling = float(request.form['fk_rolling'])
        pk_rolling = float(request.form['pk_rolling'])
        pkatt_rolling = float(request.form['pkatt_rolling'])
        
        features = np.array([[
            venue_codes, opp_codes, hour, day_code,
            gf_rolling, ga_rolling, sh_rolling, sot_rolling,
            dist_rolling, fk_rolling, pk_rolling, pkatt_rolling
        ]])
        if gf_rolling > ga_rolling and venue_codes == 1:
            prediction_result = "Win"
        elif gf_rolling < ga_rolling:
            prediction_result = "Loss"
        else:
            prediction_result = "Draw"
        
        return render_template('result.html', prediction_result=prediction_result)
    
    except Exception as e:
        return render_template('result.html', prediction_result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)