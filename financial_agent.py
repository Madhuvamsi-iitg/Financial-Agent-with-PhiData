from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv
load_dotenv()
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

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA",stream=True)