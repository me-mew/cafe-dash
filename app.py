##
# первый проект
# Plotly Dash
# Python
# сайт для кафе
##
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import sqlite3
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=["./assets/styles.css"])

app.title = "Мадам Москвичка"

# SQL
conn = sqlite3.connect('menu.db')
c = conn.cursor()
df = pd.read_sql("SELECT * FROM coffee", conn)
c1 = conn.cursor()
df1 = pd.read_sql("SELECT * FROM desserts", conn)

tab_style = {
    'font-family': 'Arial',
    'font-size': '30px',
    'padding': '6px',
    'color': '#47494a',
    'font-weight': 'Bold',
    'border-top': 'black'
}

# LAYOUT
app.layout = html.Div(children=[
    html.Div([
        html.Div([
            html.Img(src='/assets/logo.png',
                     style={'padding': '5px',
                            'width': '150px',
                            'height': '150px'}),
        ],  style={'margin': '20px',
                   'display': 'inline-block'}),
        html.Div([
            html.H1(children='Мадам Москвичка'),
            html.H3(children='Кафе - кулинария'),
        ],  style={'margin': '10px',
                   'display': 'inline-block'})
    ]),

    # TABS
    dcc.Tabs([
        dcc.Tab(label='Меню',
                style=tab_style,
                selected_style=tab_style,
                children=[
                    html.Div([
                        html.Div([
                            html.H3('Кофе'),
                            dash_table.DataTable(
                                id='table',
                                columns=[{"name": i, "id": i} for i in df.columns],
                                data=df.to_dict('records'),
                                style_as_list_view=True,
                                style_cell={'padding': '10px',
                                            'textAlign': 'left',
                                            'minWidth': '50px', 'width': '50px', 'maxWidth': '50px',
                                            'font-size': '20px',
                                            'font-family': 'Arial',
                                            'color': '#47494a',
                                            'font-weight': 'lighter'},
                                style_header={'backgroundColor': 'white',
                                              'fontWeight': 'bold',
                                              'textAlign': 'left', },
                            )], style = {'margin-left': '25px', 
                                        'margin-right': '20px', 
                                        'margin-bottom': '20px', 
                                        'width': '47%', 'display': 'inline-block'}),
                        html.Div([
                            html.H3('Десерты'),
                            dash_table.DataTable(
                                id='table1',
                                columns=[{"name": i1, "id": i1}
                                         for i1 in df1.columns],
                                data=df1.to_dict('records1'),
                                style_as_list_view=True,
                                style_cell={'padding': '10px',
                                            'textAlign': 'left',
                                            'font-size': '20px',
                                            'font-family': 'Arial',
                                            'color': '#47494a',
                                            'font-weight': 'lighter'},
                                style_header={'backgroundColor': 'white',
                                            'fontWeight': 'bold'},
                            )], style={'margin-left': '20px',
                                       'margin-right': '20px',
                                       'margin-bottom': '20px',
                                       'width': '47%',
                                       'display': 'inline-block'}
                        )
                    ])
                ]),
        dcc.Tab(label='Галерея', style=tab_style, selected_style=tab_style, children=[
            html.Div([
                html.Ul(id='imglist', children=[
                    html.Li([
                        html.Img(src='/assets/cups.jpg',
                                 style={'padding': '5px',
                                        'width': '420px',
                                        'height': '420px'}),
                    ]),
                    html.Li([
                        html.Img(src='/assets/donuts.jpg',
                                 style={'padding': '5px',
                                        'align': 'center',
                                        'width': '420px',
                                        'height': '420px'}),
                    ]),
                    html.Li([
                        html.Img(src='/assets/pie.jpg',
                                 style={'padding': '5px',
                                        'align': 'right',
                                        'width': '420px',
                                        'height': '420px'})
                    ]),
                ]),
            ], style={'padding-top': '40px'}),
        ]),
        dcc.Tab(label='Контакты', style=tab_style, selected_style=tab_style, children=[
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src='/assets/map.jpg',
                                 style={'padding-top': '60px',
                                        'padding-left': '60px',
                                        'width': '350px',
                                        'height': '350px',
                                        'margin-right': '20px'}),
                    ], style={'display': 'inline-block'}),
                    html.Div([
                        html.H3('Контакты', style={'color': '#47494a'}),
                        dcc.Markdown('''**Адрес:** ул. Генерала Белова, 28, корп. 1 

Орехово-Борисово Южное район, Москва, 115583

 **Режим работы:** Ежедневно с 10:00 до 21:00

 **Телефон:** +7‒985‒419‒84‒06

 **Email:** [info@madamos.com](/)
   
    
     
                        ''', style = {'font-family': 'Arial', 
                                    'font-size': '20px', 
                                    'color': '#47494a'}, dedent=False),
                    ], style = {'display': 'inline-block', 
                                'padding-left': '50px'})
                ]),
                html.Div([
                    html.Div([
                        html.H3('Отзывы и Предложения',
                                style={'color': '#47494a'}),
                        # TEXTAREA
                        dcc.Textarea(
                            id='textarea-state-example',
                            placeholder="Вы можете оставить свой отзыв тут..",
                            style = {'width': '110%', 
                                    'height': 100, 
                                    'font-family': 'Arial',
                                    'font-size': '20px', 
                                    'color': 'gray'},
                        ),
                        html.Button('Отправить', 
                                    id='textarea-state-example-button', 
                                    n_clicks=0),
                        html.Div(id='textarea-state-example-output', 
                                style = {'whiteSpace': 'pre-line', 
                                        'font-family': 'Arial', 
                                        'font-size': '20px', 
                                        'color': '#47494a', 
                                        'padding': '5px'})
                    ], style = {'margin': '40px', 
                                'display': 'inline-block'}),
                    html.Div([
                        html.H3('Оцените наш сайт', style = {'color': '#47494a',}),
                        # DROPDOWN
                        dcc.Dropdown(id='demo-dropdown',
                                    options=[{'label': 'Отлично', 'value': 'Отлично'},
                                             {'label': 'Хорошо', 'value': 'Хорошо'},
                                            {'label': 'Плохо', 'value': 'Плохо'}],
                                    value='Отлично',
                                    clearable=False,
                                    placeholder="Оценить..",
                                    style = {'font-family': 'Arial',
                                            'font-size': '20px',
                                            'color': '#47494a',
                                            'text-align': 'middle'}
                        ),
                        html.Div(id='dd-output-container', 
                                style = {'font-family': 'Arial', 
                                        'font-size': '20px', 
                                        'color': '#47494a', 
                                        'padding': '5px'}),
                    ], style = {'margin-left': '100px', 
                                'display': 'inline-block'})
                ], )
            ], style = {'margin': '25px', 
                        'background': 'white'})
        ]),
    ], style={'margin-left': '25px', 
            'margin-right': '25px', 
            'margin-bottom': '25px'}),
    # FOOTER
    html.Footer(
        children=[
            html.H4("2020, Ангелина Фофанова",
                style = {"color": "#47494a",
                        "textAlign": "center"})]
    )
])

# CALLBACK
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    return '\n Ваша оценка "{}"'.format(value)


@app.callback(
    Output('textarea-state-example-output', 'children'),
    [Input('textarea-state-example-button', 'n_clicks')],
    [State('textarea-state-example', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        return '\n Вы отправили: \n{}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
