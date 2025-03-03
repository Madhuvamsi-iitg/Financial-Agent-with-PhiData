from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api
import os
from dotenv import load_dotenv

import phi
from phi.playground import Playground,serve_playground_app
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")


web_search_agent = Agent(
    name='web_search_agent',
    role='Search the web for the information',
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

## Financial Agent
financial_agent = Agent(
    name='finance AI agent',
    role='Financial Agent',
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(
        stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True
    )],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team = [web_search_agent, financial_agent],
    instructions=["Always include sources","use table to display the data"],
    show_tool_calls=True,
    markdown=True
)

app = Playground(agents=[financial_agent,web_search_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playground:app",reload=True)