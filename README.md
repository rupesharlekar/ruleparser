Briefly describe the conceptual approach you chose! What are the trade-offs?
    - The rules were created using the yml file. 
    - The rules were then serialized using the the yaml.load method . A dictionary was used to save this rules (keys as the value_type and its value as list of 
      rule_operator and rule_value respectively)
    - json.load was used to read the signal from the json file. 
    - An generator was used as it will pull one value each instead of using lot of memory to save the incoming signals in a list.
    - eval() from python is used heavily to evaluate an expression
    - All dates are first converted to epoch before comparison
       
What's the runtime performance? What is the complexity? Where are the bottlenecks?
    - the solution will run in O(n) time complexity - depending on the length of the input json file 
    - the space complexity for the solution will always be constant O(1)
    - The bottlenecks are in reading the json and yml file using 'with' context manager
    
If you had more time, what improvements would you make, and in what order of priority?
    In the order of priority
    - I will have improved more on the datetime rule , adding more rule instead of coding for just 'now'
    - A object oriented approach with class and its members
    - More rule to cover postivity test , for now the rules are just for violations
    - Write the pytest test for the is_signal_violation definition
    