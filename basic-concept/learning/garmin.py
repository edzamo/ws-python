import csv
from datetime import datetime, timedelta

# Fecha de inicio
inicio = datetime(2025, 9, 10)

# Entrenamientos por semana: Miércoles, Viernes, Domingo
plan = [
    (4, 30), (6, 54), (7, 51),
    (4.5, 36.5), (6.5, 53.5), (7.5, 52.5),
    (5, 36), (7, 49.5), (8, 48),
    (5, 35), (7.5, 52.5), (8.5, 52.75),
    (6, 41.4), (8, 49.8), (9, 45),
    (6, 40.8), (8.5, 49.5), (9.5, 44.4),
    (6, 40), (9, 49), (10, 72),
    (4, 27.2), (6, 49.8), (8, 48)
]

dias_semana = [0, 2, 4]  # Miércoles, Viernes, Domingo

with open('Plan_8_Semanas_10K.csv', 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Activity Type', 'Distance (km)', 'Total Time (min)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    semana = 0
    for i, (dist, tiempo) in enumerate(plan):
        if i % 3 == 0 and i != 0:
            semana += 1
        fecha = inicio + timedelta(days=semana*7 + dias_semana[i%3])
        writer.writerow({
            'Date': fecha.strftime('%Y-%m-%d'),
            'Activity Type': 'Running',
            'Distance (km)': dist,
            'Total Time (min)': tiempo
        })

print("Archivo CSV generado: Plan_8_Semanas_10K.csv")