import pandas as pd
from books.models import Book
from datetime import datetime




def run():
    df = pd.read_csv("books.csv", on_bad_lines="skip")
   
    df["publication_date"] = pd.to_datetime(df["publication_date"], errors='coerce')

    for _, row in df.iterrows():
        try:
            if pd.notnull(row["publication_date"]):
                year = row["publication_date"].year
            else:
                continue  # skip rows with invalid dates

            Book.objects.create(
                title=row["title"],
                author=row["authors"],
                published_year=year,
                rating=row["average_rating"],
                num_pages=row["  num_pages"],
                publisher=row["publisher"]
            )
        except:
            continue
    