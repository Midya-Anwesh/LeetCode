"""
Credit for the formula: https://leetcode.com/u/anwendeng/
A connected component with v vertices is said to be complete ⟺ its edges number e = (v(v-1)) / 2
⟺ for all i in this component: deg[i]=v−1 (ps other equivalent condition)
Have a nice day.
"""
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        component, degree, partOfComponent = dict(), dict(), dict()
        for vertex in range(n):
            partOfComponent[vertex] = vertex
            component[vertex] = {'vertices': {vertex:0}, 'edges': 0}
            degree[vertex] = 0

        for u, v in edges:
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1

            # If u is not part of any component
            if not (u in partOfComponent):
                # If v is part of a component
                if v in partOfComponent:
                    compo = partOfComponent[v]
                    partOfComponent[u] = compo
                    component[compo]['vertices'].update({u:0})
                    component[compo]['edges'] += 1
                # If u and v both aren't part of any component
                else:
                    # Create a new component containing u and v
                    partOfComponent[u], partOfComponent[v] = u, u
                    component[u]['vertices'] = {u:0, v:0}
                    component[u]['edges'] += 1

            # If u is part of a component
            else:
                # If v is not part of any component
                if not (v in partOfComponent):
                    compo = partOfComponent[u]
                    partOfComponent[v] = compo
                    component[compo]['vertices'].update({v:0})
                    component[compo]['edges'] += 1
                # If both u and v are part of a component
                else:
                    compoU, compoV = partOfComponent[u], partOfComponent[v]
                    # If Both are part of same component
                    if compoU == compoV:
                        component[compoU]['edges'] += 1
                    # Else if they are from different component and size of components differ then add smaller to bigger one
                    # Else add any one to another
                    elif len(component[compoU]['vertices']) >= len(component[compoV]['vertices']):
                        component[compoU]['vertices'] |= component[compoV]['vertices']
                        component[compoU]['edges'] += component[compoV]['edges'] + 1
                        for vertex in component[compoV]['vertices']:
                            partOfComponent[vertex] = compoU
                        component.pop(compoV)
                    else:
                        component[compoV]['vertices'] |= component[compoU]['vertices']
                        component[compoV]['edges'] += component[compoU]['edges'] + 1
                        for vertex in component[compoU]['vertices']:
                            partOfComponent[vertex] = compoV
                        component.pop(compoU)
            
        noOfCompleteComponent = 0
        # Now check every component
        for compo in component:
            noOfVertex = len(component[compo]['vertices'])
            isComplete = ( component[compo]['edges'] == (((noOfVertex-1)*noOfVertex)//2) )
            if isComplete:
                for vertex in component[compo]['vertices']:
                    if degree[vertex] != noOfVertex-1:
                        isComplete = False
                        break
            noOfCompleteComponent += isComplete
        return noOfCompleteComponent