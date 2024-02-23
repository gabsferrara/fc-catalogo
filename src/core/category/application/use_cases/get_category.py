from dataclasses import dataclass
from uuid import UUID
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.exceptions import InvalidCategoryData

from src.core.category.domain.category import Category

@dataclass
class GetCategoryRequest:
    id: UUID

@dataclass
class GetCategoryResponse:
    id: UUID
    name: str
    description: str
    is_active: bool

class CreateCategory:
    def __init__(self, repository: CategoryRepository):
        self.reposity = repository
    
    def execute(self, request: GetCategoryRequest) -> GetCategoryResponse:
        category = self.reposity.get_by_id(id=request.id)
        return GetCategoryResponse(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
        )