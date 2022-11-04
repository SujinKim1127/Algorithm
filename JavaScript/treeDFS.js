let dfs = function (node) {
    let values = [node.value]
  
    node.children.forEach((n) => {
      values = values.concat(dfs(n))
    })
    
    // 탐색되는 순서대로 노드의 값이 저장된 배열 리턴
    return values;
  };
  
  let Node = function (value) {
    this.value = value;
    this.children = [];
  };
  
  Node.prototype.addChild = function (child) {
    this.children.push(child);
    return child;
  };
  