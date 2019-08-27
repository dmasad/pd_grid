from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from .model import PDModel

def portrayPDAgent(agent):
    '''
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the agent in its current state.
    
    Args:
        agent: An agent object
    
    Returns:
        The portrayal dictionary
    '''
    
    return {
        "Shape": "rect",
        "w": 1,
        "h": 1,
        "Filled": "true",
        "Layer": 0,
        "x": agent.pos[0],
        "y": agent.pos[1],
        "Color": "#7570b3" if agent.isCooroperating else "#d95f02"
    }



# Make a world that is 50x50 cells, and 500x500 pixels.
canvas_element = CanvasGrid(portrayPDAgent, 50, 50, 500, 500)

chart_element = ChartModule([{"Label": "Cooperating_Agents", 
                             "Color": "#7570b3"}])

model_params = {
    "height": 50,
    "width": 50,
    "p_coop": UserSettableParameter("slider", "Initial Cooperators", value=0.5,
                                    min_value=0.1, max_value=0.9, step=0.1),
    "schedule_type": UserSettableParameter("choice", "Scheduler type", value="Random",
                                           choices=list(PDModel.schedule_types.keys()))
}

server = ModularServer(PDModel, [canvas_element, chart_element], 
                       "Prisoner's Dilemma", model_params)
