from dash import Dash, dcc, html  # Updated imports
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import joblib

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

import pandas as pd

def load_data():
    data_path = "data/database.csv"
    df = pd.read_csv(data_path)
    print(df.head())  # Add this line to verify data loading
    return df

# Load the data
data = load_data()


# Preprocess input data
def preprocess_input(input_data):
    # Implement your preprocessing steps here
    processed_data = pd.DataFrame([input_data], columns=[
        "Age", "Workclass", "Education", "Educational_Grade",
        "Marital_Status", "Occupation", "Relationship", "Race", "Gender", "Annual-Income", 
        "Hours_Worked_Per_Week"
    ])
    return processed_data

# Load the model
def load_model():
    model_path = "models/model.pkl"
    model = joblib.load(model_path)
    return model


# Load the data and model
data = load_data()
model = load_model()


# Define the layout
app.layout = html.Div([
    html.H1("Income Prediction Dashboard"),
    
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[
            html.Div([
                html.H2("Data Story"),
                html.Img(src="/assets/initial_analysis.png", style={"width": "50%"}),
                html.P("This dashboard provides an analysis and prediction of income levels based on various demographic factors."),
                
                html.H3("Background Research"),
                html.P("""
                    In 1994, the median household income in the United States was approximately $32,368. This dataset, derived from the 1994 Census database, 
                    includes various attributes such as age, workclass, education, and occupation, among others, to predict whether an individual's income exceeds $50,000.
                """),
                html.P("""
                    Fast forward to 2024, the median household income in the United States has risen to approximately $77,397. The analysis presented here uses 
                    machine learning models to predict income levels based on demographic and socioeconomic features. By understanding the trends and patterns 
                    in the data, we can gain insights into the factors that influence income levels and how they have changed over time.
                """),
                
                html.H3("Dataset Overview"),
                html.P("""
                    The dataset contains 15 attributes including age, workclass, education, marital status, occupation, relationship, race, gender, 
                    and hours worked per week. The target variable is the income level, categorized as '>50K' or '<=50K'.
                """),
                
                html.H3("Key Findings"),
                html.P("""
                    - Certain factors such as higher education levels and specific occupations are strongly correlated with higher income levels.
                    - Gender and race also show significant disparities in income distribution.
                    - The machine learning model used in this analysis provides a predictive accuracy of approximately 83%.
                """),
            ])
        ]),
        
        dcc.Tab(label='Predictor', children=[
            html.Div([
                html.H2("Income Prediction"),
                html.Label('Age:'),
                dcc.Input(id='input-age', type='number', value=25),

                html.Label('Workclass:'),
                dcc.Dropdown(id='input-workclass', options=[
                    {'label': 'Private', 'value': 'Private'},
                    {'label': 'Self-emp-not-inc', 'value': 'Self-emp-not-inc'},
                    {'label': 'Self-emp-inc', 'value': 'Self-emp-inc'},
                    {'label': 'Federal-gov', 'value': 'Federal-gov'},
                    {'label': 'Local-gov', 'value': 'Local-gov'},
                    {'label': 'State-gov', 'value': 'State-gov'},
                    {'label': 'Without-pay', 'value': 'Without-pay'},
                    {'label': 'Never-worked', 'value': 'Never-worked'}
                ], value='Private'),

                html.Label('Education:'),
                dcc.Dropdown(id='input-education', options=[
                    {'label': 'Bachelors', 'value': 'Bachelors'},
                    {'label': 'Some-college', 'value': 'Some-college'},
                    {'label': '11th', 'value': '11th'},
                    {'label': 'HS-grad', 'value': 'HS-grad'},
                    {'label': 'Prof-school', 'value': 'Prof-school'},
                    {'label': 'Assoc-acdm', 'value': 'Assoc-acdm'},
                    {'label': 'Assoc-voc', 'value': 'Assoc-voc'},
                    {'label': '9th', 'value': '9th'},
                    {'label': '7th-8th', 'value': '7th-8th'},
                    {'label': '12th', 'value': '12th'},
                    {'label': 'Masters', 'value': 'Masters'},
                    {'label': '1st-4th', 'value': '1st-4th'},
                    {'label': '10th', 'value': '10th'},
                    {'label': 'Doctorate', 'value': 'Doctorate'},
                    {'label': '5th-6th', 'value': '5th-6th'},
                    {'label': 'Preschool', 'value': 'Preschool'}
                ], value='Bachelors'),

                html.Label('Marital Status:'),
                dcc.Dropdown(id='input-marital-status', options=[
                    {'label': 'Married-civ-spouse', 'value': 'Married-civ-spouse'},
                    {'label': 'Divorced', 'value': 'Divorced'},
                    {'label': 'Never-married', 'value': 'Never-married'},
                    {'label': 'Separated', 'value': 'Separated'},
                    {'label': 'Widowed', 'value': 'Widowed'},
                    {'label': 'Married-spouse-absent', 'value': 'Married-spouse-absent'},
                    {'label': 'Married-AF-spouse', 'value': 'Married-AF-spouse'}
                ], value='Never-married'),

                html.Label('Occupation:'),
                dcc.Dropdown(id='input-occupation', options=[
                    {'label': 'Tech-support', 'value': 'Tech-support'},
                    {'label': 'Craft-repair', 'value': 'Craft-repair'},
                    {'label': 'Other-service', 'value': 'Other-service'},
                    {'label': 'Sales', 'value': 'Sales'},
                    {'label': 'Exec-managerial', 'value': 'Exec-managerial'},
                    {'label': 'Prof-specialty', 'value': 'Prof-specialty'},
                    {'label': 'Handlers-cleaners', 'value': 'Handlers-cleaners'},
                    {'label': 'Machine-op-inspct', 'value': 'Machine-op-inspct'},
                    {'label': 'Adm-clerical', 'value': 'Adm-clerical'},
                    {'label': 'Farming-fishing', 'value': 'Farming-fishing'},
                    {'label': 'Transport-moving', 'value': 'Transport-moving'},
                    {'label': 'Priv-house-serv', 'value': 'Priv-house-serv'},
                    {'label': 'Protective-serv', 'value': 'Protective-serv'},
                    {'label': 'Armed-Forces', 'value': 'Armed-Forces'}
                ], value='Tech-support'),

                html.Label('Relationship:'),
                dcc.Dropdown(id='input-relationship', options=[
                    {'label': 'Wife', 'value': 'Wife'},
                    {'label': 'Own-child', 'value': 'Own-child'},
                    {'label': 'Husband', 'value': 'Husband'},
                    {'label': 'Not-in-family', 'value': 'Not-in-family'},
                    {'label': 'Other-relative', 'value': 'Other-relative'},
                    {'label': 'Unmarried', 'value': 'Unmarried'}
                ], value='Not-in-family'),

                html.Label('Race:'),
                dcc.Dropdown(id='input-race', options=[
                    {'label': 'White', 'value': 'White'},
                    {'label': 'Asian-Pac-Islander', 'value': 'Asian-Pac-Islander'},
                    {'label': 'Amer-Indian-Eskimo', 'value': 'Amer-Indian-Eskimo'},
                    {'label': 'Other', 'value': 'Other'},
                    {'label': 'Black', 'value': 'Black'}
                ], value='White'),

                html.Label('Gender:'),
                dcc.Dropdown(id='input-gender', options=[
                    {'label': 'Male', 'value': 'Male'},
                    {'label': 'Female', 'value': 'Female'}
                ], value='Male'),

                html.Label('Hours Worked Per Week:'),
                dcc.Input(id='input-hours-per-week', type='number', value=40),

                html.Button('Submit', id='submit-button', n_clicks=0),
                html.Div(id='prediction-output')
            ])
        ]),
        
        dcc.Tab(label='Visualizations', children=[
            html.Div([
                html.H2("Visualizations"),
                
                html.Div([
                    html.H3("Bar Chart: Income by Education Level"),
                    dcc.Dropdown(id='education-dropdown', options=[
                        {'label': 'Bachelors', 'value': 'Bachelors'},
                        {'label': 'Some-college', 'value': 'Some-college'},
                        {'label': 'HS-grad', 'value': 'HS-grad'},
                        # Add more options here
                    ], value='Bachelors'),
                    dcc.Graph(id='bar-chart-education')
                ]),
                
                html.Div([
                    html.H3("Histogram: Age Distribution"),
                    dcc.Graph(id='histogram-age')
                ]),
                
                html.Div([
                    html.H3("Map: Median Household Income"),
                    dcc.Graph(id='map')
                ]),
                
                html.Div([
                    html.H3("Pie Chart: Income Distribution by Gender"),
                    dcc.Graph(id='pie-chart-gender')
                ]),
                
                html.Div([
                    html.H3("Box Plot: Income by Occupation"),
                    dcc.Graph(id='box-plot-occupation')
                ]),
                
                html.Div([
                    html.H3("Violin Plot: Income Distribution by Education Level"),
                    dcc.Graph(id='violin-plot-education')
                ]),
                
                html.Div([
                    html.H3("Scatter Plot: Age vs. Hours Worked Per Week"),
                    dcc.Graph(id='scatter-plot-age-hours')
                ]),
                
                html.Div([
                    html.H3("Bar Chart: Income by Marital Status"),
                    dcc.Graph(id='bar-chart-marital-status')
                ]),
                
                html.Div([
                    html.H3("Heatmap: Correlation Matrix"),
                    dcc.Graph(id='heatmap-correlation')
                ])
            ])
        ])
    ])
])


