import os
from griptape.structures import Agent
from griptape.serper.drivers.serper_web_search import SerperWebSearchDriver
from griptape.tools import WebSearchTool


web_search_tool = WebSearchTool(
    web_search_driver=SerperWebSearchDriver(api_key=os.getenv("SERPER_API_KEY"))
)
agent = Agent(tools=[web_search_tool])

agent.run("Find out recent news on Griptape.ai")
