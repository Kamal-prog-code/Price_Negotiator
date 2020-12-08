# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import joblib



def cont_res_ret():
    api_url = "http://127.0.0.1:8000/api/content-detail/"
    content_id = "http://127.0.0.1:8000/api/content-id/"
        
    resid = requests.get(content_id).json()
    cid = resid['itemid']
       
    content_id = str(cid)
    URL = api_url+content_id
    response = requests.get(URL).json() 
    return response

def item_res_ret():
    api_url = "http://127.0.0.1:8000/api/item-detail/"
    item_id = "http://127.0.0.1:8000/api/content-id/"
        
    resid = requests.get(item_id).json()
    cid = resid['itemid']
       
    content_id = str(cid)
    URL = api_url+content_id
    response = requests.get(URL).json() 
    return response

class ActionCI(Action):

    def name(self) -> Text:
        return "action_cost"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ent = tracker.latest_message['entities']
        
        response = cont_res_ret()
        print(response)
        for e in ent:
            if e['entity'] == 'info':
                val = e['value']
                if val=='cost' or val == 'price':
                    msg = str(response['cost'])
                else:
                    msg="No details"    
        dispatcher.utter_message(text=msg)

        return []

class ActionRec(Action):

    def name(self) -> Text:
        return "action_recommendn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ent = tracker.latest_message['entities']     
        ls=joblib.load("prediction/costknn.pkl")

        model = lis[0]
        df = lis[1]
        response_it = item_res_ret()
        response_con = cont_res_ret()    

        it = response_it['title']
        ds = response_con['specs']
        q_df = df[df['item_copy'].str.contains(it[:-1]) & df['Description_copy'].str.contains(ds)]
        if q_df is not None:
            i = q_df['item'].values
            j = q_df['Description'].values
            x = pd.DataFrame([[i[0],j[0]]])
            print(x)
            pred = str(int(model.predict(x)[0]))
        else:
            pred = "Not Found any records"  

        dispatcher.utter_message(text=pred)
        if int(pred) > response_con['cost']:
            dispatcher.utter_message(text="PNECBS is showing the best price")

        return []