# Define callbacks

@app.callback(
    Output('prediction-output', 'children'),
    Input('submit-button', 'n_clicks'),
    State('input-age', 'value'),
    State('input-workclass', 'value'),
    State('input-education', 'value'),
    State('input-marital-status', 'value'),
    State('input-occupation', 'value'),
    State('input-relationship', 'value'),
    State('input-race', 'value'),
    State('input-gender', 'value'),
    State('input-hours-per-week', 'value')
)
def predict_income(n_clicks, age, workclass, education, marital_status, occupation, relationship, race, gender, hours_per_week):
    if n_clicks > 0:
        input_data = {
            "Age": age,
            "Workclass": workclass,
            "Education": education,
            "Marital_Status": marital_status,
            "Occupation": occupation,
            "Relationship": relationship,
            "Race": race,
            "Gender": gender,
            "Hours_Worked_Per_Week": hours_per_week
        }
        processed_data = preprocess_input(input_data)
        if processed_data is not None:
            prediction = model.predict(processed_data)
            return f'Predicted Income: {"<=50K" if prediction == 0 else ">50K"}'
    return "Please provide all input values."

@app.callback(
    Output('income-distribution-chart', 'figure'),
    Input('prediction-output', 'children')
)
def update_visualization(prediction):
    if not prediction:
        return go.Figure()

    # Example: filtering or processing data based on prediction
    # Here we pretend 'prediction' can directly influence the visualization
    filtered_data = data[data['Predicted_Income'] == prediction.split(': ')[1]]
    fig = px.bar(filtered_data, x='Education', y='Number', color='Gender',
                 title='Distribution of Predicted Incomes Across Education Levels')
    return fig

