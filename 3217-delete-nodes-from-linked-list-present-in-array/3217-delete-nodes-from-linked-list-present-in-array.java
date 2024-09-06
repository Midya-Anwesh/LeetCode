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
    public ListNode modifiedList(int[] nums, ListNode head) {
        HashSet<Integer>set=new HashSet<>();
        for (int i = 0; i < nums.length; set.add(nums[i++]));

        ListNode pre = null;
        ListNode curr = head;

        while (curr != null){
            if (set.contains(curr.val)){
                if (curr == head){
                    head = head.next;
                    curr = head;
                }
                else{
                    pre.next = curr.next;
                    curr = pre.next;
                }
            }
            else{
                pre = curr;
                curr = curr.next;
            }
        }
        return head;
    }
}