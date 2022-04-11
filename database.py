from pages.restaurantes.Comentario import Comentario
from pages.restaurantes.Restaurante import Restaurante

restaurantes = [
    Restaurante(0, 'Restaurante 1', '00.jpg', 'Vila Sésamo', '10:00 - 22:00', [
        Comentario(0, 'João', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'),
        Comentario(1, 'Pedro', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        ]),
    Restaurante(1, 'Restaurante 2', '01.jpg', 'Groove Street', '12:00 - 00:00', [
        Comentario(2, 'Maria', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'),
        Comentario(3, 'Astolfo', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        ]),
    Restaurante(2, 'Restaurante 3', '02.jpg', 'Las Venturas', '7:00 - 15:00', [
        Comentario(4, 'Leonardo', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'),
        Comentario(5, 'Abnete', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        ]),
    Restaurante(3, 'Restaurante 4', '03.jpg', 'Los Santos', '10:00 - 22:00', [
        Comentario(6, 'Pedro 2', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'),
        Comentario(7, 'Michael', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        ])
]