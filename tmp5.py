import dash
import dash_html_components as html
import dash_leaflet as dl
import json

from dash.dependencies import Input, Output

app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div([
    dl.Map([dl.TileLayer(), dl.MarkerClusterGroupTest(positions=[(56,10)])],
            center=(-78.05,42.54), zoom=7, id="map", preferCanvas=True,
            style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}),
    html.Div(id="output")
])


# @app.callback(Output("output", "children"), [Input("marker", "position")])
# def map_click(click_lat_lng):
#     return json.dumps(click_lat_lng)


if __name__ == '__main__':
    app.run_server()