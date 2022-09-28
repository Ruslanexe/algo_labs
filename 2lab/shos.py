root = -1
graph = {}
with open("input.txt","r") as input_file:
    root = int(input_file.readline())
    line = input_file.readline()
    while line:
      start,to = map(int,line.split(","))
      if not start in graph:
        graph.update({start: []})
      graph[start].append(to)
      line = input_file.readline()

def minimumDepth(root):
    if root is None:
      return 0
    q = []
    q.append((root,1))
    while q:
      antonio, dist = q.pop(0)
      if not antonio in graph:
        return dist
      for next_antonio in graph[antonio]:
        q.append((next_antonio,dist+1))


with open("output.txt", "w+") as output_file:
        output_file.write(str(minimumDepth(root)))
        