# import from python
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

# import from owner
from elements.controllers.game_controller import GameController

router = APIRouter()


# Router main
# -------------------------------------------------
# -------------------------------------------------
# Read all
@router.get('/', response_class=HTMLResponse)
async def index(request: Request): 
    return GameController.index(request)


# Read detail
@router.get('/read-details/{id}', response_class=HTMLResponse)
async def read_details(request: Request, id: str): 
    return GameController.read_details(request, id)


# Create game
# Get to opening
@router.get('/create-game', response_class=HTMLResponse)
async def create_game(request: Request): 
    return GameController.get_create_game(request)


# Post to executing
@router.post('/create-game', response_class=RedirectResponse)
async def create_game(
    request: Request,
    name: str = Form(...),
    category: str = Form(...),
    brand: str = Form(...),
    year_released: int = Form(...),
    price: float = Form(...)
): return GameController.post_create_game(
    request,
    name,
    category,
    brand,
    year_released,
    price
)


# Update game
# Get to opening
@router.get('/update-game/{id}', response_class=HTMLResponse)
async def update_game(request: Request, id: str): 
    return GameController.get_update_game(request, id)


# Post to executing
@router.post('/update-game/{id}', response_class=RedirectResponse)
async def update_game(
    request: Request,
    id: str,
    name: str = Form(...),
    category: str = Form(...),
    brand: str = Form(...),
    year_released: int = Form(...),
    price: float = Form(...)
): return GameController.post_update_game(
    request,
    id,
    name,
    category,
    brand,
    year_released,
    price
)


# Delete game
@router.get('/delete-game/{id}', response_class=RedirectResponse)
async def delete_game(request: Request, id: str): 
    return GameController.delete_game(request, id)


# Search game
@router.get('/search-game', response_class=HTMLResponse)
async def search_game(request: Request, keysearch: str): 
    return GameController.search_game(request, keysearch)
# -------------------------------------------------
# -------------------------------------------------
# End router

# @router.post('/update-game', response_class=RedirectResponse)
# async def update_game(
#     request: Request,
#     id: str,
#     name: str = Form(...),
#     category: str = Form(...),
#     brand: str = Form(...),
#     year_released: int = Form(...),
#     price: float = Form(...)
# ): return GameController.post_update_game(
#     request,
#     id,
#     name,
#     category,
#     brand,
#     year_released,
#     price
# )