@app.callback(
    Output('bar-chart-education', 'figure'),
    Input('education-dropdown', 'value')
)
def update_bar_chart_education(education_level):
    if not education_level:
        return go.Figure()  # Return an empty figure if no selection

    filtered_data = data[data['Education'] == education_level]
    if filtered_data.empty:
        return go.Figure()  # Return an empty figure if no data matches the filter

    fig = px.bar(filtered_data, x='Workclass', y='Annual_Income',
                 color='Workclass', labels={'Annual_Income': 'Annual Income'},
                 title=f'Income by Workclass for {education_level} Education Level')
    fig.update_layout(barmode='group', xaxis_title='Workclass', yaxis_title='Annual Income')
    return fig

@app.callback(
    Output('histogram-age', 'figure'),
    Input('education-dropdown', 'value')
)
def update_histogram_age(education_level):
    if not education_level:
        return go.Figure()  # Return an empty figure if no education level is selected

    filtered_data = data[data['Education'] == education_level]
    if filtered_data.empty:
        return go.Figure()  # Return an empty figure if no data matches the filter

    fig = px.histogram(filtered_data, x='Age', nbins=20, color='Gender',
                       title=f'Age Distribution for {education_level}',
                       labels={'Age': 'Age'})
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    return fig


@app.callback(
    Output('map', 'figure'),
    Input('some-map-dropdown', 'value')  # Replace or remove if not needed
)
def update_map(selection):
    # Assuming 'selection' influences what is displayed on the map
    fig = px.choropleth(data, geojson='path_to_geojson_file', locations='State',
                        color='Median_Income', hover_name='State',
                        locationmode='USA-states', color_continuous_scale="Viridis")
    fig.update_geos(fitbounds="locations", visible=False)
    return fig


