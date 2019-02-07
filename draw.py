class Draw():
    def draw_q(self):
        print("Q")
        for i in self.q_table:
            for j in i:
                print(int(j),"\t",end=' ')
            print("")
                
    def draw_r(self):
        print("R")
        for i in self.reward_table:
            for j in i:
                print(int(j),"\t",end=' ')
            print("")