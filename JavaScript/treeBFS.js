let bfs = function (node) {
    let queue = [node];
    const values = [];
    while (queue.length > 0) {
      const head = queue[0];
      queue = queue.slice(1);       // 반복문 끝내기 위해서
      console.log("queue", queue);
        
      head.children.forEach((child) => {
        console.log("child", child)
        queue.push(child)
      })
    }
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
  