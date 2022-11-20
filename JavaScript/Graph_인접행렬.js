function createMatrix(edges) {
    const max = Math.max(...edges.flat().filter(el => typeof(el) === 'number')) + 1
    const result =  Array.from(new Array(max), () => new Array(max).fill(0))
    
    for(let edge of edges){
      let from = edge[0]
      let to = edge[1]
      if(edge[2] === 'directed'){
        result[from][to] = 1
      }
      if(edge[2] === 'undirected'){
        result[from][to] = 1
        result[to][from] = 1
      }
    }
    return result
  }