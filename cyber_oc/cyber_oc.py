import curses
class Cyber_oc:
    def __init__(self):
        self.version="1.0"
        self.author="Thyéz de oliveira"
        self.running=True
        self.setup_header()
        self.setup_main_options()
        self.selected_option=1

    def setup_header(self) -> None:
        self.header_template=[
            "----------------------",
            "======================",
            f"-:- ¢¥be® Oc€lot {self.version} -:-",
            f"Autor: {self.author}",
            "======================",
            "----------------------"
            ]
    
    def setup_main_options(self) -> None:
        self.options = [{
            "id":1,
            "name":"criar_pasta",
            "text":"NOVO PROJETO",
            "action":self.criar_pasta
        },{
            "id":2,
            "name":"criar_arquivo",
            "text":"NOVO ARQ",
            "action":self.criar_arquivo
        },{
            "id":3,
            "name":"rodar_script",
            "text":"RODAR SCRIPTS",
            "action":self.rodar_script
        },{
            "id":4,
            "name":"ativar_virtual_env",
            "text":"TVENV",
            "action":self.ativar_virtual_env
        }]
    
    def limpar_terminal(self) -> None:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def criar_pasta(self):
        print("...criando projeto.")
        import os
        pasta_raiz = os.path.dirname(os.path.abspath(__file__))
        nome_diretorio = "novo_projeto_cyoc"
        try:
            os.makedirs(os.path.join(pasta_raiz, nome_diretorio))
        except Exception as e:
            if e.errno == 17:
                print("o diretorio ja existe")
    
    def criar_arquivo(self):
        print("...criando arquivo.")
    
    def rodar_script(self):
        print("...rodando script.")
    
    def ativar_virtual_env(self):
        print("...avenv.")
    
    def display_options(self, stdscr) -> None:
        y_pos=10
        x_pos=stdscr.getmaxyx()
        for op in self.options:
            y_pos+=1
            stdscr.addstr(y_pos, round(x_pos[1]/2) - 10, f":: {op['text']}")
            if self.selected_option == op["id"]:
                stdscr.addstr(y_pos, round(x_pos[1]/2) - 10, f">> {op['text']}")
            stdscr.refresh()
    
    def display_header(self, stdscr) -> None:
        y_pos=0
        x_pos=stdscr.getmaxyx()
        for line in self.header_template:
            stdscr.addstr(y_pos, round(x_pos[1]/2) - 10, line)
            y_pos+=1
            stdscr.refresh()
    
    def display_key_debugger(self, stdscr, key) -> None:
        y_pos=stdscr.getmaxyx()[0]
        stdscr.addstr(y_pos - 3,0, f"Tecla:( {key} )")
        stdscr.refresh()
    
    def display_guide(self, stdscr) -> None:
        y_pos=stdscr.getmaxyx()[0]
        guide = "Para navegar pelas opções, use as setas CIMA e BAIXO. Para sair utilize a tecla HOME e para selecionar uma opção a tecla S."
        stdscr.addstr(y_pos - 10,0, guide)
        stdscr.refresh()
        
    def main(self, stdscr) -> None:
        self.render(stdscr)
        while self.running==True:
            key = stdscr.getkey()
            self.manage_keys(key)
            self.render(stdscr, key)
    
    def manage_keys(self, key:str) -> None:
        match(key):
            case 'KEY_UP':
                if self.selected_option >= 2 and self.selected_option <= len(self.options):
                    self.selected_option = self.selected_option - 1
            case 'KEY_DOWN':
                if self.selected_option < len(self.options) and self.selected_option >= 1:
                    self.selected_option = self.selected_option + 1
            case 'KEY_HOME':
                self.running=False
            case 's':
                self.options[self.selected_option - 1]["action"]()
    
    def render(self, stdscr, key=None) -> None:
        self.display_header(stdscr)
        self.display_options(stdscr)
        #self.display_key_debugger(stdscr, key)
        self.display_guide(stdscr)
        
    def run(self) -> None:
        curses.wrapper(self.main)
