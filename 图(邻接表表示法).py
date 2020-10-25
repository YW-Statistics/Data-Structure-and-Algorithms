# Title: Graph(Adjacency List)
# Time: 2020/10/19
# Author: Vincent

class Graph_AL:
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('mat必须是一个标准的邻接矩阵！')
        self.mat_  = [Graph_AL.out_edges(mat[i], unconn) for i in range(vnum)]
        self.vnum_ = vnum
        self.unconn_ = unconn
    
    # 获取所有顶点数目
    def get_v_count(self):
        return self.vnum_
    
    # 判断顶点下标是否越界
    def v_invalid(self, v):
        return v < 0 or v >= self.vnum_
    
    # 加入顶点
    def add_vertex(self, val):
        self.mat_.append([])
        self.vnum_ += 1
    
    # 加入边
    def add_edge(self, v1, v2, val):
        if self.vnum_ == 0:
            raise IndexError('顶点数量小于2，无法形成边！')
        if self.v_invalid(v1) or self.v_invalid(v2):
            raise IndexError('顶点下标越界！')
        row = self.mat_
        i = 0
        while i < len(row):
            # 如果已经存在这条边的连接，那么只需要修改权值
            if row[i][0] == v2:
                self.mat_[v1][v2] == [v2, val]
                return
            # 如果不存在这条边，那么跳出循环直接insert
            if row[i][0] > v2:
                break
            i += 1
        self.mat_[v1].insert(i, [v2, val])
        
    # 获取边的信息
    def get_edge(self, v1, v2):
        if self.vnum_ == 0:
            raise IndexError('顶点数量小于2，无法形成边！')
        if self.v_invalid(v1) or self.v_invalid(v2):
            raise IndexError('顶点下标越界！')
        for i, val in self.mat_[v1]:
            if i == v2:
                return val
        return self.unconn_
    
    def out_edges_(self, v):
        if self.v_invalid(v):
            raise IndexError('顶点下标越界！')
        return self.out_edges(self.mat_[v], self.unconn_)
    
    # 获取所有的出边信息
    @staticmethod
    def out_edges(row, unconn):
        output = []
        for i in range(len(row)):
            if row[i] != unconn:
                output.append([i, row[i]])
        return output
    
    
if __name__ == '__main__':
    mat = [[1,0,0,1], [0,1,0,0], [0,0,1,0], [1,0,0,1]]
    sample = Graph_AL(mat)
    print(sample.mat_)
    print('\n')
    
    print(sample.get_v_count())
    print('\n')
    
    sample.add_vertex(3)
    print(sample.mat_)
    print('\n')
    
    print(sample.get_edge(0, 3))
    print('\n')
