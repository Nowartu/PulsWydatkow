from sqlalchemy import select
from db.models import *
CATEGORIES = {
    "SPOŻYWCZE": ["ZABKA", "LIDL", "BIEDRONKA", "CARREFOUR", "AUCHAN", "ALDI", "KAUFLAND", "DELIKATESY", "SPOZYWCZE", "PUTKA", "FIRMOWY"],
    "JEDZENIE NA MIEŚCIE": ["MCDONALD", "KFC", "BURGER", "PIZZA", "SUBWAY", "STARBUCKS", "COSTA", "GLOVO", "UBER EATS", "PYSZNE", "BISTRO"],
    "TRANSPORT": ["UBER", "BOLT", "FREE NOW", 'TAXI', 'ORLEN', 'SHELL', 'BP', 'CIRCLE K', 'STACJA', 'PALIWO', 'ZTM', 'MPK', 'MPSA', 'PKP', 'AUTOSTRADA', 'PARKING', "INTERCITY"],
    "MIESZKANIE": ['CZYNSZ', 'ADMINISTRACJA', 'WSPOLNOTA', 'SPOLDZIELNIA', 'PRAD', 'GAZ', 'ENERGIA', 'WODA', 'INTERNET', 'ORANGE', 'PLAY', 'PLUS', 'T-MOBILE'],
    "SUBSKRYPCJE": ['NETFLIX', 'SPOTIFY', 'HBO','DISNEY', 'AMAZON PRIME', 'APPLE', 'GOOGLE', 'MICROSOFT', 'ADOBE', 'YOUTUBE', 'DROPBOX', 'ICLOUD'],
    "ZAKUPY ONLINE": ['WWW', 'ALLEGRO', 'AMAZON', 'ZALANDO', 'IKEA', 'X-KOM', 'RTV EURO AGD', 'RESERVED', 'ZARA', 'MEDIA MARKT', 'NEONET', 'H&M', ".COM", ".PL", ".EU"],
    "ZDROWIE": ['APTEKA', 'DOZ', 'ZIKO', 'LEKARZ', 'DENTYSTA', 'MEDYCZNY', 'MEDICOVER', 'LUXMED', 'ENEL-MED', 'DIAGNOSTYKA', "ROSSMANN"],
    "ROZRYWKA": ['KINO', 'TEATR', 'BILET', 'CINEMA', 'BAR', 'STEAM', 'KLUB', 'EPIC GAMES', 'XBOX', 'EVENT', 'PLAYSTATION'],
    "EDUKACJA": ['SZKOLENIE', 'UDEMY', 'COURSERA', 'BOOK', 'KSIEGARNIA', 'EMPIK', 'CERTYFIKAT', 'STUDIA'],
    "FINANSE": ['OPLATA', "PROWIZJA", 'BANK', 'RATA', 'KREDYT', 'LEASING'],
    "WYNAGRODZENIE": ['WYNAGRODZENIE', 'SALARY', 'PENSJA', 'UMOWA'],
    "INWESTYCJE": ['LOKAT', 'OSZCZEDNOSC', 'INWESTYCYJ', 'OBLIGACJ'],
    "ZWROTY": ['ZWROT', 'CASHBACK', 'REFUND']
}


def categorize(db):
    """
    Matches categories to expenses based on category mapping in database.
    :param db: database connection
    :return:
    """
    categories = db.execute(select(Categories)).scalars().all()
    expenses = db.execute(select(BankRecord)).scalars().all()

    for expense in expenses:
        for category in categories:
            if category.keyword in expense.title.upper() or category.keyword in expense.description.upper():
                expense.category = category.category
                break
        else:
            expense.category = 'INNE'


    db.commit()

