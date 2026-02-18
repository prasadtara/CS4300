from unittest.mock import Mock, patch
from src.task7 import get_status_code

def test_get_status_code_mocked():
    fake_resp = Mock()
    fake_resp.status_code = 200

    with patch("src.task7.requests.get", return_value=fake_resp) as mocked_get:
        assert get_status_code("https://example.com", timeout=1.0) == 200
        mocked_get.assert_called_once()
