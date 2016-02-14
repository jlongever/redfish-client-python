from on_http_redfish_1_0 import \
    ApiClient, \
    Configuration, \
    RedfishvApi as redfish
from json import loads,dumps

config = Configuration()
config.host = 'http://localhost:8080/redfish/v1'
config.verify_ssl = False
config.api_client = ApiClient(host=config.host)
config.debug = False
api_client = config.api_client

def get_data():
    return loads(api_client.last_response.data)

def pprint():
    print dumps(get_data(), \
                sort_keys=True, \
                indent=4, \
                separators=(',', ': ')).decode('string-escape')


def getServiceRoot():
    redfish().get_service_root()
    pprint()

def listChassis():
    redfish().list_chassis()
    pprint()

def listPower():
    redfish().list_chassis()
    membersList = get_data().get('Members')
    if membersList is not None:
        for member in membersList:
            id = member.get('@odata.id').split('/redfish/v1/Chassis/')[1]
            redfish().get_power(id)
            pprint()

def listThermal():
    redfish().list_chassis()
    membersList = get_data().get('Members')
    if membersList is not None:
        for member in membersList:
            id = member.get('@odata.id').split('/redfish/v1/Chassis/')[1]
            redfish().get_thermal(id)
            pprint()

getServiceRoot()
listChassis()
listPower()
listThermal()

