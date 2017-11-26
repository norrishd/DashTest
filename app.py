"""
My first ever Dash app, just following the tutorial at https://plot.ly/dash/getting-started

"""

import dash
# Library with a component for every HTML tag
import dash_html_components as html
# Higher-level interactive components with JS, HTML, and CSS through React.js
import dash_core_components as dcc

# Declare a new app
app = dash.Dash()

# Import default CSS styling for font and a bunch of stuff
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# A JSON-like dictionary to use as CSS style information
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Define the layout, which is a tree of components:
# a div which contains a heading, a div and a graph
# Components are described entirely through their keyword attributes
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    # Generates <h1>Wow, a Python web app!</h1>
    # 'children' is always 1st attribute; can omit, e.g. html.H1('Hello Dash')
    html.H1(
        children='Wow, a Python web app!',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Here is a test bar chart to appreciate.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Melbourne'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Canberra'},
            ],
            'layout': {
                'title': 'Australia East Coast Vis',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': colors['text']
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
