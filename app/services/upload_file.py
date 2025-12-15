import pandas as pd
from db.session import engine
from parsers.custom_parser import custom_csv_parser
from services.categories import categorize

def upload_csv_file(file, db):
    """
    Uploads CSV band data to database
    :param file: file descriptor with bank data
    :param db: database connection
    :return: bool based on success
    """

    # Try different encodings
    try:
        df = pd.read_csv(file, delimiter=",", encoding="utf-8")
    except UnicodeDecodeError:
        file.seek(0)
        df = pd.read_csv(file, delimiter=",", encoding="windows-1250")
    except:
        return False

    # prepare data to be (remove extra columns and set names)
    df = custom_csv_parser(df)

    # upload to database
    df.to_sql(
        name="bank_records",
        con=engine,
        if_exists="append",
        index=False
    )

    # set categories to uploaded data
    categorize(db)
    return True

