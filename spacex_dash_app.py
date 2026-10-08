# spacex_dash_app.py
# SpaceX Falcon 9 First Stage Landing Prediction Dashboard
# Author: Dhruv Khokhriya
# Course: IBM Applied Data Science Capstone

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Ingest analytical dataset
spacex_df = pd.read_csv("spacex_data.csv")
max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

# Initialize Dash application
app = dash.Dash(__name__)

# Application UI Layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#0B49CB', 'font-size': 32}),
    
    # Task 1: Launch Site Dropdown Selector
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                 ],
                 value='ALL',
                 placeholder="Select a Launch Site here",
                 searchable=True),
    html.Br(),

    # Task 2: Launch Success Pie Chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload Range (Kg):", style={'fontWeight': 'bold'}),
    # Task 3: Payload Mass RangeSlider
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                    value=[min_payload, max_payload]),

    # Task 4: Payload vs. Outcome Scatter Plot
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# Callback 1: Success Pie Chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='Class', 
                     names='LaunchSite', 
                     title='Total Successful Launches By Site',
                     color_discrete_sequence=px.colors.sequential.Blues_r)
        return fig
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        outcome_df = filtered_df['Class'].value_counts().reset_index()
        outcome_df.columns = ['Class', 'count']
        outcome_df['Outcome_Label'] = outcome_df['Class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(outcome_df, values='count', 
                     names='Outcome_Label', 
                     title=f'Landing Outcome Distribution for site {entered_site}',
                     color='Outcome_Label',
                     color_discrete_map={'Success': '#16A34A', 'Failure': '#DC2626'})
        return fig

# Callback 2: Payload vs Success Scatter Plot
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[(spacex_df['PayloadMass'] >= low) & (spacex_df['PayloadMass'] <= high)]
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='PayloadMass', y='Class',
                         color='BoosterVersion',
                         title='Correlation between Payload and Landing Outcome for all Sites',
                         labels={'Class': 'Landing Outcome (1=Success, 0=Failure)'})
        return fig
    else:
        site_filtered_df = filtered_df[filtered_df['LaunchSite'] == entered_site]
        fig = px.scatter(site_filtered_df, x='PayloadMass', y='Class',
                         color='BoosterVersion',
                         title=f'Correlation between Payload and Landing Outcome for {entered_site}',
                         labels={'Class': 'Landing Outcome (1=Success, 0=Failure)'})
        return fig

if __name__ == '__main__':
    app.run(debug=True, port=8050)
