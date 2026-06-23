# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
# pylint: disable=line-too-long

import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    #
    # Crear carpeta docs
    #
    os.makedirs("docs", exist_ok=True)

    #
    # Leer datos
    #
    df = pd.read_csv("files/input/shipping-data.csv")

    #
    # 1. Envíos por bodega
    #
    plt.figure(figsize=(6, 4))
    df["Warehouse_block"].value_counts().sort_index().plot(kind="bar")
    plt.title("Shipping per Warehouse")
    plt.xlabel("Warehouse")
    plt.ylabel("Number of Shipments")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    #
    # 2. Modo de envío
    #
    plt.figure(figsize=(6, 4))
    df["Mode_of_Shipment"].value_counts().plot(kind="bar")
    plt.title("Mode of Shipment")
    plt.xlabel("Shipment Mode")
    plt.ylabel("Number of Shipments")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    #
    # 3. Promedio de calificación por bodega
    #
    plt.figure(figsize=(6, 4))
    (
        df.groupby("Warehouse_block")["Customer_rating"]
        .mean()
        .sort_index()
        .plot(kind="bar")
    )
    plt.title("Average Customer Rating")
    plt.xlabel("Warehouse")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    #
    # 4. Distribución del peso
    #
    plt.figure(figsize=(6, 4))
    df["Weight_in_gms"].plot(kind="hist", bins=20)
    plt.title("Weight Distribution")
    plt.xlabel("Weight (g)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

    #
    # Crear dashboard HTML
    #
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shipping Dashboard</title>
    </head>
    <body>
        <h1>Shipping Dashboard</h1>

        <img src="shipping_per_warehouse.png" width="45%">
        <img src="mode_of_shipment.png" width="45%">

        <br><br>

        <img src="average_customer_rating.png" width="45%">
        <img src="weight_distribution.png" width="45%">

    </body>
    </html>
    """

    with open("docs/index.html", "w", encoding="utf-8") as file:
        file.write(html)