from pages.restaurantes.Comentario import Comentario
from pages.restaurantes.Restaurante import Restaurante

restaurantes = [
    Restaurante(0, 'Teste 1', '00.jpg', 'Rua Teste 1', '10:00 - 22:00', [
        Comentario(0, 'Nome 1', 'Teste 1'),
        Comentario(1, 'Nome 2', 'Teste 2')
        ]),
    Restaurante(1, 'Teste 2', '01.jpg', 'Rua Teste 2', '10:00 - 22:00', [
        Comentario(2, 'Nome 1', 'Teste 1'),
        Comentario(3, 'Nome 2', 'Teste 2')
        ]),
    Restaurante(2, 'Teste 3', '02.jpg', 'Rua Teste 3', '10:00 - 22:00', [
        Comentario(4, 'Nome 1', 'Teste 1'),
        Comentario(5, 'Nome 2', 'Teste 2')
        ]),
    Restaurante(3, 'Teste 4', '03.jpg', 'Rua Teste 4', '10:00 - 22:00', [
        Comentario(6, 'Nome 1', 'Teste 1'),
        Comentario(7, 'Nome 2', 'Teste 2')
        ])
]