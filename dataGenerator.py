from random import seed
from random import random
import pandas as pd
import pandas

Sim_time = 60


def randomValue(Rc, xx):
    dx = []
    if xx == 1:
        dx = ([(Rc[0] + (Rc[1] - Rc[0]) * random()) for i in range(60)])
        dx = [int(i) for i in dx]
    else:
        dx = ([(Rc[0] + (Rc[1] - Rc[0]) * random()) for i in range(60)])
    return dx


product_Demand = [5200, 6500]
Finishied_good = [400, 600]
Processing_time = [1.5, 2]
Monthly_time = [260, 286]
PWorkerCost = [20000, 25000]
Safety = [1.001, 1.002]
Scrape_Rate = [0.1, 0.15]
ScrapeCost = [200, 250]
Sale_Price = [32000, 38000]
Maintenance_cost = [20000, 40000]
Co2 = 2.68
Fuel_usage = [545, 815]
fuel_fuel_vehicles = [70, 100]

P_demand = randomValue(product_Demand, 1)
F_goods = randomValue(Finishied_good, 1)
P_time = randomValue(Processing_time, 0)
PWcost = randomValue(PWorkerCost, 0)
Safety_cost = randomValue(Safety, 0)
S_Rate = randomValue(Scrape_Rate, 0)
Sca_cost = randomValue(ScrapeCost, 0)
Number_of_machines = 2
salesP = randomValue(Sale_Price, 0)
mtceCost = randomValue(Sale_Price, 0)
Fuel_machine = randomValue(Fuel_usage, 0)
Fuel_vehicles = randomValue(fuel_fuel_vehicles, 0)
Req_Processing_time = [a - b for (a, b) in zip(P_demand, F_goods)]
Production_time = [a * b for (a, b) in zip(Req_Processing_time, P_time)]
P_workers = [a / b for (a, b) in zip(Req_Processing_time, P_time)]
P_workers = [int(i) for i in P_workers]

P_workersCost = [a * b for (a, b) in zip(P_workers, PWcost)]
T_workerCost = [a * b for (a, b) in zip(P_workersCost, Safety_cost)]

Total_output = [a / b for (a, b) in zip(Production_time, P_time)]
Total_output = [(Total_output[i] * Number_of_machines) for i in range(len(Total_output))]
Total_output = [int(i) for i in Total_output]

Scr_prod = [a * b for (a, b) in zip(Total_output, S_Rate)]
TScr_cost = [a * b for (a, b) in zip(Scr_prod, Sca_cost)]
Quality_pd = [a - b for (a, b) in zip(Total_output, Scr_prod)]
Quality_pd = [int(i) for i in Quality_pd]

Total_pd_Cost = [a + b for (a, b) in zip(TScr_cost, T_workerCost)]
Gross_cost = [((Total_pd_Cost[i] * 1.02) + mtceCost[i]) for i in range(len(Total_pd_Cost))]
Total_sales = [a * b for (a, b) in zip(Quality_pd, salesP)]
Revenue = [a - b for (a, b) in zip(Total_sales, Gross_cost)]
Fuel = [a + b for (a, b) in zip(Fuel_machine, Fuel_vehicles)]
Emission = [((Fuel[i] * Co2) + mtceCost[i]) for i in range(len(Fuel))]

df = pandas.DataFrame(data={"Demond": P_demand, "Finished Good": F_goods, "Production time": Production_time,
                            "Production workers": P_workers, "Production workers cost": T_workerCost,
                            "Total output": Total_output, "Quality product": Quality_pd, "Gross_cost ": Gross_cost,
                            "Total sales ": Total_sales, "Revenue  ": Revenue, "Emission ": Emission})
df.to_csv("Sim30.csv", sep=',', index=False)