@app.callback(
    Output('pie-chart-gender', 'figure'),
    Input('pie-chart-gender', 'id')  # Dummy input to trigger callback
)
def update_pie_chart_gender(_):
    fig = px.pie(data, names='Gender', values='Annual_Income',
                 title='Income Distribution by Gender')
    fig.update_traces(textinfo='percent+label')
    return fig

@app.callback(
    Output('box-plot-occupation', 'figure'),
    Input('box-plot-occupation', 'id')  # Dummy input to trigger callback
)
def update_box_plot_occupation(_):
    fig = px.box(data, x='Occupation', y='Annual_Income', color='Occupation',
                 title='Income by Occupation',
                 labels={'Annual_Income': 'Annual Income'})
    fig.update_layout(xaxis_title='Occupation', yaxis_title='Annual Income')
    return fig

@app.callback(
    Output('violin-plot-education', 'figure'),
    Input('violin-plot-education', 'id')  # Dummy input to trigger callback
)
def update_violin_plot_education(_):
    fig = px.violin(data, x='Education', y='Annual_Income', color='Education',
                    box=True, points="all",
                    title='Income Distribution by Education Level',
                    labels={'Annual_Income': 'Annual Income'})
    fig.update_layout(xaxis_title='Education Level', yaxis_title='Annual Income')
    return fig

@app.callback(
    Output('scatter-plot-age-hours', 'figure'),
    Input('scatter-plot-age-hours', 'id')  # Dummy input to trigger callback
)
def update_scatter_plot_age_hours(_):
    fig = px.scatter(data, x='Age', y='Hours_Worked_Per_Week', color='Annual_Income',
                     title='Age vs. Hours Worked Per Week',
                     labels={'Hours_Worked_Per_Week': 'Hours Worked Per Week'})
    fig.update_layout(xaxis_title='Age', yaxis_title='Hours Worked Per Week')
    return fig

@app.callback(
    Output('bar-chart-marital-status', 'figure'),
    Input('bar-chart-marital-status', 'id')  # Dummy input to trigger callback
)
def update_bar_chart_marital_status(_):
    fig = px.bar(data, x='Marital_Status', y='Annual_Income', color='Marital_Status',
                 barmode='group',
                 title='Income by Marital Status',
                 labels={'Annual_Income': 'Annual Income'})
    fig.update_layout(xaxis_title='Marital Status', yaxis_title='Annual Income')
    return fig

@app.callback(
    Output('heatmap-correlation', 'figure'),
    Input('heatmap-correlation', 'id')  # Dummy input to trigger callback
)
def update_heatmap_correlation(_):
    correlation = data.corr()
    fig = go.Figure(data=go.Heatmap(
        z=correlation.values,
        x=correlation.index.values,
        y=correlation.columns.values,
        colorscale='Viridis',
        colorbar=dict(title='Correlation Coefficient')))
    fig.update_layout(title='Correlation Matrix',
                      xaxis_nticks=36)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)