from unittest.mock import MagicMock
from uuid import UUID
from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse


from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestCreateCategory:
    def test_create_category_with_valid_date(self):
        repository = InMemoryCategoryRepository() #SQLAlchmy / DjangoORM
        use_case = CreateCategory(repository=repository)
        request = CreateCategoryRequest(
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        response = use_case.execute(request)

        
        assert response.id is not None
        assert isinstance(response, CreateCategoryResponse)
        assert isinstance(response.id , UUID)
        assert len(repository.categories) == 1

        persistence_category = repository.categories[0]
        assert persistence_category.id == response.id
        assert persistence_category.name == "Filme"
        assert persistence_category.description == "Categoria para filmes"
        assert persistence_category.is_active == True