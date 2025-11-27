import pandas as pd
import matplotlib.pyplot as plt 

import seaborn as sns

# Laad het CSV-bestand


def makeScatter():
    df = pd.read_csv('Own_Project/mce.csv')

    # Converteer tijd naar minuten
    df['time_min'] = df['speedrun_time'] / 6000

    # Selecteer top 100 plaatsen
    df_top100 = df[df['place'] <= 100].copy()

    plt.figure(figsize=(12, 7))

    # Boxplot per categorie om de spreiding van tijden te tonen
    sns.boxplot(
        data=df_top100,
        x='cat_name',
        y='time_min'
    )

    plt.xlabel('Categorie')
    plt.ylabel('Speedrun Time (minutes)')
    plt.title('Spreiding van Speedrun Tijd per Categorie (Top 100)')
    plt.show()

def make_stacked_countplot():
    df = pd.read_csv('Own_Project/mce.csv')
    df_top100 = df[df['place'] <= 100].copy()

    plt.figure(figsize=(12, 7))

    # Gestapelde countplot met Seaborn (histplot met multiple="stack")
    sns.histplot(
        data=df_top100,
        x='cat_name',
        hue='timing_type',
        multiple='stack',
        shrink=0.8,
        discrete=True
    )

    plt.xlabel('Categorie')
    plt.ylabel('Aantal runs (count)')
    plt.title('Gestapelde countplot per timing type (Top 100)')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()


makeScatter()
make_stacked_countplot()
