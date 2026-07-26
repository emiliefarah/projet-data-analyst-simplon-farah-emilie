import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
print(données)
données['chiffre_affaires'] = données ['prix']*données ['qte']
print(données)
figure = px.pie(données, values='chiffre_affaires', names='produit', title="chiffre d'affaires par produit")

figure.write_html('chiffre-affaires-par-produit.html')

print ('chiffre-affaires-par-produit.html')
