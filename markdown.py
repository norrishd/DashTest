# -*- coding: utf-8 -*-
"""
Dash exposes HTML through the dash_html_components library, however it can be
tedious to write your copy in HTML. For writing blocks of text, you can use the
Markdown component in the dash_core_components library
"""

import dash_core_components as dcc
import dash_html_components as html
import dash

app = dash.Dash()

# Import default CSS styling for font and a bunch of stuff
app.css.append_css({"external_url":
                    "https://codepen.io/chriddyp/pen/bWLwgP.css"})

markdown_text = '''
# Dash and Markdown

## Here's a Subtitle

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server()
