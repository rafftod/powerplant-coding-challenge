type_to_energy_keyword = {
    "gasfired": "gas",
    "turbojet": "kerosine",
    "windturbine": "wind",
}


def solve(data):
    # Expressed as a linear programming problem :
    # We have a load to exactly meet.
    # We have n power plants that can produce a certain amount of energy.
    # Constants :
    # load : load to meet during the hour
    # pmin_i : minimal energy p of power plant i, in MW
    # pmax_i : maximal energy p of power plant i, in MW (takes into
    # account the wind percentage)
    # c_i : cost of energy produced by power plant i, in euro/MWh (takes into
    # account the efficiency of the plant)
    # w_i : 1 if the power plant i is a wind turbine, 0 otherwise
    # Variables :
    # x_i : amount of energy produced by power plant i, in MWh
    # b_i : 1 if the power plant i is used, 0 otherwise
    # Objective function :
    # min sum_i c_i * x_i
    # Constraints :
    # sum_i x_i = load
    # pmin_i * b_i <= x_i <= pmax_i * b_i
    # x_i * w_i >= pmax_i * b_i * w_i
    # b_i <= x_i
    # b_i in {0, 1}
    # x_i >= 0

    # mixed integer programming problem that can be solved with the PuLP library
    # Here I will solve it greedily by hand to be able to implement it myself.
    # I will use the following heuristic :
    # 1. Sort the power plants by cost per MWh
    # 2. For each power plant, use it to produce as much energy as possible
    # The problem of this approach is that, if the gas and kerosine prices are
    # respectively very low and very high, the gas power plants won't be used
    # because of their minimal power output, leading to the expensive cost of kerosine plants.
    # This is a problem that could be solved by using a mixed integer programming solver and the above formulation.
    load = data["load"]
    fuels = data["fuels"]
    powerplants = data["powerplants"]
    for powerplant in powerplants:
        if powerplant["type"] == "windturbine":
            # wind turbines can only produce up to their maximum capacity weighted by wind percentage
            powerplant["pmax"] *= fuels["wind"] / 100
            # round it to 1 decimal
            powerplant["pmax"] = round(powerplant["pmax"], 1)
            powerplant["cost"] = 0
        else:
            # turn costs into costs of producing 1 MWh of energy output
            powerplant["cost"] = powerplant["efficiency"] * data["fuels"][type_to_energy_keyword[powerplant["type"]]]
            # round it to 1 decimal
            powerplant["cost"] = round(powerplant["cost"], 1)
        powerplant["p"] = 0
    # sort powerplants by cost
    powerplants.sort(key=lambda powerplant: powerplant["cost"])
    # for each powerplant, produce as much energy as possible
    for powerplant in powerplants:
        if load == 0:
            break
        if powerplant["pmax"] <= load:
            # use the powerplant to its maximum capacity as it does not exceed the load
            powerplant["p"] = powerplant["pmax"]
            load -= powerplant["pmax"]
        elif powerplant["pmin"] <= load and powerplant["type"] != "windturbine":
            # use the plant to fulfill the remaining load
            powerplant["p"] = load
            load = 0
    return [
        {
            "name": powerplant["name"],
            "p": round(powerplant["p"], 1),
        }
        for powerplant in powerplants
    ]
