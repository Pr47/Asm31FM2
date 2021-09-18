class Action:
    def __init__(self):
        pass

    def action_name(self):
        pass

    def sanitize_input_output_files(self, inputs, outputs):
        pass


class DumpBasicBlockAction(Action):
    def action_name(self):
        return 'basic block dump'

    def sanitize_input_output_files(self, inputs, outputs):
        pass


def pick_actions(options, inputs, outputs):
    pass
