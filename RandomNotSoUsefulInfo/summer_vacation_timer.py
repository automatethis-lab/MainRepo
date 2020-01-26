import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime
from dash.dependencies import Input, Output

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
    brand="Days Till School Summer Vacation",
    # brand_href="#",
    # sticky="top",

)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Special Thanks"),
                        html.P(
                            """\
This project was inspired by some very smart friends, Otto and Bert.
Thank you for the insperation and if you have more ideas that you
would like to see here, you know where to find me :)\n \n Adam

"""
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                    html.H2("Time till Summer Vacation\n "),
                    html.H2(id='updated-date')
                     ]

                ),
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, body,
                        dcc.Interval(id='interval-component',
                        interval=1000,
                        n_intervals=0)
                        ])

@app.callback(Output('updated-date', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_time (n):
    summer_start_date = datetime(2020, 6, 19, 12, 00, 00)
    days_till_summer = summer_start_date - datetime.now()
    return str(days_till_summer).split('.')[0]

if __name__ == "__main__":
    app.run_server()
