from utils.model_loaders import Modelloader
from tools.place_search import Placesearch
from tools.weather_info import Weatherinfo
from tools.calculator import Calculator
from tools.currency_conversion import Currencyconversion
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition


class Graphbuilder():
    def __init__(self):
        self.tools=[
            #
        ]
        pass


    def agent_function(self, state:MessagesState):
        user_question = state['messages']
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return{"messages": [response]}


    def build_graph(self):
        graph_builder = StateGraph(MessagesState)

        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditonal_edges("agent", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)


        self.graph = graph_builder.compile()
        return self.graph
    
    def __call__(self):
        pass


