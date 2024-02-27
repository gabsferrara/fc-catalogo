import uuid

import pytest
from src.core.category.domain.category import Category
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound

class TestGetCategory:
    def test_get_category_by_id(self):
        category_filme = Category(
            name="Filme",
            description="Categoria para filmes",
            is_active=True
        )
        category_serie = Category(
            name="Serie",
            description="Categoria para serie",
            is_active=True
        )
        repository = InMemoryCategoryRepository(
            categories=[category_filme, category_serie]
        ) 
        use_case = GetCategory(repository=repository)
        request = GetCategoryRequest(
            id=category_filme.id,
        )
        response = use_case.execute(request)

        
        assert response == GetCategoryResponse(
            id=category_filme.id,
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )

            
    def test_get_category_by_id_when_id_not_exist(self):
        category_filme = Category(
            name="Filme",
            description="Categoria para filmes",
            is_active=True
        )
        category_serie = Category(
            name="Serie",
            description="Categoria para serie",
            is_active=True
        )
        repository = InMemoryCategoryRepository(
            categories=[category_filme, category_serie]
        ) 
        use_case = GetCategory(repository=repository)
        request = GetCategoryRequest(
            id=uuid.uuid4(),
        )

        with pytest.raises(CategoryNotFound) as exc:
            use_case.execute(request)

    