from mesa import Model
from mesa.time import BaseScheduler, RandomActivation, SimultaneousActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

from .agent import PDAgent


class PDModel(Model):
    ''' Multiplayer Prisoner's Dilemma on a grid 
    The Demographic Prisoner's Dilemma is a family of variants on the classic 
    two-player Prisoner's Dilemma. The model consists of agents, each with a 
    strategy of either Cooperate or Defect. Each agent's payoff is based on its 
    strategy and the strategies of its spatial neighbors. After each step of the 
    model, the agents adopt the strategy of their neighbor with the highest 
    total score. 
    '''

    schedule_types = {"Sequential": BaseScheduler,
                      "Random": RandomActivation,
                      "Simultaneous": SimultaneousActivation}

    # This dictionary holds the payoff for this agent,
    # keyed on: (my_move, other_move)

    payoff = {("C", "C"): 1,
              ("C", "D"): 0,
              ("D", "C"): 1.6,
              ("D", "D"): 0}

    def __init__(self, height=50, width=50, schedule_type="Random", p_coop=0.5,
                 payoffs=None, seed=None):
        '''
        Create a new Spatial Prisoners' Dilemma Model.

        Args:
            height, width: Grid size. There will be one agent per grid cell.
            schedule_type: Can be "Sequential", "Random", or "Simultaneous".
                           Determines the agent activation regime.
            p_coop: Initial fraction of the population playing Cooperate
            payoffs: (optional) Dictionary of (move, neighbor_move) payoffs.
        '''
        self.grid = SingleGrid(height, width, torus=True)
        self.schedule_type = schedule_type
        self.schedule = self.schedule_types[self.schedule_type](self)
        self.p_coop = p_coop

        # Create agents
        for x in range(width):
            for y in range(height):
                strategy = 'C' if self.random.random() < self.p_coop else 'D'
                agent = PDAgent((x, y), self, strategy)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)

        self.datacollector = DataCollector({
            "Cooperating_Agents":
            lambda m: len([a for a in m.schedule.agents if a.move == "C"])
        })

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run(self, n):
        ''' Run the model for n steps. '''
        for _ in range(n):
            self.step()
