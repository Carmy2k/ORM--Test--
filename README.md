# ORM con Esempi CRUD per la Tabella "Film" 🎬

Benvenuto nel nostro fantastico repository dedicato all'uso di un ORM per gestire la tabella "Film". Qui imparerai come eseguire operazioni CRUD (Create, Read, Update, Delete) in modo intuitivo e coinvolgente. 🚀

## Introduzione

In questo progetto, utilizzeremo un ORM per semplificare la gestione dei dati nella nostra tabella "Film". Gli ORM rendono l'interazione con il database più intuitiva, consentendoti di concentrarti sulle tue operazioni invece che sulla complessità del database.

## Setup Iniziale

1. Assicurati di avere il tuo ORM preferito installato. Puoi trovare le istruzioni nel readme del rispettivo ORM.

2. Configura la connessione al tuo database nel file di configurazione.

## Esempi di Utilizzo

### 1. Creazione di un Nuovo Film

```python
film = Film(title='Inception', director='Christopher Nolan', year=2010)
db.session.add(film)
db.session.commit()
```

### 2. Lettura di Tutti i Film

```python
all_films = Film.query.all()
for film in all_films:
    print(film.title, film.year)
```

### 3. Aggiornamento di un Film

```python
film = Film.query.filter_by(title='Inception').first()
film.director = 'Updated Director'
db.session.commit()
```

### 4. Cancellazione di un Film

```python
film_to_delete = Film.query.filter_by(title='Inception').first()
db.session.delete(film_to_delete)
db.session.commit()
```

## Contribuisci

Se vuoi arricchire questo progetto con nuovi esempi, migliorie o correzioni di bug, invia una pull request! 🎉

Grazie per unirti a noi nel mondo affascinante degli ORM e delle operazioni CRUD su una tabella di Film! 🎥💻
