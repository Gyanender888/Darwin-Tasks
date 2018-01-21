import math, time


class Custom_Random:
    def __init__(self, low=0, high=0,samples=None):
        if (low < 2):
            low = 2
        if (high < 2):
            high = 9223372036854775807
        self.m_min = low
        self.m_max = high
        self.m_seed = time.time()
        self.samples=samples+1
        self.output=[]

    def Next(self):
        a = self.m_min
        m = self.m_max
        q = math.trunc(m / a)
        r = m % a
        hi = self.m_seed / q
        lo = self.m_seed % q
        x = (a * lo) - (r * hi)
        if (x < a):
            x += a
        self.m_seed = x
        self.m_seed %= m
        if (self.m_seed < a):
            self.m_seed += a
        return int(self.m_seed)

    def generate(self):
        while(len(self.output)!=self.samples):
            temp=self.Next()
            if ((float(temp)/self.m_max)*100)<23 and len([i for i in self.output if ((float(i)/self.m_max)*100)<23])<((float(23)/100)*self.samples):
                self.output.append(temp)
            elif (float(temp)/self.m_max)*100>23 and len([i for i in self.output if ((float(i)/self.m_max)*100)>23])<(float(77)/100)*self.samples:
                self.output.append(temp)


s=Custom_Random(low=0, high=100,samples=10)
s.generate()
print s.output


