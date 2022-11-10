import mesa
from agentModels import *
# def compute_gini(model):
#     agent_clean = [agent.clean for agent in model.schedule.agents]
#     x = sorted(agent_clean)
#     N = model.num_agents
#     B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
#     return 1 + (1 / N) - 2 * B

def compute_gini(model):
    agent_wealths = [agent.clean for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B   
#AGENTE BASURA
class trashAgent(mesa.Agent):
    def __init__(self, trash_id,model):
        super().__init__(trash_id, model)
        self.trash = trash_id

#AGENTE LIMPIADOR
class cleanerAgent(mesa.Agent):
    def __init__(self,cleaner_id,model):
        super().__init__(cleaner_id,model)
        self.clean = cleaner_id
    #mover agentes cleaner
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore = True, #moverse a los 8 cuadros circundantes
            include_center = False
        )
        new_position = self.random.choice(possible_steps) #eligir nueva posicion
        self.model.grid.move_agent(self, new_position) #mover el agente
    def step(self):
        self.move()
        cell = self.model.grid.get_cell_list_contents([self.pos])
        trash = [obj for obj in cell if isinstance(obj, trashAgent)]
        if len(trash) > 0:
            othertrash = self.random.choice(trash)
            self.model.grid.remove_agent(othertrash)
        

#NUMERO DE AGENTES
class NumberAgent(mesa.Model):
    #recibe como parámetros: N número de agentes, width y height
    def __init__(self, N, M, width, height): 
        self.num_agents = N #numero de agentes
        self.grid = mesa.space.MultiGrid(width, height, True) #tablero que permite múltiples agentes en misma celda
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        #se crean los agentes aspiradores
        for i in range(N):
            a = cleanerAgent(i,self)
            self.schedule.add(a)
            #Se añaden los agentes al tablero
            x = 1
            y = 1
            self.grid.place_agent(a,(x,y)) #colocar al agente en la posicion x,y = 0

        for i in range(M):
            dirty = trashAgent(i,self)
            x2 = self.random.randrange(0, 10)
            y2 = self.random.randrange(0, 10)
            self.grid.place_agent(dirty,(x2,y2))

        self.datacollector = mesa.DataCollector(
            model_reporters= {"Gini":compute_gini}, agent_reporters= {"Limpieza":"clean"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

