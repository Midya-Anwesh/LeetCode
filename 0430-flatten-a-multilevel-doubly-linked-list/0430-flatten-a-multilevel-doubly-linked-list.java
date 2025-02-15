/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        if (head == null){
            return null;
        }
        Node node = head;
        while (node != null){ // Check all nodes in current level
            if (node.child != null){ // If current node has a child
                Node newNext = flatten(node.child); // Recursively flatten the child and save it's head to a pointer
                node.child = null; // Make the child pointer null
                if (node.next == null){ // If there is no next node on current level
                    node.next = newNext; // Add the head of flattened list to the next pointer
                    newNext.prev = node;
                    break; // Break out of the loop
                }
                // Get to the last node of flattend list
                Node temp = newNext;
                while (temp.next != null){
                    temp = temp.next;
                }
                // Add next of current node to next of last node of flattened list
                temp.next = node.next;
                temp.next.prev = temp;

                // Make head of flattened list next of current node
                node.next = newNext;
                newNext.prev = node;

                // Pick the node that was next of current node for next iteration
                node = temp.next;
            }
            else{ // If current node doesn't contain any child go to next node
                node = node.next;
            }
        }
        return head;
    }
}