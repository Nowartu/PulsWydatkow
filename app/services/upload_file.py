import pandas as pd
from db.session import engine
from parsers.custom_parser import custom_csv_parser
from services.categories import categorize

def upload_csv_file(file, db):
    try:
        df = pd.read_csv(file, delimiter=",", encoding="utf-8")
    except UnicodeDecodeError:
        file.seek(0)
        df = pd.read_csv(file, delimiter=",", encoding="windows-1250")
    except:
        return False

    df = custom_csv_parser(df)

    df.to_sql(
        name="bank_records",
        con=engine,
        if_exists="append",
        index=False
    )
    categorize(db)
    return True

