from unittest.mock import MagicMock, create_autospec
from uuid import UUID
import uuid
import pytest
from src.core.category.domain.category import Category
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.domain.category_repository import CategoryRepository

from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse
from src.core.category.application.use_cases.exceptions import InvalidCategoryData


class TestGetCategory:
    def test_return_found_category(self):
        category = Category(
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category
        use_case = GetCategory(repository=mock_repository)
        request = GetCategoryRequest(
            id=category.id
        )

        response = use_case.execute(request)

        assert response == GetCategoryResponse(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
        )


    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info: 
            use_case.execute(CreateCategoryRequest(name=""))
            
        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "name cannot be empty"

