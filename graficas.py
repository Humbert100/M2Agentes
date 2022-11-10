from agentModels import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


########################################################

#PRIMERA GRAFICA
all_clean = []
# This runs the model 100 times, each model executing 10 steps.
for j in range(200):
    # Run the model
    model = NumberAgent(20, 30,10,10)
    for i in range(10):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        all_clean.append(agent.clean)

plt.hist(all_clean, bins=range(max(all_clean) + 1))
plt.show()

########################################################

#SEGUNDA GRÁFICA
agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation="nearest")
plt.colorbar()
plt.show()

########################################################
#TERCERA GRÁFICA

# params = {"width": 10, "height": 10, "N": range(10, 250, 10), "M": range(10,300,10)}

# results = mesa.batch_run(
#     NumberAgent,
#     parameters=params,
#     iterations=5,
#     max_steps=100,
#     number_processes=1,
#     data_collection_period=1,
#     display_progress=True,
# )

# results_df = pd.DataFrame(results)
# print(results_df.keys())

# results_filtered = results_df[(results_df.AgentID == 0) & (results_df.Step == 100)]
# N_values = results_filtered.N.values
# gini_values = results_filtered.Gini.values
# plt.scatter(N_values, gini_values)
# plt.show()
