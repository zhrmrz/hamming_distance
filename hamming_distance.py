class Sol:
    def hamming_distance(self,x,y):
        res=0
        while x or y :
            res+=(x%2)^(y%2)
            x>>=1
            y>>=1
        return res


if __name__ == '__main__':
    p1=Sol()
    print(p1.hamming_distance(1,4))
