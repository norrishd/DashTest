"""
My first ever Dash app, just following the tutorial at https://plot.ly/dash/getting-started

"""

import dash
# Library with a component for every HTML tag
import dash_html_components as html
# Higher-level interactive components generated with JavaScript, HTML, and CSS through React.js
import dash_core_components as dcc

# Declare a new app
app = dash.Dash()

# Import default CSS styling
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Define the layout, which is a tree of components:
# a div which contains a heading, a div and a graph
# Components are described entirely through their keyword attributes
app.layout = html.Div(children=[
    # Generates <h1>Wow, a Python web app!</h1>
    # 'children' is always the first attribute; can omit: html.H1('Hello Dash')
    html.H1(children='Wow, a Python web app!'),
    
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

