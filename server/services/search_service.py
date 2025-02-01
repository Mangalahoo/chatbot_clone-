from tavily import TavilyClient
import trafilatura 
from config import Settings 

settings = Settings()
tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)



class SearchService :
    def web_search(self,query :str) :
      results = []
      respone = tavily_client.search(query, max_results=10)
      search_results =  respone.get("results",[])
      

      for result in search_results:
          downloaded =  trafilatura.fetch_url(result.get("url"))
          content = trafilatura.extract(downloaded,include_comments=False)

          results.append({
              "title": result.get("title"),
              "content": content,
              "url": result.get("url"),
              "source": result.get("source")
          })
      return results
