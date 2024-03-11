class GuiDisplay:
    
    def list_options(self, choices):
        print(*choices, sep = "\n")

class GuiInputHandling:
    
    def take_input(self, input_type):
        choice = input()
        return choice
