# -*- coding: utf-8 -*-
"""Second Dash tutorial, demonstrating the use of a reusable component"""

import dash
import dash_html_components as html
import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')


# A reusable component
def generate_table(dataframe, max_rows=10):
    print(type([html.Tr([html.Th(col) for col in dataframe.columns])]))
    print(len([html.Tr([html.Th(col) for col in dataframe.columns])]))
    print(type([html.Tr([html.Th(col) for col in dataframe.columns])][0]))
    print(len([html.Tr([html.Th(col) for col in dataframe.columns])][0]))
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


# Declare a new app
app = dash.Dash()

# Get that good standard CSS
app.css.append_css({"external_url":
                    "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.H4(children='US Agriculture exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
