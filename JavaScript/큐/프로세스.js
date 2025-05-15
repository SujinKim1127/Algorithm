function solution(priorities, location) {
  const queue = [];
  for (let i = 0; i < priorities.length; i++) {
    queue.push({ name: i, priority: priorities[i] });
  }
  let order = 0;
  while (queue.length > 0) {
    const current = queue.shift();
    const hasHighPriority = queue.some(
      (item) => item.priority > current.priority
    );
    if (hasHighPriority) {
      queue.push(current);
    } else {
      order++;
      if (current.name === location) return order;
    }
  }
}
