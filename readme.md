# Mesa on Glitch demo
## Demographic Prisoner's Dilemma

## Mesa on Glitch

[Mesa](https://github.com/projectmesa/mesa) is an [agent-based modeling](https://en.wikipedia.org/wiki/Agent-based_model) framework for Python that includes a browser-based visualization system. While the visualization is primarily intended to run locally, this project demonstrates how Glitch can be used to deploy a Mesa model online for others to play with.

Running Mesa on Glitch requires two changes: the visualization server must be launched on port 3000, and you need a `start.sh` shell script to install Mesa and launch the visualization. This script in its entirety is:

```
pip3 install mesa --user
python3 run.py
```

## Model Summary

The Demographic Prisoner's Dilemma is a family of variants on the classic two-player [Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner's_dilemma). The model consists of agents on a grid, each with a strategy of either Cooperate (purple) or Defect (orange). Every step of the model, agent play the prisoner's dilemma with all of their neighbors: if their current strategy is Cooperate, they cooperate with all their neighbors, and likewise for Defect. After each step of the model, the agents adopt the strategy of the neighbor with the highest total score.

The Demographic Prisoner's Dilemma demonstrates how simple rules can lead to the emergence of widespread cooperation, despite the Defection strategy dominating each individual interaction game. Run the model and see how zones of cooperation and defection emerge and change. 

The model is also interesting for another reason: it is sensitive to the activation regime. Try changing the activation type between `Random` (agents update their score and strategies in random order), `Sequential` (agents update in fixed order, from the top-left to the bottom-right), and `Simultaneous` (first all agents update their scores, then they all update their behavior simultaneously) and see how the model behavior changes. 

## Files
* ``start.sh``: Script that installs Mesa and launches the model
* ``run.py`` launches the front-end visualization.
* ``pd_grid/``: contains the model and agent classes; 
  * ``agent.py``: Defines the behavior of the individual agent
  * ``model.py``: Defines the overall model class
  * ``server.py``: Sets up the visual portrayal of the agents, and the parameters exposed in the front-end
  * ``__init__.py``: Empty file that makes the scripts in this directory importable.

## Further Reading

This model is adapted from:

Wilensky, U. (2002). NetLogo PD Basic Evolutionary model. http://ccl.northwestern.edu/netlogo/models/PDBasicEvolutionary. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

The Demographic Prisoner's Dilemma originates from:

[Epstein, J. Zones of Cooperation in Demographic Prisoner's Dilemma. 1998.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.8.8629&rep=rep1&type=pdf)
