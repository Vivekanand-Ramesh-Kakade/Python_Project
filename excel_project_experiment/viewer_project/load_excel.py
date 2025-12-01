import pandas as pd
from viewer_project.models import Record  

def import_excel_data():
    df = pd.read_excel('data.xlsx')
    for _, row in df.iterrows():
        Record.objects.create(
            name=row['Name'],
            age=row['Age'],
            email=row['Email']
        )
