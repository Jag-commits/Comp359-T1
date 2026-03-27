package implementations;
public class QuickFind {
    private int[] id;

    public QuickFind(int n) {
        id = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;
        }
    }

    public int find(int p) {
        return id[p]; // in constant time 
    }

    public boolean connected(int p, int q) {
        return find(p) == find(q); //T/F statement
    }
    
    public void union(int p, int q) {
        int pid = find(p);
        int qid = find(q);

        for (int i = 0; i < id.length; i++) { 
            if (id[i] == pid) {
                id[i] = qid;
            }
        }
    }

    //quick test to see if it works
    public static void main(String[] args) {
        QuickFind uf = new QuickFind(50);
        uf.union(12, 15);
        uf.union(33, 45);
        System.out.println(uf.connected(12, 15)); //should be true
        System.out.println(uf.connected(13, 45)); //should be false
        
    }
}