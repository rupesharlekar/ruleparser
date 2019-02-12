from datetime import datetime
import utils

def find_violating_signals(filepath):

    total_signals = 0
    violated_signals =[]

    incoming_signal = utils.read_json(filepath)

    for signal_details in incoming_signal:

        total_signals +=1

        try:
            if signal_details['value_type'] in ['String','Integer','Datetime']:
                if is_signal_violation(signal_details['value_type'],signal_details['value']):
                    violated_signals.append(signal_details['signal'])
            else:
                raise KeyError("signal value type is not supported")
        except Exception as err:
            print(err)

    return (total_signals, violated_signals)

def is_signal_violation(signal_value_type, signal_value):
    is_violation = False

    precedence = {'LOW': 0, 'MEDIUM': 1, 'HIGH': 2}

    rules_from_yml = utils.read_rules_from_yml_file()

    if signal_value_type == 'Integer':
        operator = rules_from_yml['Integer'][0]
        rule_value = rules_from_yml['Integer'][1]

        if eval(str(signal_value) + str(operator) + str(rule_value)):
            is_violation = True

    elif signal_value_type == 'String':
        operator = rules_from_yml['String'][0]
        rule_value = rules_from_yml['String'][1]

        if eval(str(precedence[signal_value]) + str(operator) + str(precedence[rule_value])):
            is_violation = True

    elif signal_value_type == 'Datetime':
        operator = rules_from_yml['Datetime'][0]
        rule_value = rules_from_yml['Datetime'][1]

        dateobj = datetime.strptime(signal_value, '%Y-%m-%d %H:%M:%S')
        epoch_signal_value_datetime = dateobj.timestamp()

        if rule_value == 'now':
            epoch_rule_datetime = datetime.now().timestamp()

        if eval(str(epoch_signal_value_datetime) + str(operator) + str(epoch_rule_datetime)):
            is_violation = True

    return is_violation

if __name__ == "__main__":

    total_signals, violated_signals = find_violating_signals("raw_data.json")

    print("Total signals:",total_signals)
    print("Number of violations found:",len(violated_signals))
    print("Violations:",violated_signals)