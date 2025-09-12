from datetime import date
from typing import List, Optional

from pydantic import BaseModel
from src.database.models import MovieStatusEnum


class CountryOut(BaseModel):
    id: int
    code: str
    name: Optional[str]

    class Config:
        from_attributes = True


class GenreOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ActorOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class LanguageOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# --- movie schemas ---

class MovieBase(BaseModel):
    name: str
    date: date
    score: float
    overview: str
    status: MovieStatusEnum
    budget: float
    revenue: float
    country: str
    genres: List[str]
    actors: List[str]
    languages: List[str]

    class Config:
        from_attributes = True


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    name: Optional[str] = None
    date: Optional[date] = None
    score: Optional[float] = None
    overview: Optional[str] = None
    status: Optional[MovieStatusEnum] = None
    budget: Optional[float] = None
    revenue: Optional[float] = None


class MovieListItem(BaseModel):
    id: int
    name: str
    date: date
    score: float
    overview: str

    class Config:
        from_attributes = True


class MovieListResponse(BaseModel):
    movies: List[MovieListItem]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int


class MovieOut(BaseModel):
    id: int
    name: str
    date: date
    score: float
    overview: str
    status: MovieStatusEnum
    budget: float
    revenue: float
    country: CountryOut
    genres: List[GenreOut]
    actors: List[ActorOut]
    languages: List[LanguageOut]

    class Config:
        from_attributes = True


class MovieDetailSchema(MovieOut):
    pass


MovieListResponseSchema = MovieListResponse
MovieDetailSchema = MovieOut

MovieCreateSchema = MovieCreate
MovieUpdateSchema = MovieUpdate

MovieListItemSchema = MovieListItem

CountrySchema = CountryOut
GenreSchema = GenreOut
ActorSchema = ActorOut
LanguageSchema = LanguageOut

#before change MovieDetailSchema