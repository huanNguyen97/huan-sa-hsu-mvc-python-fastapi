# import from python
from fastapi import Request
from fastapi.responses import RedirectResponse

# import from owner
import main
from elements.models.game_model import GameModel
from database.dbConfig import SessionLocal

# Config db
db = SessionLocal()

# Game Controller 
# --------------------------------------------------------------
# --------------------------------------------------------------
class GameController():
    # Read all
    def index(request: Request):
        game_list = db.query(GameModel).all()
        return main.templates.TemplateResponse("index.html", {
            "request": request, 
            "game_list": game_list
        })
    

    # Read Detail
    def read_details(request: Request, id: str):
        game_detail = db.query(GameModel).filter(GameModel.id == id).first()
        return main.templates.TemplateResponse("details.html", {
            "request": request, 
            "game": game_detail
        })
    

    # Create game
    # Get
    def get_create_game(request: Request):
        return main.templates.TemplateResponse("create_game.html", { "request": request })
    

    # Post
    def post_create_game(
        request: Request, 
        name: str,
        category,
        brand,
        year_released,
        price
    ):
        game = GameModel(
            id=None, 
            name=name, 
            category=category, 
            brand=brand, 
            year_released=year_released, 
            price=price
        )
        db.add(game)
        db.commit()
        return RedirectResponse(url='/', status_code=302) 
    

    # Update game
    # Get
    def get_update_game(request: Request, id: str):
        game_detail = db.query(GameModel).filter(GameModel.id == id).first()
        return main.templates.TemplateResponse("update_game.html", {
            "request": request, 
            "game": game_detail
        })
    

    # Post
    def post_update_game(
        request: Request, 
        id: str,
        name: str,
        category,
        brand,
        year_released,
        price
    ):
        game = GameModel(
            id=id, 
            name=name, 
            category=category, 
            brand=brand, 
            year_released=year_released, 
            price=price
        )
        db.query(GameModel).filter(GameModel.id == id).update({
            "id": game.id,
            "name": game.name,
            "category": game.category,
            "brand": game.brand,
            "year_released": game.year_released,
            "price": game.price
        })
        db.commit()
        return RedirectResponse(url='/', status_code=302) 


    # Delete game
    def delete_game(request: Request, id: str):
        db.query(GameModel).filter(GameModel.id == id).delete()
        db.commit()
        return RedirectResponse(url='/', status_code=302) 

    
    # Search game
    def search_game(request: Request, keysearch: str):
        game_list = db.query(GameModel).filter(GameModel.name.contains(keysearch))
        return main.templates.TemplateResponse("search.html", {
            "request": request, 
            "game_list": game_list
        })
# --------------------------------------------------------------
# --------------------------------------------------------------
# End Controller