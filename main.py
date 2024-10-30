class MusicalPiece:
    """Музыкальное произведение"""

    def __init__(self, id, name, genre, author, duration):
        self.id = id
        self.name = name
        self.genre = genre
        self.author = author
        self.duration = duration


class Orchestra:
    """Оркестр"""

    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country


class Performance:
    """
    'Выступления оркестров' для реализации
    связи многие-ко-многим
    """

    def __init__(self, orchestra_id, piece_id, date):
        self.orchestra_id = orchestra_id
        self.piece_id = piece_id
        self.date = date


pieces = [
    MusicalPiece(1, 'Симфония № 5', 'Классическая', 'Бетховен', 45),
    MusicalPiece(2, 'Болеро', 'Классическая', 'Равель', 15),
    MusicalPiece(3, 'Концерт для скрипки с оркестром', 'Классическая', 'Чайковский', 30),
    MusicalPiece(4, 'Времена года', 'Классическая', 'Вивальди', 25),
    MusicalPiece(5, 'Лунная соната', 'Романтическая', 'Бетховен', 20),
    MusicalPiece(6, 'Ноктюрн № 2', 'Романтическая', 'Шопен', 10),
    MusicalPiece(7, 'Вальс цветов', 'Романтическая', 'Чайковский', 15),
    MusicalPiece(8, 'Полька', 'Танцевальная', 'Штраус', 5),
    MusicalPiece(9, 'Танго', 'Танцевальная', 'Пьяццолла', 4),
    MusicalPiece(10, 'Маленькая ночная серенада', 'Классическая', 'Моцарт', 12),
]

# Оркестры
orchestras = [
    Orchestra(1, 'Берлинский филармонический оркестр', 'Германия'),
    Orchestra(2, 'Лондонский симфонический оркестр', 'Великобритания'),
    Orchestra(3, 'Филармония', 'Россия'),
    Orchestra(4, 'Виенский филармонический оркестр', 'Австрия'),
    Orchestra(5, 'Симфонический оркестр Мариинского театра', 'Россия'),
    Orchestra(6, 'Королевский оркестр Концертгебау', 'Нидерланды'),
]

# Связь оркестров и музыкальных произведений
performances = [
    Performance(1, 1, '2023-01-01'),
    Performance(1, 2, '2023-02-01'),
    Performance(2, 3, '2023-03-01'),
    Performance(3, 4, '2023-04-01'),
    Performance(4, 5, '2023-05-01'),
    Performance(5, 6, '2023-06-01'),
    Performance(6, 7, '2023-07-01'),
    Performance(1, 8, '2023-08-01'),
    Performance(2, 9, '2023-09-01'),
    Performance(3, 10, '2023-10-01'),
    Performance(4, 1, '2023-11-01'),
    Performance(5, 2, '2023-12-01'),
    Performance(6, 3, '2024-01-01'),
    Performance(1, 4, '2024-02-01'),
    Performance(2, 5, '2024-03-01'),
    Performance(3, 6, '2024-04-01'),
    Performance(4, 7, '2024-05-01'),
    Performance(5, 8, '2024-06-01'),
    Performance(6, 9, '2024-07-01'),
    Performance(1, 10, '2024-08-01'),
]


def main():

    # один ко многим
    one_to_many = [(p.name, p.author, p.duration, o.name)
                   for o in orchestras
                   for p in pieces
                   if p.id == o.id]

    # многие ко многим
    many_to_many_temp = [(o.name, v.orchestra_id, v.piece_id)
                         for o in orchestras
                         for v in performances
                         if o.id == v.orchestra_id]

    many_to_many = [(p.name, p.author, p.duration, o_name)
                    for o_name, o_id, p_id in many_to_many_temp
                    for p in pieces if p.id == p_id]

    # B1
    # «Музыкальное произведение» и «Оркестр» связаны соотношением один-ко-многим.
    # Выведите список всех произведений, длительность которых больше 20 минут,
    # и названия их оркестров.

    print('Задание В1')
    result = [item for item in one_to_many if item[2] > 20]
    for i in result:
        print(i[0], i[3])

    # B2
    # «Музыкальное произведение» и «Оркестр» связаны соотношением один-ко-многим.
    # Выведите список оркестров с минимальной длительностью музыкальных произведений в каждом оркестре,
    # отсортированный по минимальной длительности.

    print('Задание В2')
    min_durations = {}
    for name, author, duration, orchestra_name in one_to_many:
        if orchestra_name not in min_durations or duration < min_durations[orchestra_name]:
            min_durations[orchestra_name] = duration
    sorted_orchestrals = sorted(min_durations.items(), key=lambda x: x[1])
    for orchestra_name, duration in sorted_orchestrals:
        print(f"Оркестр: {orchestra_name}, Длительность самого короткого произведения: {duration}")

    # B3
    # «Музыкальное произведение» и «Оркестр» связаны соотношением многие-ко-многим.
    # Выведите список всех связанных музыкальных произведений и оркестров, отсортированный по музыкальным произведениям,
    # сортировка по оркестрам произвольная.

    print('Задание В3')
    sorted_productions = sorted(many_to_many, key=lambda x: (x[0], x[1]))
    for production in sorted_productions:
        print(production[0], production[3])


if __name__ == '__main__':
    main()
