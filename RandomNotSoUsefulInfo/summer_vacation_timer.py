import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from datetime import date
from dash.dependencies import Input, Output

summer_start_date = date(2020, 6, 25)
days_till_summer = summer_start_date - date.today()

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
This project was inspired by some very smart boys, Otto and Burt.
Thank you for the insperation and if you have more ideas that you
would like to see here, you know where to find me :)\n \n Adam

"""
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                    html.H2("Days Till Summer vacation\n "),
                    html.H2(str(days_till_summer.days)+ ' Days.')
                     ]
                ),
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, body,
                        # dcc.Interval(id='interval-component',
                        # interval=2000,
                        # n_intervals=0)
                        ])

# @app.callback(Output(''))

if __name__ == "__main__":
    app.run_server()
