import dash
import dash_html_components as html
import dash_core_components as dcc
import config
from kontent_delivery.client import DeliveryClient
from reports.content_types import build_types_chart
from reports.personas import build_personas_pie
from reports.article_timeline import build_post_timeline

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# KONTENT
client = DeliveryClient(config.project_id, options=config.delivery_options)

bar = build_types_chart(client)
pie = build_personas_pie(client)
timeline = build_post_timeline(client)

app.layout = html.Div([
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Content Types', value='tab-1'),
        dcc.Tab(label='Article Personas', value='tab-2'),
        dcc.Tab(label='Article Post Timeline', value='tab-3'),
    ]),
    html.Div(id='tabs-example-content')
])

@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dcc.Graph(figure=bar)
        ])
    elif tab == 'tab-2':
        return html.Div([
             dcc.Graph(figure=pie)
        ])
    elif tab == 'tab-3':
        return html.Div([
             dcc.Graph(figure=timeline)
        ])


if __name__ == '__main__':
    app.run_server(debug=True)