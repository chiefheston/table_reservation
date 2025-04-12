from fastapi import APIRouter

from .endpoints import reservations, tables

main_router = APIRouter()

main_router.include_router(reservations.router)
main_router.include_router(tables.router)
