/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private int getLength(ListNode head){
        int count = 0;
        for (; head != null; count++, head = head.next);
        return count;
    }
    public ListNode[] splitListToParts(ListNode head, int k) {
        int len = getLength(head), base_len = len/k, i = 0;
        ListNode ret[] = new ListNode[k];
        for (; i < k; i++){
            ret[i] = head;
            int curr_len = base_len+((i < len%k)? 1:0);
            for (int j = 0; j < curr_len-1; j++){
                head = head.next;
            }
            ListNode temp = head;
            if (head != null){
                head = head.next;
                temp.next = null;
            }
            else{
                break;
            }
        }
        while (i++ < k){
            ret[i-1] = null;
        }
        return ret;
    }
}