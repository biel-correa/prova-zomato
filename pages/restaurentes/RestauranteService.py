from database import restaurantes

class RestauranteService:
    @classmethod
    def getById(cls, id):
        for item in restaurantes:
            if item.id == id:
                return item
        return None
