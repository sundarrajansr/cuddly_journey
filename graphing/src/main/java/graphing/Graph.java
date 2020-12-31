package graphing;


import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.IntStream;

public class Graph {
    private Integer[] vertices;
    private LinkedList<Integer>[] edges;
    private HashMap<Integer, String> vertexToName;
    private HashMap<String, Integer> nameToVertex;
    private int size;


    public Graph(int v) {
        this.size = v;
        this.vertices = new Integer[v];
        edges = new LinkedList[v];
        IntStream.range(0, v).forEach(i -> {
            edges[i] = new LinkedList<Integer>();
        });
    }

    private void validateVertex (int v)
    {
        if (v < 0 && v >= size)
            throw new IllegalArgumentException("Invalid vertex passed " + v);
    }
    
    public List<Integer> neighbours(int v) {
        validateVertex(v);
        return edges[v];
    }

    public boolean forEachNeighbour(int v, Consumer<? super Integer> consumer) {
        validateVertex(v);
        edges[v].forEach(consumer);
        return false;
    }

}
