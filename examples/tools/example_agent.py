import os
from griptape.structures import Agent
from griptape.serper.drivers.serper_web_search.driver import SerperWebSearchDriver
from griptape.tools import WebSearchTool
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

web_search_tool = WebSearchTool(
    web_search_driver=SerperWebSearchDriver(
        api_key=os.getenv("SERPER_API_KEY"), type="news", date_range="d"
    )
)
agent = Agent(tools=[web_search_tool])

agent.run("Recent news on Trump please")
