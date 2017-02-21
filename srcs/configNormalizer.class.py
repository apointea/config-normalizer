import os

class configNormalizer:

    script_dir = os.path.dirname(os.path.realpath(__file__))
    def_res = os.path.join(script_dir, '../res')
    def_models = os.path.join(def_res, 'models')
    def_patterns = os.path.join(def_res, 'patterns')

    def __init__(self, modelsDir=def_models, patternsDir=def_patterns):
        self.modelsDir = modelsDir
        self.patternsDir = patternsDir
