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
