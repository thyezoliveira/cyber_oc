class Cyber_oc:
    def __init__(self):
        self.version="1.0"
        self.author="Thyéz de oliveira"
        self.setup_header()
        self.setup_main_options()

    def setup_header(self):
        self.header_template=f"""
        ----------------------
        ======================
        Cyber Ocelot {self.version}
        ======================
        ----------------------
        [Author: {self.author}]
        """
    
    def setup_main_options(self):
        self.options = ["criar_pasta",
        "criar_arquivo",
        "rodar_script",
        "ativar_virtual_env"
        ]
        
    def criar_pasta(self):
        pass
    
    def criar_arquivo(self):
        pass
    
    def rodar_script(self):
        pass
    
    def ativar_virtual_env(self):
        pass
    
    def display_options(self):
        for op in self.options:
            print(f":: {op}")
            
    def print_header(self):
        print(self.header_template)
    
    def run(self):
        self.print_header()
        self.display_options()