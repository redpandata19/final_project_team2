from flask import Flask, render_template, jsonify, send_file
import pandas as pd
import json

app = Flask(__name__)

# Read the dataset
df = pd.read_csv('database.csv')

# Mapping between country names in the CSV and GeoJSON filenames
country_name_mapping = {
    'United States of America': 'united_states_of_america',
    'United Kingdom': 'united_kingdom',
    'Trinidad and Tobago': 'trinidad_and_tobago',
    'Taiwan': 'taiwan',
    'Puerto Rico': 'puerto_rico',
    'Philippines': 'philippines',
    'Laos': 'laos',
    'Iran': 'iran',
    'India': 'india',
    'Honduras': 'honduras',
    'Haiti': 'haiti',
    'Guatemala': 'guatemala',
    'Greece': 'greece',
    'France': 'france',
    'Germany': 'germany',
    # Add more mappings as needed
}

# Route to render the map page
@app.route('/')
def map_page():
    return render_template('3.html')

# Route to fetch data for the map
@app.route('/data')
def get_data():
    country_counts = df['Native-Country'].value_counts()

    data = {
        'countries': country_counts.index.tolist(),  # List of country names
        'counts': country_counts.values.tolist()     # List of counts of people from each country
    }
    return jsonify(data)

# Route to fetch GeoJSON for a specific country
@app.route('/country_geojson/<country>')
def get_country_geojson(country):
    try:
        # Load GeoJSON file for the specified country
        filename = country_name_mapping.get(country, '').lower() + '.geojson'
        if filename:
            with open(f'geojson_files/{filename}', 'r') as file:
                geojson_data = json.load(file)
            return jsonify(geojson_data)
        else:
            return jsonify({'error': 'No GeoJSON file found for this country'}), 404
    except FileNotFoundError:
        return jsonify({'error': 'GeoJSON file not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)