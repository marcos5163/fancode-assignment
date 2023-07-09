from rest_framework.test import APISimpleTestCase, APITestCase
from model_bakery import baker
from requests import Response as TestResponseObject
from app.models import  News

class BaseTestCase(APISimpleTestCase, APITestCase):
   
    def assertSuccessResponse(self, resp_object: TestResponseObject, message=None):
        status_code = resp_object.status_code
        resp_json = resp_object.json()
        self.assertTrue(status_code >= 200 and status_code <= 299, msg=resp_json)
        if "status_code" in resp_json:
            self.assertEqual(status_code, resp_json["status_code"], msg=resp_json)
        if "status" in resp_json:
            self.assertEqual(resp_json["status"], "success", msg=resp_json)
        if message and "detail" in resp_json:
            self.assertEqual(resp_json["detail"], message, msg=resp_json)

    def assertErrorResponse(self, resp_object: TestResponseObject, message=None):
        status_code = resp_object.status_code
        resp_json = resp_object.json()
        self.assertTrue(status_code >= 400 and status_code < 500, msg=resp_json)
        if "status_code" in resp_json:
            self.assertEqual(status_code, resp_json["status_code"], msg=resp_json)
        if "status" in resp_json:
            self.assertEqual(resp_json["status"], "failure", msg=resp_json)
        if message and "detail" in resp_json:
            self.assertEqual(resp_json["detail"], message, msg=resp_json)

class NewsAPIsTestCase(BaseTestCase):


    def setUp(self) -> None:

        self.sport = baker.make("app.sports", name="cricket")
        
        self.tour = baker.make('app.tours', sportid = self.sport.id, name = "IPL")

        self.match = baker.make('app.matches', tourid = self.tour.id)

    
    def test_news_is_getting_created_for_match(self):
        
        create_news_payload = {"title":"CSK won", 
                            "description":"CSK defeated GT to win IPL 2023", 
                            "matchid":self.match.id}
        response = self.client.post("news/", create_news_payload)

        self.assertSuccessResponse(response)

        news = News.objects.filter(matchid_id = self.match.id).first()
        self.assertEqual(news.title, "CSK won")
        self.assertEqual(news.description, "CSK defeated GT to win IPL 2023")

    def test_news_is_getting_created_for_tour(self):

        create_news_payload = {"title":"CSK won", 
                               "description":"CSK defeated GT to win IPL 2023", 
                               "matchid":self.tour.id}
        response = self.client.post("news/", create_news_payload)

        self.assertSuccessResponse(response)

        news = News.objects.filter(tourid_id = self.tour.id).first()
        self.assertEqual(news.title, "CSK won")
        self.assertEqual(news.description, "CSK defeated GT to win IPL 2023")
    
    def test_get_news_by_match_id(self):

        create_news_payload = {"title":"CSK won", 
                            "description":"CSK defeated GT to win IPL 2023", 
                            "matchid":self.match.id}
        response = self.client.post("news/", create_news_payload)

        self.assertSuccessResponse(response)

        news = News.objects.filter(matchid_id = self.match.id).first()
        self.assertEqual(news.title, "CSK won")
        self.assertEqual(news.description, "CSK defeated GT to win IPL 2023")

        response = self.client.get(f"/news/match/{self.match.id}")

        self.assertSuccessResponse(response)
        self.assertEqual(response.json()[0]['title'], "CSK won")
        self.assertEqual(response.json()[0]['description'], "CSK defeated GT to win IPL 2023")

