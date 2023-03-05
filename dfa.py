class DFA:

    def __init__(self):

        states = {'q0', 'q1', 'q2', 'q3'}
        alphabet = {'f', '+', '-'}
        transition_function = {
            'q0': {'f': 'q1'},
            'q1': {'f': 'q1', '+': 'q2', '-': 'q3'},
            'q2': {'f': 'q1', '+': 'q2'},
            'q3': {'f': 'q1', '-': 'q3'}
        }
        start_state = 'q0'
        accept_states = {'q1'}

        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_str):
        current_state = self.start_state
        for char in input_str:
            if char not in self.alphabet:
                return False
            try:
                current_state = self.transition_function[current_state][char]
            except:
                return False
        return current_state in self.accept_states
