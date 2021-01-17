

class StemLemPipeline:

    def __init__(self, func_list):

        assert len(func_list) > 0, "empty list of functions!"

        for f in func_list:
            assert callable(f), 'func_list must be the list of callable objects'
        
        self.funcs = func_list

    
    def __call__(self, arg):

        answer = self.funcs[0](arg)

        for f in self.funcs[1:]:
            answer = f(answer)
        
        return answer



