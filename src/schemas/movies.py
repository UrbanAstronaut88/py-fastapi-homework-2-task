from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict, field_validator
from src.database.models import MovieStatusEnum


class CountryOut(BaseModel):
    id: int
    code: str
    name: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class GenreOut(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class ActorOut(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class LanguageOut(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


# --- movie schemas ---

class MovieBase(BaseModel):
    name: str = Field(..., max_length=255)
    date: date
    score: float = Field(..., ge=0, le=100)
    overview: str
    status: MovieStatusEnum
    budget: float = Field(..., ge=0)
    revenue: float = Field(..., ge=0)
    country: str = Field(..., min_length=2, max_length=3)
    genres: List[str]
    actors: List[str]
    languages: List[str]

    @field_validator("date")
    def validate_date(cls, value):
        max_date = date(date.today().year + 1, 12, 31)
        if value > max_date:
            raise ValueError("Date cannot be more than one year in the future.")
        return value

    model_config = ConfigDict(from_attributes=True)


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    date: Optional[date] = None
    score: Optional[float] = Field(None, ge=0, le=100)
    overview: Optional[str] = None
    status: Optional[MovieStatusEnum] = None
    budget: Optional[float] = Field(None, ge=0)
    revenue: Optional[float] = Field(None, ge=0)
    country: Optional[str] = Field(None, min_length=2, max_length=3)
    genres: Optional[List[str]] = None
    actors: Optional[List[str]] = None
    languages: Optional[List[str]] = None

    @field_validator("date")
    def validate_date(cls, value):
        if value is None:
            return value
        max_date = date(date.today().year + 1, 12, 31)
        if value > max_date:
            raise ValueError("Date cannot be more than one year in the future.")
        return value

    model_config = ConfigDict(from_attributes=True)


class MovieListItem(BaseModel):
    id: int
    name: str = Field(..., max_length=255)
    date: date
    score: float = Field(..., ge=0, le=100)
    overview: str

    @field_validator("date")
    def validate_date(cls, value):
        max_date = date(date.today().year + 1, 12, 31)
        if value > max_date:
            raise ValueError("Date cannot be more than one year in the future.")
        return value

    model_config = ConfigDict(from_attributes=True)


class MovieListResponse(BaseModel):
    movies: List[MovieListItem]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int

    model_config = ConfigDict(from_attributes=True)


class MovieOut(BaseModel):
    id: int
    name: str = Field(..., max_length=255)
    date: date
    score: float = Field(..., ge=0, le=100)
    overview: str
    status: MovieStatusEnum
    budget: float = Field(..., ge=0)
    revenue: float = Field(..., ge=0)
    country: CountryOut
    genres: List[GenreOut]
    actors: List[ActorOut]
    languages: List[LanguageOut]

    @field_validator("date")
    def validate_date(cls, value):
        max_date = date(date.today().year + 1, 12, 31)
        if value > max_date:
            raise ValueError("Date cannot be more than one year in the future.")
        return value

    model_config = ConfigDict(from_attributes=True)


class MovieDetailSchema(MovieOut):
    pass


MovieListResponseSchema = MovieListResponse
MovieCreateSchema = MovieCreate
MovieUpdateSchema = MovieUpdate
MovieListItemSchema = MovieListItem
CountrySchema = CountryOut
GenreSchema = GenreOut
ActorSchema = ActorOut
LanguageSchema = LanguageOut
