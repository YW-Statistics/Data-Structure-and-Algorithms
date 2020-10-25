# Title: Graph(Matrix)
# Time: 2020/10/19
# Author: Vincent

class Graph_mat:
    def __init__(self, mat, unconn=0):
        '''
        
        Parameters
        ----------
        mat : matrix
            图的邻接矩阵.
        uncon : float、string、int, etc.
            主要用于表示无关联时的数值. The default is 0.

        Returns
        -------
        None.

        '''
        vnum = len(mat) # 顶点数
        for x in mat:
            if len(x) != vnum:
                raise ValueError('mat必须是一个标准的邻接矩阵！')
        self.mat_ = [mat[i][:] for i in range(vnum)] # 拷贝mat
        self.unconn_ = unconn
        self.vnum_ = vnum
    
    # 获得顶点的数目
    def get_v_count(self):
        return self.vnum_
    
    # 判断顶点下标是否越界
    def vertex_invalid(self, v):
        return v < 0 or v >= self.vnum_
    
    # 加入顶点
    def add_vertex(self, val):
        self.mat_.append([self.unconn_ for _ in range(self.vnum_)])
        self.vnum_ += 1
        for x in self.mat_:
            x.append(self.unconn_)
        self.mat_[self.vnum_-1][self.vnum_-1] = val
            
    # 加入一条边
    def add_edge(self, v1, v2, val):
        if self.vertex_invalid(v1) or self.vertex_invalid(v2):
            raise IndexError('顶点下标越界！')
        self.mat_[v1][v2] = val
        
    # 获取任意边的信息
    def get_edge(self, v1, v2):
        if self.vertex_invalid(v1) or self.vertex_invalid(v2):
            raise IndexError('顶点下标越界！')
        return self.mat_[v1][v2]
    
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
    sample = Graph_mat(mat)
    print(sample.mat_)
    print('\n')
    
    print(sample.get_v_count())
    print('\n')
    
    sample.add_vertex(3)
    print(sample.mat_)
    print('\n')
    
    print(sample.get_edge(1, 2))
    print('\n')
    
    print(sample.out_edges(sample.mat_[0], 0))