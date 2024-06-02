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

