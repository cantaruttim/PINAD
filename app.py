# bibliotecas para o dash
import dash
from dash import dcc
import dash_core_components as html
from dash.dependencies import Input, Output, ClientsideFunction
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import json


df = pd.read_csv('dados/dados.csv')

br_states = json.load(open('geojson/br_states.json'))

br_states['features'][2]['properties']['SIGLA'] # retorna a sigla do estado

