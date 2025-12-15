# PulsWydatków
Aplikacja prezentująca domowy budżet w formie wykresów z podziałem na kategorie.
Do programu wczutujemy wyciąg bankowy w fornacie CSV. Program ładuje go do bazy danych PostgreSQL i tworzy dashboard w Grafanie do prezentacji.

### Wymagania:
docker

### Sposób uruchomienia

Uruchomienie aplikacji:

```bash
docker compose up
```

API do wgrywania zestawienia i edycji kategorii: \
(dodawanie zestawienia i edycja kategorii)
```
http://localhost:8000/docs
```
Dashboard w Grafanie:\
```
http://localhost:3000 
```
login/haslo: admin/admin