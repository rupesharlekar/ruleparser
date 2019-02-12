import yaml
import json

def read_rules_from_yml_file():
    with open("rules.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

        rule_from_yaml = {}

        for d in cfg.values():
            for signal_rule in d:
                rule = signal_rule['expression'].split(" ")             ## For e.g.:   expression: integer > 240.00
                operator = rule[1]                                      ## >
                value = rule[2]                                         ## 240.00

                rule_from_yaml[signal_rule['value_type']] = [operator, value]

    # print(rule_from_yaml)
    return rule_from_yaml

def read_json(filepath):
    with open(filepath) as file:
        signals = json.load(file)

    for signal in signals:
        yield signal