import pytest
import cerberus


@pytest.mark.parametrize("test_input", [1, 5, 10, 20])
def test_post_users(url_api_jsonplaceholder, test_input):
    r = url_api_jsonplaceholder.get(f"posts/{test_input}")
    response = r.json()
    assert response['id'] == test_input


@pytest.mark.parametrize("test_input", [1, 5, 10, 20])
def test_comment_in_post(url_api_jsonplaceholder, test_input):
    r = url_api_jsonplaceholder.get(f"/comments?postId={test_input}")
    response = r.json()
    for id_comment in response:
        print(id_comment['postId'].text())
        assert id_comment['postId'] == test_input


def test_post_comment(url_api_jsonplaceholder, jsonplaceholder_post):
    r = url_api_jsonplaceholder.post(path="posts",
                                     json={"title": "Test43s",
                                          "body": "qa_otus_2020",
                                          "userId": 43242343})
    assert r.status_code == 201


@pytest.mark.parametrize("test_input", range(1, 20, 4))
def test_structure_comment_response(test_input, url_api_jsonplaceholder, schema_jsonplaceholder_comment_json):
    r = url_api_jsonplaceholder.get(f"comment/{test_input}")
    response = r.json()
    v = cerberus.Validator()
    assert v.validate(response, schema_jsonplaceholder_comment_json)


def test_count_photos(url_api_jsonplaceholder, count_element_response):
    for key, value in count_element_response.items():
        r = url_api_jsonplaceholder.get(f"{key}")
        response = r.json()
        assert len(response) == value
