import pytest
from unittest.mock import Mock, patch
from griptape.artifacts import ListArtifact, TextArtifact
from griptape.serper.drivers.serper_web_search.driver import (
    SerperWebSearchDriver,
    SerperType,
)


class TestSerperWebSearchDriver:
    @pytest.fixture
    def driver(self):
        return SerperWebSearchDriver(api_key="test_key")

    @pytest.fixture
    def mock_response(self):
        mock = Mock()
        mock.status_code = 200
        mock.json.return_value = {
            "organic": [
                {
                    "link": "https://example.com",
                    "title": "Example Title",
                    "snippet": "Example Description",
                    "position": 1,
                }
            ],
            "knowledgeGraph": {
                "title": "Knowledge Graph Title",
                "type": "Type",
                "description": "Knowledge Graph Description",
            },
        }
        return mock

    def test_search_with_default_type(self, driver, mock_response):
        with patch("requests.request", return_value=mock_response) as mock_request:
            result = driver.search("test query")

            mock_request.assert_called_once_with(
                "POST",
                "https://google.serper.dev/search",
                headers={"X-API-KEY": "test_key", "Content-Type": "application/json"},
                data='{"q": "test query"}',
            )

            assert isinstance(result, ListArtifact)
            assert len(result.value) == 2  # One organic result + knowledge graph

    def test_search_with_date_range(self, driver, mock_response):
        driver.date_range = "m"
        with patch("requests.request", return_value=mock_response):
            result = driver.search("test query")
            assert isinstance(result, ListArtifact)

    def test_invalid_api_response(self, driver):
        mock_error_response = Mock()
        mock_error_response.status_code = 401
        mock_error_response.reason = "Unauthorized"

        with patch("requests.request", return_value=mock_error_response):
            with pytest.raises(Exception) as exc_info:
                driver.search("test query")
            assert "401" in str(exc_info.value)
            assert "Unauthorized" in str(exc_info.value)

    @pytest.mark.parametrize(
        "search_type",
        [SerperType.NEWS, SerperType.PLACES, SerperType.IMAGES, SerperType.PATENTS],
    )
    def test_different_search_types(self, search_type):
        driver = SerperWebSearchDriver(api_key="test_key", type=search_type.value)
        mock_response = Mock()
        mock_response.status_code = 200

        # Different response structure for each type
        response_data = {
            SerperType.NEWS: {
                "news": [{"link": "url", "title": "title", "snippet": "desc"}]
            },
            SerperType.PLACES: {"places": [{"title": "place", "address": "address"}]},
            SerperType.IMAGES: {"images": [{"imageUrl": "url", "title": "title"}]},
            SerperType.PATENTS: {"organic": [{"title": "patent", "link": "url"}]},
        }

        mock_response.json.return_value = response_data[search_type]

        with patch("requests.request", return_value=mock_response):
            result = driver.search("test query")
            assert isinstance(result, ListArtifact)
