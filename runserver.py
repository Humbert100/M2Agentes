from agentModels import *
import mesa


def agent_portrayal(agent):
    if type(agent) == cleanerAgent:
        portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}
    else:
        portrayal ={"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "blue",
                 "r": 0.5}
    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(
    NumberAgent, [grid], "Money Model", {"N": 5, "M":8, "width":10, "height":10}
)

server.port = 8521 # The default
server.launch()
