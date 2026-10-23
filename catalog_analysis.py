import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1. Разминка: переменные, числа, math
# Средняя оценка по каталогу, округлённая до одного знака

def average_rating(movies):
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)

# Самый старый фильм в годах, самый новый фильм в годах, среднее

def catalog_age_stats(movies, current_year=2026):
    oldest_film = current_year - min(movie["year"] for movie in movies)
    newest_film = current_year - max(movie["year"] for movie in movies)
    total_age = sum(current_year - movie["year"] for movie in movies)
    average_film = math.ceil(total_age / len(movies))
    return (oldest_film, newest_film, average_film)

# Перевод продолжительности в минутах в формат часы, минуты

def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

print("Средний рейтинг фильма:", average_rating(movies))
print(
    "Возраст фильма в годах (самый старый, самый новый, средний):", 
    catalog_age_stats(movies)
)
print("Продолжительность фильма:")
for movie in movies:
    print(f"{movie['title']}: {duration_in_hours(movie['duration_min'])}")

# Этап 2. Условия и match
# Рейтинг фильма по категориям

def rating_tier(rating):
    if rating >= 7:
        return "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"

print("Рейтинг фильма:")
for movie in movies:
    print(
        f"{movie['title']}: {movie['rating']} — {rating_tier(movie['rating'])}"
    )

# Метка фильма по году выпуска

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

print("Метка фильма по году выпуска:")
for movie in movies:
    print(f"{movie['title']} ({movie['year']}): {decade_label(movie['year'])}")

# Этап 3. Циклы
# Названия всех фильмов, кроме комедий

print("Названия всех фильмов, кроме комедий:")
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

# Первый по порядку в списке фильм с рейтингом выше 9.0

def find_first_top(movie):
    i = 0
    while i < len(movie):
        if movie[i]["rating"] > 9.0:
            print("Первый шедевр:", movie[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


find_first_top(movies)
find_first_top(movies[:7])

# Количество фильмов длиннее threshold минут

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


threshold = 120
print(f"Фильмов длиннее {threshold} минут:", count_long_movies(movies, threshold))

# Этап 4. Строки
# Приведение строки к Title Case (каждое слово с заглавной буквы)

def normalize_title(title):
    words = title.split()
    new_words = []
    for word in words:
        new_words.append(word[0].upper() + word[1:])
    return " ".join(new_words)


# Название через дефис, все буквы маленькие

def make_slug(title):
    return title.lower().replace(" ", "-")


# Единая строка с описанием фильма

def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


print(normalize_title("silent hours"))
print(make_slug("Silent Hours"))
print(format_report_line(movies[7]))
