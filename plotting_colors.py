import matplotlib.pyplot as plt
import cycler
class color_load:
    def __init__(self, col_dict):
        self.col_dict = col_dict
        self.set_mpl()
    def set_mpl(self):
        self.names = []
        self.hexes = []
        for k,v in self.col_dict.items():
            self.names.append(k)
            self.hexes.append(v)
        cyc_col = cycler.cycler(color=self.hexes)
        plt.rcParams['axes.prop_cycle'] = cyc_col
    def get_dict(self):
        return self.col_dict

fall_colors={'red':'#A4243B',
'yellow':'#D8973C',
'green':'#22637C',
'blue':'#CA4FE8',
'purple':'#BD632F',
'black':'#000000'}

if __name__ == '__main__':
    a = color_load(fall_colors)
    a.set_mpl()
    print( a.get_dict())
