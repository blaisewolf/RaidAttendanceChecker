
import requests
import json

TOKEN_URI = "https://www.warcraftlogs.com/oauth/token"
WCLOGS_CLINET_ID = "9ca5751d-a4a1-4e7d-b46c-dbbf6189de9e"
WCLOGS_CLIENT_SECRET_ID = "V0Q1sahMkZ3ejuf7tFVQ0ZoyPKKaz5krwbNJgVBN"
PUBLIC_API_URI = "https://www.warcraftlogs.com/api/v2/client"
TEST_LOG_ID = "jcwLBJZb6rV78y4C"

data = {
    'grant_type': 'client_credentials',
}

response = None
with requests.Session() as session:
    response = session.post(TOKEN_URI, data=data, auth=(WCLOGS_CLINET_ID, WCLOGS_CLIENT_SECRET_ID))

if response.status_code == 200:
    with open("Data/wclogs_credentials.json", "w") as credentials:
        json.dump(response.json(), credentials)
else:
    print(f"Bad response {response.status_code}")

token = None
accesstoken = None
with open("Data/wclogs_credentials.json", "r+", encoding="utf8") as credentials:
    token = json.load(credentials)
    accesstoken = token.get("access_token")

header = {"Authorization": f"Bearer {accesstoken}"}
query = """query($code:String){
                reportData{
                    report(code:$code) {
                        masterData {
                            actors(type: "Player") {
                                name
                                server
                            }
                        }
                    }
                }
            }"""

def get_data(query, **kwargs):
    data = {"query": query, "variables": kwargs}
    with requests.Session() as session:
        session.headers = header
        response = session.get(PUBLIC_API_URI, json = data)
        return response.json()

def get_names(response_json):
    character_json = json.load(response_json)
    character_list = []
    character_list.append()

def get_character_list():
    character_list = []
    raw_data = get_data(query, code=TEST_LOG_ID)
    filtered = raw_data.get("data").get("reportData").get("report").get("masterData").get("actors")
    for character_data in filtered:
        character = f"{character_data.get("name")}-{character_data.get("server")}"
        character_list.append(character)
    return character_list