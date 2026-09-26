from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
import os

load_dotenv()


llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course with search tool!")
    result = agent.invoke({"messages":HumanMessage(content="Search for Top 3 movies from director Christopher Nolan based on gross earnings")})
    print(result)


if __name__ == "__main__":
    main()
