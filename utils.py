import db

async def take_data(prompt):
    df = db.save(prompt)
    return df

def cinema(date):
    return db.cinema(date)

def movie_ans(movie, date):
    return db.movie(movie,date)

def Films(date):
    return db.Films(date)

def afisha(theater, date):
    return db.afisha(theater, date)