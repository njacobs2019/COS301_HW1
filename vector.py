class vector:
    def __init__(self, in_vec=None):
        if in_vec:
            self.vec = in_vec
        else:
            self.vec = []
    
    def append(self, num):
        self.vec.append(num)
        return self
    
    def add(self, vec2):
        self.test_len(vec2)
        for i in range(len(self.vec)):
            self.vec[i] += vec2.vec[i]
        return self
    
    def subtract(self, vec2):
        self.test_len(vec2)
        for i in range(len(self.vec)):
            self.vec[i] -= vec2.vec[i]
        return self

    def multiply(self, vec2):
        self.test_len(vec2)
        for i in range(len(self.vec)):
            self.vec[i] *= vec2.vec[i]
        return self

    def divide(self, vec2):
        self.test_len(vec2)
        for i in range(len(self.vec)):
            self.vec[i] /= vec2.vec[i]
        return self

    def div(self, vec2):
        self.test_len(vec2)
        for i in range(len(self.vec)):
            self.vec[i] = self.vec[i] // vec2.vec[i]
        return self
    
    def mod(self, vec2):
        self.test_len(vec2)
        for i in range(len(self.vec)):
            self.vec[i] = self.vec[i] % vec2.vec[i]
        return self

    def negate(self):       
        for i in range(len(self.vec)):
            self.vec[i] *= -1
        return self

    def __str__(self):
        if len(self.vec)==0:
            return "()"
        
        elif len(self.vec)==1:
            return f"({self.vec[0]},)"
        
        out = "("
        for i, num in enumerate(self.vec):
            out = out + str(num)
            if i != len(self.vec)-1:
                out = out + ", "
        out = out + ")"
        return out
    
    def test_len(self, vec2):
        if len(self.vec) != len(vec2.vec):
            ## Throw an error
            print("ERROR: lists are not the same length")
            exit(1)