import numpy as np

np.sqrt(1)


def get_units_from_output(output_unit):
    if isinstance(output_unit, list):
        output_units = output_unit
    elif isinstance(output_unit, str):
        output_units = output_unit.split(".")
    else:
        raise ValueError(f"Output unit format {type(output_unit)} not supported")
    return output_units


def develop_unit(unit):
    if "^" in unit:
        power = float(unit.split("^")[1])
        unit = unit.split("^")[0]
    # elif "(" in unit:
    #     unit = unit.split("(")[1].split(')')[0]
    else:
        power = 1.0
        # function_=None
    return {"symbol": unit, "power": power}  # ,"function":function_)


def unit_coherence(input_units, output_unit):
    output_units = get_units_from_output(output_unit)
    for i, unit in enumerate(input_units):
        input_units[i]["symbols"] = develop_unit(unit["symbol"])
    for i, unit in enumerate(output_units):
        output_units[i] = develop_unit(unit)
    print(input_units, output_units)
    base_units_input = set(unit["symbol"] for unit in input_units)
    base_units_output = set(unit["symbol"] for unit in output_units)
    if base_units_input == base_units_output:
        print("Coherent units, continuing analysis")
    else:
        missing_units = (base_units_input ^ base_units_output) & base_units_output
        raise ValueError(f"Units are not coherent, missing unit(s) :  {missing_units}")
    return input_units, output_units


def get_combinations(input_units, output_units):
    # for unit in output_units:

    return 1


if __name__ == "__main__":
    input_units = [{"name": "distance", "symbol": "m"}, {"name": "time", "symbol": "s"}]
    output_unit = "m.s^-2"
    input_units, output_units = unit_coherence(input_units, output_unit)
