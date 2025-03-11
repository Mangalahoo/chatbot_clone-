import asyncio
from fastapi import FastAPI, WebSocket

from pydantic_models.chat_body import ChatBody
from services.llm_service import LLMService
from services.sort_source_services import SortSourceServices
from services.search_service import SearchService

app = FastAPI()

search_service = SearchService()
sort_source_services = SortSourceServices()
llm_service = LLMService()


#chat websocket
@app.websocket("/ws/chat")
async def websocket_chat_endpoint (websocket: WebSocket):
    await websocket.accept()

    try : 
        await asyncio.sleep(0.1)

        data = await websocket.receive_json()
        query = data.get("query")

        search_results = search_service.web_search(query)
        sorted_results = sort_source_services.sort_source(query,search_results)
        await websocket.send_json({
            "type":"search_results",
            "data":sorted_results
        })
        
        
        
        for chunk in  llm_service.generate_response(query,sorted_results):
            await asyncio.sleep(0.1)
            await websocket.send_json({
                "type":"content",
                "data":chunk
            })
        
  
    except :
        print("unexpected error occured")
    finally:
            await websocket.close()

#chat 
@app.post("/chat")
def chat_endpoint(body :ChatBody):
    search_results = search_service.web_search(body.query)
    sorted_results = sort_source_services.sort_source(body.query,search_results)
    print(sorted_results)
    
    response = llm_service.generate_response(body.query,sorted_results)
    return response 
 