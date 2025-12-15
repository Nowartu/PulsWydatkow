
column_alliases = {
    "date": ["Data operacji", "Data księgowania", "Date"],
    "operation_type": ["Rodzaj operacji", "Typ operacji", "Kategoria", "Operation Type", "Typ transakcji"],
    "value": ["Kwota", "Amount"],
    "title": ["Opis", "Tytuł", "Tytuł operacji", "Description", "Opis transakcji"]
}

def get_columns(df):
    mapping = {}
    df_columns_upper = [col.upper() for col in df.columns]
    for standard_name, possible_names in column_alliases.items():
        for name in possible_names:
            if name.upper() in df_columns_upper:
                mapping[df.columns[df_columns_upper.index(name.upper())]] = standard_name
                break
    return mapping


def custom_csv_parser(df):
    df = df.rename(columns=get_columns(df))

    df["description"] = df.iloc[:, df.columns.get_loc("title") + 1:].astype(str).agg("; ".join, axis=1)

    df["value"] = (df["value"] * 100).astype(int)

    result_cols = ["date", "operation_type", "value", "title", "description"]
    df = df[result_cols]

    return df