import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime
from dash.dependencies import Input, Output, State
import  base64
import io


navbar = dbc.NavbarSimple(
     # children=[
        # dbc.NavItem(dbc.NavLink("Link", href="#")),
    #     dbc.DropdownMenu(
    #         nav=True,
    #         in_navbar=True,
    #         label="Menu",
    #         children=[
    #             dbc.DropdownMenuItem("Entry 1"),
    #             dbc.DropdownMenuItem("Entry 2"),
    #             dbc.DropdownMenuItem(divider=True),
    #             dbc.DropdownMenuItem("Entry 3"),
    #         ],
    #     ),
    # ],
    brand="AEECOM",)
    # brand_href="#",
    # sticky="top",

instruction = """Hi Ashraf,\n this dashboard is designed to help you get
the information you need from Souq. All you need to do is
upload the HTML files using the box on the right and the
results will be mailed to you. You can also see the history of
all items using the below table.

"""

upload_component = dcc.Upload(id='upload-files',
                            children=html.Div([
                                'Drag and Drop or ',
                                html.A('Select Files')
                            ]),
                            style={
                                'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                            # Allow multiple files to be uploaded
                            multiple=True
                            )

body = dbc.Container(
    [
        dbc.Row([
                dbc.Col(
                    [html.H2("Instructions"),html.P(instruction),],
                    md=4,
                ),
                dbc.Col([upload_component,html.Div(id='output-file-upload')]),
            ])
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, body,
                        dcc.Interval(id='interval-component',
                        interval=2000,
                        n_intervals=0)
                        ])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        # if 'csv' in filename:
        #     # Assume that the user uploaded a CSV file
        #     df = pd.read_csv(
        #         io.StringIO(decoded.decode('utf-8')))
        # elif 'xls' in filename:
        #     # Assume that the user uploaded an excel file
        #     df = pd.read_excel(io.BytesIO(decoded))
        #
        if '.html' in filename:
            data = decoded.decode('utf-8')
            with open(filename, "w") as f:
                f.write(data)
            return html.Div(['File uploaded ' + filename])

    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])




@app.callback(Output('output-file-upload', 'children'),
              [Input('upload-files', 'contents')],
              [State('upload-files','filename')])
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        print('list of content is: '+ str(len(list_of_contents)))
        children = [parse_contents(c, n) for c, n in
                zip(list_of_contents, list_of_names)]
        return children

if __name__ == "__main__":
    app.run_server()
